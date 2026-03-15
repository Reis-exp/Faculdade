public class Produto2 {

    private String nome;
    private double preco;
    private static int quantidadeTotal = 0;

    public Produto2() {
        this.nome = "Produto sem nome";
        this.preco = 0.0;
        quantidadeTotal++;
    }

    public Produto2(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
        quantidadeTotal++;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public static int getQuantidadeTotal() {
        return quantidadeTotal;
    }

    public void exibirDados() {
        System.out.printf("Nome: %s - Preço: R$ %.2f\n", nome, preco);
    }
}


