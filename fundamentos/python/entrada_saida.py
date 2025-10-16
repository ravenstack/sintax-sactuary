"""Demonstração guiada de leitura e escrita no console em Python.

Este módulo faz parte da trilha de fundamentos do repositório The Syntax Sanctuary e
foi pensado para ser executado no terminal. Ele apresenta três etapas principais:

1. Ler informações digitadas pela pessoa usuária com ``input``.
2. Validar e converter o texto recebido para outros tipos, como ``int``.
3. Mostrar mensagens personalizadas usando f-strings e funções reutilizáveis.

Execute este arquivo diretamente para acompanhar cada passo da coleta de dados.
"""

from typing import Optional


def solicitar_texto(prompt: str, *, permitir_vazio: bool = False) -> str:
    """Lê um texto do console e aplica validação básica.

    Args:
        prompt: Mensagem exibida antes de coletar o valor.
        permitir_vazio: Quando ``False`` (padrão), força a digitar algo diferente de
            vazio.
    """

    while True:
        resposta = input(prompt).strip()

        if resposta or permitir_vazio:
            return resposta

        print("\nOps! Digite ao menos um caractere para continuar.\n")


def solicitar_idade(prompt: str = "Quantos anos você tem? ") -> int:
    """Pergunta a idade ao usuário e retorna um número inteiro não negativo."""

    while True:
        resposta = input(prompt).strip()

        try:
            idade = int(resposta)
        except ValueError:
            print("\nOps! Digite apenas números inteiros para a idade. Vamos tentar novamente.\n")
            continue

        if idade < 0:
            print("\nA idade não pode ser negativa. Tente novamente.\n")
            continue

        return idade


def montar_mensagem_boas_vindas(nome: str, idade: int, hobby: Optional[str]) -> str:
    """Cria o texto final exibido no console a partir dos dados coletados."""

    hobby_texto = ""
    if hobby:
        hobby_texto = f" É ótimo saber que você gosta de {hobby.lower()}!"

    return (
        f"Olá, {nome}! Bem-vindo(a) ao Syntax Sanctuary.\n"
        f"É incrível saber que você tem {idade} anos e está aprendendo programação!"
        f"{hobby_texto}\n"
    )


def main() -> None:
    """Executa o fluxo completo de perguntas e apresenta o resumo final."""

    print("=== Demonstração: entrada e saída em Python ===\n")

    nome = solicitar_texto("Qual é o seu nome? ")
    idade = solicitar_idade()
    hobby = solicitar_texto("Qual é o seu hobby favorito? (Opcional) ", permitir_vazio=True)

    mensagem = montar_mensagem_boas_vindas(nome, idade, hobby)
    print()
    print(mensagem)
    print("Obrigado por praticar! Experimente alterar as perguntas e respostas para treinar.")


if __name__ == "__main__":
    main()
