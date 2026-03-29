public class Livro {
    String titulo;
    String autor;
    int anoPublicacao;
    String Classificacao;

    public Livro(String titulo, String autor, int anoPublicacao, String Classificacao){
    this.autor = autor;
    this.titulo = titulo;
    this.anoPublicacao = anoPublicacao;
    this.Classificacao = Classificacao;
    }

    public void exibirInformacoes(){
        System.out.println("Titúlo: " +titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Ano de Publicação: " + anoPublicacao);
        System.out.println("Classificação: " + Classificacao);
        System.out.println("________________________________");
    }
}

