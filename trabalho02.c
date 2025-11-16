#include <stdio.h>
int main(){
    int num;
    int soma = 0;
    // agora que declaramos as variaveis, iremos iniciar o loop

    printf("Digite numeros inteiros (ou 0 para sair do programa):\n");
    while (1){
        printf("Digite um numero: ");
        scanf("%d", &num);
    
        if (num == 0){
            printf("Aguarde, irei calcular a soma dos valores digitados....\n");
            break; // vamos colocar o break para sair do loop caso o usuario digite 0
        }
        soma += num;
    }
    printf("A soma dos numeros digitados e: %d\n", soma);
     return 0;
}