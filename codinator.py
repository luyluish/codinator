from random import randint

print("\033[1;34mBEM VINDO AO CODINATOR !!\033[m")

perguntas = {
    1:  {"pergunta": "(Ampla) Você se considera um bom líder em grupos? [s/n] ", "sim": {"eng_software"}, "nao": {"front"}},
    2:  {"pergunta": "(Ampla) Você prefere trabalhar sozinho e não receber ordens? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    3:  {"pergunta": "(Ampla) Você traz ideias novas constantemente para resolver problemas? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    4:  {"pergunta": "(Ampla) Você se considera uma pessoa criativa? [s/n] ", "sim": {"front", "apps"}, "nao": {"dados"}},
    5:  {"pergunta": "(Ampla) Você se considera uma pessoa organizada? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    6:  {"pergunta": "Você gosta de construir coisas novas? [s/n] ", "sim": {"eng_software", "apps", "back", "front"}, "nao": {"seguranca"}},
    7:  {"pergunta": "Você é contratado de alguma empresa? [s/n] ", "sim": {"eng_software", "seguranca", "dados", "back"}, "nao": {"front"}},
    8:  {"pergunta": "Você tem interesse em trabalhar na web? [s/n] ", "sim": {"eng_software", "front", "back", "analise_sis"}, "nao": {"dados", "apps", "seguranca"}},
    9:  {"pergunta": "Você gosta de matemática e lógica? [s/n] ", "sim": {"dados", "analise_sis", "eng_software", "back"}, "nao": {"front"}},
    10: {"pergunta": "Você gosta de estatística ou finanças? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    11: {"pergunta": "Você trabalharia com um alto volume de informações? [s/n] ", "sim": {"dados", "seguranca", "back"}, "nao": {"front", "apps"}},
    12: {"pergunta": "Você gostaria de expressar seu lado artístico no seu trabalho? [s/n] ", "sim": {"front", "apps"}, "nao": {"dados", "seguranca"}},
    13: {"pergunta": "Você gostaria de trabalhar criando jogos? [s/n] ", "sim": {"apps"}, "nao": {"dados", "seguranca"}},
    14: {"pergunta": "Você gosta de lidar diretamente com clientes no desenvolvimento de um projeto? [s/n] ", "sim": {"front", "analise_sis", }, "nao": {"dados", "seguranca"}}
}

perguntasFinais = {
    "apps": {"pergunta": "(Especifica) Você gostaria de trabalhar com dispositivos mobile? [s/n] "},
    "front": {"pergunta": "(Específica) Você gosta de design ou desenho? [s/n] "},
    "back": {"pergunta": "(Especifica) Back? [s/n] "},
    "analise_sis": {"pergunta": "(Especifica) Análise? [s/n] "},
    "seguranca": {"pergunta": "(Especifica) Dados? [s/n] "},
    "dados": {"pergunta": "(Especifica) Segurança? [s/n] "},
    "eng_software": {"pergunta": "(Especifica) Engenharia de Software? [s/n] "}
}

scores = {
    "apps": 0,
    "front": 0,
    "back": 0,
    "analise_sis": 0,
    "seguranca": 0,
    "dados": 0,
    "eng_software": 0
}

lista_perguntas = []

def checar_vencedor():
    for area in scores:
        if scores[area] == 5:
            return area
    return -1

def checar_maior():
    maior = -999
    indice_maior = -999
    for area in scores:
        if scores[area] > maior:
            maior = scores[area]
            indice_maior = area
    return indice_maior

def perguntarAmplas(x = 5):
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


def perguntar_especifico(y = 14):
    print("/--------------/")
    while checar_vencedor() == -1:
        c = randint(6, y)
        if c not in lista_perguntas:
            d = str(input(perguntas[c]["pergunta"]))
            lista_perguntas.append(c)
            if d[0] == 's' or d[0] == 'S':
                for score in perguntas[c]["sim"]:
                    scores[score] += 1
            elif d[0] == 'n' or d[0] == 'N':
                for score in perguntas[c]["nao"]:
                    scores[score] += 1
        if len(lista_perguntas) >= 14:
            break
    if len(lista_perguntas) < 14:
        perguntarFinal(checar_vencedor())
    else:
        encerrarPrograma(checar_maior())

def perguntarFinal(area):
    resposta = str(input(perguntasFinais[area]["pergunta"]))
    if resposta[0] == "s" or resposta[0] == "S":
        encerrarPrograma(area)
    elif resposta[0] == "n" or resposta[0] == "N":
        scores[area] += 1
        perguntar_especifico()

def encerrarPrograma(vencedor):
    print("----- Resultado -----")
    if vencedor == "apps":
        print("Apps")
    elif vencedor == "front":
        print("Front End")
        print("""
            Front-end refere-se à criação da interface de usuário de sites e aplicativos web. 
            Desenvolvedores Front-end usam HTML, CSS e JavaScript para projetar e 
            implementar elementos visuais e interativos. Eles colaboram com designers e desenvolvedores Back-end
            para criar experiências de usuário intuitivas e responsivas. 
        """)
    elif vencedor == "back":
        print("Back End")
        print("""
            Back-end é a parte do desenvolvimento web que lida com a lógica e o armazenamento de dados
            por trás de um site ou aplicativo. Os desenvolvedores Back-end usam linguagens como Python,
            Java ou Ruby para criar e manter servidores, APIs e bancos de dados. Eles garantem a segurança,
            escalabilidade e desempenho do sistema, trabalhando em colaboração com equipes de Front-end e DevOps.
        """)
    elif vencedor == "analise_sis":
        print("Analise de Sistemas")
        print("""
            Análise de Sistemas é o processo de entender as necessidades de um sistema de informação,
            identificar problemas e propor soluções por meio do uso de tecnologia da informação. 
            Os analistas de sistemas utilizam técnicas de investigação e modelagem para projetar 
            sistemas que atendam às demandas organizacionais e melhorem a eficiência dos processos.
        """)
    elif vencedor == "dados":
        print("Dados")
        print("""
            Cientista de Dados é um profissional que analisa grandes conjuntos de dados usando técnicas estatísticas
            e de machine learning para extrair insights e informação útil. Eles usam ferramentas como Python e R 
            para processar e visualizar dados, ajudando as organizações a tomar decisões informadas e estratégicas.""")
    elif vencedor == "seguranca":
        print("Segurança da Informação")
        print("""
            Segurança da Informação abrange medidas e práticas para proteger dados e sistemas contra ameaças.
            Isso inclui técnicas como criptografia, controle de acesso e monitoramento para garantir a confidencialidade,
            integridade e disponibilidade das informações, visando mitigar riscos de segurança.
        """)
    elif vencedor == "eng_software":
        print("Engenharia de Software")
        print("""
            Engenharia de Software é a aplicação de princípios de engenharia para desenvolver software de forma eficiente.
            Envolve análise de requisitos, design, implementação, teste e manutenção de sistemas de software. 
            O objetivo é produzir software de alta qualidade, entregue dentro do prazo e do orçamento estabelecidos.
              """)

def main():
    print("Iniciando o programa.")
    perguntarAmplas()
    perguntar_especifico()

if __name__ == '__main__':
    main()