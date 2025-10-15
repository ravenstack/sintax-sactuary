import java.util.Locale;
import java.util.Scanner;

/**
 * Conversor simples de temperaturas.
 * 
 * Demonstra leitura de dados, condicionais e formatação de saída.
 */
public class ConversorTemperatura {

    private static double celsiusParaFahrenheit(double celsius) {
        return (celsius * 9 / 5) + 32;
    }

    private static double fahrenheitParaCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Conversor de Temperaturas ===");
        System.out.print("Converter para (C)elsius ou (F)ahrenheit? ");
        String escala = scanner.next().trim().toLowerCase();

        System.out.print("Digite o valor a ser convertido: ");
        double valor = scanner.nextDouble();

        if (escala.equals("c")) {
            double resultado = fahrenheitParaCelsius(valor);
            System.out.printf("%.1f°F equivalem a %.1f°C%n", valor, resultado);
        } else if (escala.equals("f")) {
            double resultado = celsiusParaFahrenheit(valor);
            System.out.printf("%.1f°C equivalem a %.1f°F%n", valor, resultado);
        } else {
            System.out.println("Opção inválida. Utilize 'C' ou 'F'.");
        }

        scanner.close();
    }
}
