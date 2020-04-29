import requests
import re


def url(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    return url


def main():
    cep = input('Digite um cep que gostaria de procurar na base de dados sem pontuação, ex: (00000000): ').strip()

    reposta = requests.get(url(cep))

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

if __name__ == '__main__':
    main()
