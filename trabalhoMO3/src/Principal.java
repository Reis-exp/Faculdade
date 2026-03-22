import java.util.Scanner;

public class Principal {

    public static void main(String[] args) throws DivisaoPorZeroException {

        Scanner sc = new Scanner(System.in);

        OperacaoMatematica soma = new Soma();
        OperacaoMatematica divisao = new Divisao();

        System.out.println("Bem vindo!!");
        System.out.println("Vamos realizar a operação de soma.");

        System.out.print("Digite o primeiro número: ");
        double a = sc.nextDouble();

        System.out.print("Digite o segundo número: ");
        double b = sc.nextDouble();

        // Soma
        double resultadoSoma = soma.calcular(a, b);
        soma.exibirResultado(resultadoSoma);

        Scanner sc1 = new Scanner(System.in);
        System.out.println("Agora vamos realizar a operação de Divisão.");

        System.out.print("Digite o primeiro número: ");
        double a1 = sc1.nextDouble();

        System.out.print("Digite o segundo número: ");
        double b2 = sc1.nextDouble();

        // Divisão com tratamento
        try {
            double resultadoDivisao = divisao.calcular(a1, b2);
            divisao.exibirResultado(resultadoDivisao);
        } catch (DivisaoPorZeroException e) {
            System.out.println(e.getMessage());
        }

        sc.close();
    }
}