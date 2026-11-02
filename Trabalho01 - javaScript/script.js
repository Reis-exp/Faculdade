let inputNumero = document.getElementById("numero")
let inputGerar = document.getElementById("gerar")
let conteudoTabuada = document.getElementById("conteudo-tabuada")
let inputLimpar = document.getElementById("limpar")

inputGerar.addEventListener("click", function(){
    const valor = Number(inputNumero.value);

    if (inputNumero.value.trim()=== "" || valor < 1 || valor > 10){
        alert("Por favor, insira um número entre 1 a 10");
        return;
    }

    
    conteudoTabuada.innerHTML = "";
    for (let i = 1; i<=10; i++){
        const resultado = valor * i;
    
        const linha = document.createElement("p");
        linha.textContent = `${valor} x ${i} = ${resultado}`;
        
        conteudoTabuada.appendChild(linha);
    
    
    }
});
 inputLimpar.addEventListener("click", function(){
    conteudoTabuada.innerHTML = "";
    inputNumero.value = "";
});

