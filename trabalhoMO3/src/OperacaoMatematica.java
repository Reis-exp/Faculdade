abstract class OperacaoMatematica {
    public abstract double calcular(double a, double b) throws DivisaoPorZeroException;

    public void exibirResultado(double resultado){
        if (resultado != 0)
        System.out.println("O resultado da conta é:" + resultado);
    }
}
