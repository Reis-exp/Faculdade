public class Divisao extends OperacaoMatematica {

    @Override
    public double calcular(double a, double b) throws DivisaoPorZeroException {
        try {
            if (b == 0) {
                throw new DivisaoPorZeroException("Erro: divisão por zero não é permitida.");
            }
            return a / b;
        } catch (DivisaoPorZeroException e) {
            System.out.println(e.getMessage());
            return 0;
        }
    }
}