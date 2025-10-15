#include <iomanip>
#include <iostream>
#include <string>

// Conversor simples de temperaturas.
// Demonstra leitura de dados, condicionais e formatação de saída.

namespace {

double CelsiusParaFahrenheit(double celsius) {
    return (celsius * 9.0 / 5.0) + 32.0;
}

double FahrenheitParaCelsius(double fahrenheit) {
    return (fahrenheit - 32.0) * 5.0 / 9.0;
}

}  // namespace

int main() {
    std::cout << "=== Conversor de Temperaturas ===\n";
    std::cout << "Converter para (C)elsius ou (F)ahrenheit? ";
    std::string escala;
    std::getline(std::cin, escala);

    std::cout << "Digite o valor a ser convertido: ";
    double valor = 0.0;
    std::cin >> valor;

    std::cout << std::fixed << std::setprecision(1);

    if (escala == "c" || escala == "C") {
        double resultado = FahrenheitParaCelsius(valor);
        std::cout << valor << "°F equivalem a " << resultado << "°C\n";
    } else if (escala == "f" || escala == "F") {
        double resultado = CelsiusParaFahrenheit(valor);
        std::cout << valor << "°C equivalem a " << resultado << "°F\n";
    } else {
        std::cout << "Opção inválida. Utilize 'C' ou 'F'.\n";
    }

    return 0;
}
