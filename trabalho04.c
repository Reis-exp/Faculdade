#include <stdio.h>

// antes de entrar no main, iremos definir algumas funções para calcular os valores

float calcular_salario_bruto(float valor_Hora,float horas_Trabalhadas) // essa variavel iremos usar para descobrir o bruto do salario
{
    return valor_Hora * horas_Trabalhadas;
}
float calcular_Desconto (float salario_bruto) // essa variavel iremos usar para descobrir o desconto sobre o salario
{
    return salario_bruto * 0.09;
}
float calcular_salario_liquido(float salario_bruto, float desconto) // essa vai calcular o salario que o funcionaria vai receber
{
    return salario_bruto - desconto;
}

int main (){
    float valor_Hora, horas_Trabalhadas ;
    float salario_bruto, desconto, salario_liquido;
// com as variaveis declaradas, vamos pedir as informações ao usuario
    printf("Digite o valor da hora trabalhada:");
    scanf("%f", &valor_Hora);

    printf("Digite o total de horas que foram trabalhadas no mes:");
    scanf("%f", &horas_Trabalhadas);

    // agora que temos os valores, iremos calcular o salario bruto, desconto e salario liquido
    salario_bruto = calcular_salario_bruto(valor_Hora, horas_Trabalhadas);
    desconto = calcular_Desconto(salario_bruto);
    salario_liquido = calcular_salario_liquido(salario_bruto,desconto);


    //agora vamos mostrar ao usuario os valores calculados
    printf(" O salario bruto e: R$ %2.f\n", salario_bruto);
    printf(" O valor descontado pelo INSS e: R$ %2.f\n", desconto);
    printf("O salario liquido e: R$ %2.f\n", salario_liquido);

    return 0;
}
