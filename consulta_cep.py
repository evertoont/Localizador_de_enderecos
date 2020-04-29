import requests
import re


def url(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    return url


def main():
    cep = input('Digite um cep que gostaria de procurar na base de dados sem pontuação, ex: (00000000): ').strip()

    reposta = requests.get(url(cep))

    dados = reposta.json()

    try:

        dados = reposta.json()

        print(f"""
        =========================================
        Cep: {dados['cep']}
        Logradouro: {dados['logradouro']}
        Bairro: {dados['bairro']}
        Localidade: {dados['localidade']}
        UF: {dados['uf']}
        =========================================
        """)

    except:
        print("\nErro ao encontrar dados do cep! Verfique o número e digite novamente.")

if __name__ == '__main__':
    main()
