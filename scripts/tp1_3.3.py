import os
from sql_queries import *

def interface():

    quited = invalid = False
    while (not quited):
        print('------------------------Bem vindo ao Dashboard---------------------')
        print('selecione uma opção(q para sair): \n')
        print(""" a) Dado um produto:
        Listar os 5 comentários mais úteis e com maior avaliação
        Listar os 5 5 comentários mais úteis e com menor avaliação\n""")
        print(""" b) Dado um produto:
        Listar os produtos similares com maiores vendas do que ele\n""")
        print(""" c) Dado um produto: 
        Mostrar a evolução diária das médias de avaliação ao longo
        do intervalo de tempo coberto no arquivo de entrada\n""")
        print(""" d) Listar os 10 produtos líderes de venda em cada grupo de
    produtos\n""")
        print(""" e) Listar os 10 produtos com a maior média de  avaliações úteis
    positivas por produto\n""")
        print(""" f) Listar a 5 categorias de produto com a maior média de
    avaliações úteis positivas por produto\n""")
        print(""" g) Listar os 10 clientes que mais fizeram comentários por
    grupo de produto\n""")
        if invalid:
            print('Comando inválido!')
        quited, invalid = options(input())
        os.system('cls' if os.name == 'nt' else 'clear')


def options(selected):

    if selected == 'a':
        os.system('cls' if os.name == 'nt' else 'clear')
        entry = input('Insira o ASIN de um produto: ')

        while True:
            if check_product_exists(entry):
                top_reviews(entry)
                break
            else:
                print("Produto não encontrado!")
                entry = input('Insira o ASIN de um produto: ')

        input("Press Enter para continuar...")
        return False, False
    
    elif selected == 'b':
        os.system('cls' if os.name == 'nt' else 'clear')
        entry = input('Insira o ASIN de um produto: ')
        input("Press Enter para continuar...")
        return False, False
    elif selected == 'c':
        os.system('cls' if os.name == 'nt' else 'clear')
        entry = input('Insira o ASIN de um produto: ')
        #insira a função aqui
        input("Press Enter para continuar...")
        return False, False
    elif selected == 'd':
        os.system('cls' if os.name == 'nt' else 'clear')
        #insira a função aqui
        input("Press Enter para continuar...")
        return False, False
    elif selected == 'e':
        os.system('cls' if os.name == 'nt' else 'clear')
        #insira a função aqui
        input("Press Enter para continuar...")
        return False, False
    elif selected == 'f':
        os.system('cls' if os.name == 'nt' else 'clear')
        #insira a função aqui
        input("Press Enter para continuar...")
        return False, False
    elif selected == 'g':
        os.system('cls' if os.name == 'nt' else 'clear')
        #insira a função aqui
        input("Press Enter para continuar...")
        return False, False
    elif selected == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        #insira a função aqui
        print('volte sempre! :D')
        return True, False
    else:
        return False, True


if __name__ == '__main__':
    interface()