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

scores = {
    "apps": 0,
    "front": 0,
    "back": 0,
    "analise_sis": 0,
    "dados": 0,
    "seguranca": 0,
    "eng_software": 0,
}

lista_perguntas= []

def perguntar(x):
    while(len(lista_perguntas) < x):
        a = randint(1, x)
        if a not in lista_perguntas:
            print("/--------------/")
            b = str(input(perguntas[a]["pergunta"]))
            if b[0] == "s" or b[0] == "S":
                for score in perguntas[a]["sim"]:
                    scores[score] += 10
            elif b[0] == "n" or b[0] == "N":
                for score in perguntas[a]["nao"]:
                    scores[score] += 10
            else:
                print("Input inválido, insira apenas [s] ou [n]")
                continue

            lista_perguntas.append(a)
    print("/--------------/")
    print("Fim do programa. Resultados:")
    return scores