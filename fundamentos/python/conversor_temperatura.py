"""Conversor simples de temperaturas.

Mostra o uso de entrada de dados, funções e formatação de strings.
"""

from __future__ import annotations


def celsius_para_fahrenheit(celsius: float) -> float:
    """Converte graus Celsius em Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    """Converte graus Fahrenheit em Celsius."""
    return (fahrenheit - 32) * 5 / 9


def executar_conversao() -> None:
    print("=== Conversor de Temperaturas ===")
    escala = input("Converter para (C)elsius ou (F)ahrenheit? ").strip().lower()
    valor = float(input("Digite o valor a ser convertido: "))

    if escala == "c":
        resultado = fahrenheit_para_celsius(valor)
        print(f"{valor:.1f}°F equivalem a {resultado:.1f}°C")
    elif escala == "f":
        resultado = celsius_para_fahrenheit(valor)
        print(f"{valor:.1f}°C equivalem a {resultado:.1f}°F")
    else:
        print("Opção inválida. Utilize 'C' ou 'F'.")


if __name__ == "__main__":
    executar_conversao()
