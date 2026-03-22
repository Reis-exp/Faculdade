abstract class OperacaoMatematica {
    public abstract double calcular(double a, double b) throws DivisaoPorZeroException;

   public void exibirResultado(double resultado){
    System.out.println("O resultado da conta é: " + resultado);
    }
}
