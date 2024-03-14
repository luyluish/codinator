from random import randint
perguntas = {
    1: {"pergunta": "Você se considera um bom líder em grupos? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    2: {"pergunta": "Você prefere trabalhar sozinho e não receber ordens? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    3: {"pergunta": "Você traz ideias novas constantemente para resolver problemas? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    4: {"pergunta": "Você gosta de design ou desenho? [s/n] ", "sim": {"front", "analise_sis"}, "nao": {"front"}},
    5: {"pergunta": "Você gosta de matemática e lógica? [s/n] ", "sim": {"dados", "analise_sis"}, "nao": {"front"}},
    6: {"pergunta": "Você gosta de estatística ou finanças? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    7: {"pergunta": "Você gosta de construir coisas novas? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    8: {"pergunta": "Você é contratado de alguma empresa? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    9: {"pergunta": "Você tem interesse em trabalhar na web? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    10: {"pergunta": "Você se considera uma pessoa criativa? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    11: {"pergunta": "Você se considera uma pessoa organizada? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    12: {"pergunta": "Você trabalharia com um alto volume de informações? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    13: {"pergunta": "Você gostaria de expressar seu lado artístico no seu trabalho? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    14: {"pergunta": "(Especifica) Você gostaria de trabalhar com dispositivos mobile? [s/n] ", "sim": {"apps"}, "nao": {"back"}},
    15: {"pergunta": "Você gostaria de trabalhar criando jogos? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    16: {"pergunta": "Você gosta de lidar com clientes no desenvolvimento de um projeto? [s/n] ", "sim": {"analise_sis"}, "nao": {"dados"}},
}

perguntasFinais = {
    1: {"pergunta": "(Especifica) Você gostaria de trabalhar com dispositivos mobile? [s/n] ", "nao": {"back"}},
    2: {"pergunta": "(Especifica) Front? [s/n] "},
    3: {"pergunta": "(Especifica) Back? [s/n] "},
    4: {"pergunta": "(Especifica) Análise? [s/n] ", "nao": {"back"}},
    5: {"pergunta": "(Especifica) Dados? [s/n] ", "nao": {"back"}},
    6: {"pergunta": "(Especifica) Segurança? [s/n] ", "nao": {"back"}},
    7: {"pergunta": "(Especifica) Engenharia de Software? [s/n] ", "nao": {"back"}},
}

scores = {
    "apps": 0,
    "front": 0,
    "back": 0,
    "analise_sis": 0,
    "dados": 0,
    "seguranca": 0,
    "eng_software": 0,
}

lista_perguntas = []

def perguntar(x):
    while(len(lista_perguntas) < x):
        for area in scores:
            if scores[area] == 5:
                perguntarFinal(area.index)
        a = randint(1, x)
        if a not in lista_perguntas:
            print("/--------------/")
            b = str(input(perguntas[a]["pergunta"]))
            if b[0] == "s" or b[0] == "S":
                for score in perguntas[a]["sim"]:
                    scores[score] += 1
            elif b[0] == "n" or b[0] == "N":
                for score in perguntas[a]["nao"]:
                    scores[score] += 1
            else:
                print("Input inválido, insira apenas [s] ou [n]")
                continue

            lista_perguntas.append(a)
    print("/--------------/")
    print("Fim do programa. Resultados:")
    return scores

def perguntarFinal(area):
    resposta = str(input(perguntasFinais[area]["pergunta"]))
    if area == 2 or area == 3:
        if resposta[0] == "s" or resposta[0] == "S":
            encerrarPrograma(2)
        elif resposta[0] == "n" or resposta[0] == "N":
            encerrarPrograma(3)
    else:
        if resposta[0] == "s" or resposta[0] == "S":
            encerrarPrograma(area)
        elif resposta[0] == "n" or resposta[0] == "N":
            scores[area] += 1


def encerrarPrograma(vencedor):
    print("Resultado: ")
    match(vencedor):
        case 1:
            print("Apps")
        case 2:
            print("Front End")
        case 3:
            print("Back End")
        case 4:
            print("Analise de Sistemas")
        case 5:
            print("Dados")
        case 6:
            print("Segurança")
        case 7:
            print("Engenharia de Software")