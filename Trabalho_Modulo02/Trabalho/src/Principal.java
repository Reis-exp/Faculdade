import java.util.ArrayList;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Produto2> produtos = new ArrayList<>();

        produtos.add(new Produto2("Tênis nike Jordan", 2500.00));
        produtos.add(new Produto2("Moletom Nike Jordan", 550.00));

        int opcao;
        do {
            System.out.println("\n===============================");
            System.out.println("Loja Nike");
            System.out.println("===============================");
            System.out.println("1. Ver produtos");
            System.out.println("2. Adicionar Produto");
            System.out.println("3. Finalizar Compra");
            System.out.print("Escolha uma opção: ");

            opcao = sc.nextInt();
            sc.nextLine();

            switch (opcao) {
                case 1:
                    System.out.println("\nProdutos Disponíveis:");
                    System.out.println("------------------------------");
                    for (Produto2 p : produtos) {
                        p.exibirDados();
                    }
                    System.out.println("Pressione ENTER para voltar ao menu...");
                    sc.nextLine();
                    break;

                case 2:
                    System.out.print("Digite o nome do produto: ");
                    String nome = sc.nextLine();
                    System.out.print("Digite o preço do produto: ");
                    double preco = sc.nextDouble();
                    sc.nextLine();
                    produtos.add(new Produto2(nome, preco));
                    System.out.println("Produto cadastrado com sucesso!");
                    System.out.println("Pressione ENTER para voltar ao menu...");
                    sc.nextLine();
                    break;

                case 3:
                    double total = 0;
                    System.out.println("\nResumo da compra:");
                    System.out.println("------------------------------");
                    for (Produto2 p : produtos) {
                        p.exibirDados();
                        total += p.getPreco();
                    }
                    System.out.println("\nTotal de produtos: " + Produto2.getQuantidadeTotal());
                    System.out.printf("Valor total da compra: R$ %.2f\n", total);
                    System.out.println("Obrigado por comprar conosco!");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        } while (opcao != 3);

        sc.close();
    }
}
