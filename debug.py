from random import randint

perguntas = {
    1:  {"pergunta": "(Ampla) Você se considera um bom líder em grupos? [s/n] ", "sim": {"eng_software"}, "nao": {"front"}},
    2:  {"pergunta": "(Ampla) Você prefere trabalhar sozinho e não receber ordens? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    3:  {"pergunta": "(Ampla) Você traz ideias novas constantemente para resolver problemas? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    4:  {"pergunta": "(Ampla) Você se considera uma pessoa criativa? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    5:  {"pergunta": "(Ampla)Você se considera uma pessoa organizada? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    6:  {"pergunta": "Você gosta de construir coisas novas? [s/n] ", "sim": {"eng_software", "apps", "back", "front"}, "nao": {"seguranca"}},
    7:  {"pergunta": "Você é contratado de alguma empresa? [s/n] ", "sim": {"eng_software", "seguranca", "dados", "back"}, "nao": {"front"}},
    8:  {"pergunta": "Você tem interesse em trabalhar na web? [s/n] ", "sim": {"eng_software", "front", "back", "analise_sis"}, "nao": {"dados", "apps", "seguranca"}},
    9:  {"pergunta": "Você gosta de matemática e lógica? [s/n] ", "sim": {"dados", "analise_sis", "eng_software", "back"}, "nao": {"front"}},
    10: {"pergunta": "Você gosta de estatística ou finanças? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    11: {"pergunta": "Você trabalharia com um alto volume de informações? [s/n] ", "sim": {"dados", "seguranca", "back"}, "nao": {"front", "apps"}},
    12: {"pergunta": "Você gostaria de expressar seu lado artístico no seu trabalho? [s/n] ", "sim": {"front", "apps"}, "nao": {"dados", "seguranca"}},
    13: {"pergunta": "Você gostaria de trabalhar criando jogos? [s/n] ", "sim": {"apps"}, "nao": {"dados", "seguranca"}},
    14: {"pergunta": "Você gosta de lidar diretamente com clientes no desenvolvimento de um projeto? [s/n] ", "sim": {"front", "analise_sis", }, "nao": {"dados", "seguranca"}},
}

perguntasFinais = {
    "apps": {"pergunta": "(Especifica) Você gostaria de trabalhar com dispositivos mobile? [s/n] "},
    "front": {"pergunta": "(Específica) Você gosta de design ou desenho? [s/n] "},
    "back": {"pergunta": "(Especifica) Você gosta de design ou desenho? [s/n] "},
    "analise_sis": {"pergunta": "(Especifica) Análise? [s/n] "},
    "seguranca": {"pergunta": "(Especifica) Dados? [s/n] "},
    "dados": {"pergunta": "(Especifica) Segurança? [s/n] "},
    "eng_software": {"pergunta": "(Especifica) Engenharia de Software? [s/n] "},
}

scores = {
    "apps": 0,
    "front": 0,
    "back": 0,
    "analise_sis": 0,
    "seguranca": 0,
    "dados": 0,
    "eng_software": 0,
}

lista_perguntas = []

def perguntarAmplas(x = 5):
    print("Iniciando perguntas amplas.")
    while(len(lista_perguntas) < x):
        print(f"Scores atual: {scores}")
        for area in scores:
            if scores[area] == 5:
                perguntarFinal(area.index)
        a = randint(1, x)
        if a not in lista_perguntas:
            print("/--------------/")
            print(f"Realizando pergunta {a}")
            b = str(input(perguntas[a]["pergunta"]))
            print(perguntas[a]["pergunta"] + b)
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

def checar_vencedor():
    print("Checando vencedor...")
    for area in scores:
        if scores[area] == 5:
            print(f"Vencedor encontrado: {area}")
            return area
    print("Nenhum vencedor ainda.")
    return -1

def perguntar_especifico(y = 14):
    print("Iniciando perguntas específicas.")
    while checar_vencedor() == -1:
        c = randint(6, y)
        if c not in lista_perguntas:
            print(f"Realizando pergunta específica {c}")
            d = str(input(perguntas[c]["pergunta"]))
            print(perguntas[c]["pergunta"] + d)
            lista_perguntas.append(c)
            if d[0] == 's' or d[0] == 'S':
                for score in perguntas[c]["sim"]:
                    scores[score] += 1
            elif d[0] == 'n' or d[0] == 'N':
                for score in perguntas[c]["nao"]:
                    scores[score] += 1
    print(f"Scores após perguntas específicas: {scores}")
    perguntarFinal(checar_vencedor())

def perguntarFinal(area):
    print(f"Iniciando pergunta final para área {area}.")
    resposta = str(input(perguntasFinais[area]["pergunta"]))
    print(perguntasFinais[area]["pergunta"] + resposta)
    if area == "front" or area == "back":
        if resposta[0] == "s" or resposta[0] == "S":
            encerrarPrograma("front")
        elif resposta[0] == "n" or resposta[0] == "N":
            encerrarPrograma("back")
    else:
        if resposta[0] == "s" or resposta[0] == "S":
            encerrarPrograma(area)
        elif resposta[0] == "n" or resposta[0] == "N":
            scores[area] += 1
            perguntar_especifico()

def encerrarPrograma(vencedor):
    print("Resultado: ")
    if vencedor == "apps":
        print("Apps")
    elif vencedor == "front":
        print("Front End")
    elif vencedor == "back":
        print("Back End")
    elif vencedor == "analise_sis":
        print("Analise de Sistemas")
    elif vencedor == "dados":
        print("Dados")
    elif vencedor == "seguranca":
        print("Segurança")
    elif vencedor == "eng_software":
        print("Engenharia de Software")

def main():
    print("Iniciando o programa.")
    perguntarAmplas()
    print(f"Scores após perguntas amplas: {scores}")
    perguntar_especifico()
    print(f"Scores finais: {scores}")

if __name__ == '__main__':
    main()
