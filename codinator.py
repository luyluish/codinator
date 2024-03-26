from random import randint

print("\033[1;34mBEM VINDO AO CODINATOR !!\033[m")

perguntas = {
    1:  {"pergunta": "Você se considera um bom líder em grupos? [s/n] ", "sim": {"eng_software", "back"}, "nao": {"front"}},
    2:  {"pergunta": "Você prefere trabalhar sozinho e não receber ordens? [s/n] ", "sim": {"front"}, "nao": {"eng_software", "analise_sis", "back", "seguranca"}},
    3:  {"pergunta": "Você traz ideias novas constantemente para resolver problemas? [s/n] ", "sim": {"eng_software", "analise_sis", "back", "seguranca"}, "nao": {"front"}},
    4:  {"pergunta": "Você se considera uma pessoa criativa? [s/n] ", "sim": {"front", "apps", "seguranca"}, "nao": {"dados"}},
    5:  {"pergunta": "Você se considera uma pessoa organizada? [s/n] ", "sim": {"eng_software", "analise_sis", "back", "seguranca"}, "nao": {"front"}},
    6:  {"pergunta": "Você gosta de construir coisas novas? [s/n] ", "sim": {"eng_software", "apps", "back", "front"}, "nao": {"seguranca"}},
    7:  {"pergunta": "Você é contratado de alguma empresa? [s/n] ", "sim": {"eng_software", "seguranca", "dados", "back"}, "nao": {"front"}},
    8:  {"pergunta": "Você tem interesse em trabalhar na web? [s/n] ", "sim": {"eng_software", "front", "back", "analise_sis"}, "nao": {"dados", "apps", "seguranca"}},
    9:  {"pergunta": "Você gosta de matemática e lógica? [s/n] ", "sim": {"dados", "analise_sis", "eng_software", "back", "seguranca"}, "nao": {"front"}},
    10: {"pergunta": "Você gosta de estatística ou finanças? [s/n] ", "sim": {"eng_software", "analise_sis"}, "nao": {"front"}},
    11: {"pergunta": "Você trabalharia com um alto volume de informações? [s/n] ", "sim": {"dados", "seguranca", "back"}, "nao": {"front", "apps"}},
    12: {"pergunta": "Você gostaria de expressar seu lado artístico no seu trabalho? [s/n] ", "sim": {"front", "apps"}, "nao": {"dados", "seguranca", "back"}},
    13: {"pergunta": "Você gostaria de trabalhar criando jogos? [s/n] ", "sim": {"apps", "back"}, "nao": {"dados", "seguranca"}},
    14: {"pergunta": "Você gosta de lidar diretamente com clientes no desenvolvimento de um projeto? [s/n] ", "sim": {"front", "analise_sis", }, "nao": {"dados", "seguranca", "back"}}
}

perguntasFinais = {
    "apps": {"pergunta": "Você gostaria de trabalhar com dispositivos mobile? [s/n] "},
    "front": {"pergunta": "Você gosta de design ou desenho? [s/n] "},
    "back": {"pergunta": "Você gostaria de trabalhar na parte lógica e operacional dentro de um ambiente web? [s/n] "},
    "analise_sis": {"pergunta": "Você gosta de explorar conteúdos de maneira minuciosa, analisando detalhes de cada estrutura? [s/n] "},
    "seguranca": {"pergunta": "Você gostaria de proteger a empresa em que trabalha ciberneticamente? [s/n] "},
    "dados": {"pergunta": "Você gostaria de coletar e interpretar dados fornecidos a você da empresa em que trabalha? [s/n] "},
    "eng_software": {"pergunta": "Você gostaria de ser responsável por projetar, desenvolver e manter sistemas de softwares? [s/n] "}
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
        print("""
            \033[1;36mDesenvolvimento de Aplicativos é o processo de criação de software para dispositivos
            móveis ou computadores. Envolve design, codificação, teste e implementação de aplicativos
            usando linguagens de programação específicas da plataforma. O objetivo é criar aplicativos
            funcionais e intuitivos que atendam às necessidades dos usuários.
            \033[m""")
    elif vencedor == "front":
        print("Front End")
        print("""
            \033[1;36mFront-end refere-se à criação da interface de usuário de sites e aplicativos web. 
            Desenvolvedores Front-end usam HTML, CSS e JavaScript para projetar e 
            implementar elementos visuais e interativos. Eles colaboram com designers e desenvolvedores Back-end
            para criar experiências de usuário intuitivas e responsivas. 
            \033[m""")
    elif vencedor == "back":
        print("Back End")
        print("""
            \033[1;36mBack-end é a parte do desenvolvimento web que lida com a lógica e o armazenamento de dados
            por trás de um site ou aplicativo. Os desenvolvedores Back-end usam linguagens como Python,
            Java ou Ruby para criar e manter servidores, APIs e bancos de dados. Eles garantem a segurança,
            escalabilidade e desempenho do sistema, trabalhando em colaboração com equipes de Front-end e DevOps.
            \033[m""")
    elif vencedor == "analise_sis":
        print("Analise de Sistemas")
        print("""
            \033[1;36mAnálise de Sistemas é o processo de entender as necessidades de um sistema de informação,
            identificar problemas e propor soluções por meio do uso de tecnologia da informação. 
            Os analistas de sistemas utilizam técnicas de investigação e modelagem para projetar 
            sistemas que atendam às demandas organizacionais e melhorem a eficiência dos processos.
            \033[m""")
    elif vencedor == "dados":
        print("Dados")
        print("""
            \033[1;36mCientista de Dados é um profissional que analisa grandes conjuntos de dados usando técnicas estatísticas
            e de machine learning para extrair insights e informação útil. Eles usam ferramentas como Python e R 
            para processar e visualizar dados, ajudando as organizações a tomar decisões informadas e estratégicas.
            \033[m""")
    elif vencedor == "seguranca":
        print("Segurança da Informação")
        print("""
            \033[1;36mSegurança da Informação abrange medidas e práticas para proteger dados e sistemas contra ameaças.
            Isso inclui técnicas como criptografia, controle de acesso e monitoramento para garantir a confidencialidade,
            integridade e disponibilidade das informações, visando mitigar riscos de segurança.
            \033[m""")
    elif vencedor == "eng_software":
        print("Engenharia de Software")
        print("""
            \033[1;36mEngenharia de Software é a aplicação de princípios de engenharia para desenvolver software de forma eficiente.
            Envolve análise de requisitos, design, implementação, teste e manutenção de sistemas de software. 
            O objetivo é produzir software de alta qualidade, entregue dentro do prazo e do orçamento estabelecidos.
            \033[m""")

def main():
    print("Iniciando o programa.")
    perguntarAmplas()
    perguntar_especifico()

if __name__ == '__main__':
    main()
