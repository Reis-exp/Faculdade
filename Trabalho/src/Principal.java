public class Principal {
    public static void main(String[] args) {
        Livro[] livros = new Livro[5];

        livros[0] = new Livro ("Java: Como Programar", "Paul. J Deitel", 1996, "Programação/Didatico");
        livros[1] = new Livro ("Código limpo", "Robert C. Martin",2008, "Programação/Didatico" );
        livros[2] = new Livro ("Use a Cabeça! Java", "Kathy Sierra e Bert Bates", 2003, "Programação/Didatico");
        livros[3] = new Livro ("O programador Pragmático", "Andrew Hunt e David Thomas", 2010, "Programação/Didatico"); // versão em português
        livros[4] = new Livro ("Desbravando Java e Orientação a Objetos", "Rodrigo Turini", 2014, "Programação/Didatico");

        String PalavraChave = "Java";

        System.out.println("Bem vindo ao mundo dos Livros De Programação!!\n");
        System.out.println("Livros que contêm a palavra " + PalavraChave + " no Título!\n");

        for( int i = 0; i < livros.length; i ++){
            if (livros[i].titulo.contains(PalavraChave)){
                livros[i].exibirInformacoes();
            }
        }
    }
}
