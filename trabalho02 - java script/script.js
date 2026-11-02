// este arquivo será o mesmo do trabalho do primeiro modulo, porém com as alterações para o segundo modulo.

let canvas = document.getElementById("efeitos");
let ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let inputNumero = document.getElementById("numero")
let inputGerar = document.getElementById("gerar")
let conteudoTabuada = document.getElementById("conteudo-tabuada")
let inputLimpar = document.getElementById("limpar")

inputGerar.addEventListener("click", function(){

    const valor = Number(inputNumero.value);

    if (inputNumero.value.trim() === "" || valor < 1 || valor > 10) {
        alert("Por favor, insira um número entre 1 a 10");
        return;
    }

    const posicao = inputGerar.getBoundingClientRect();
    const centroX = posicao.left + posicao.width / 2;
    const centroY = posicao.top + posicao.height / 2;

    for (let i = 0; i < 20; i++) {
        criarParticula(centroX, centroY);
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

    const posicao = inputLimpar.getBoundingClientRect();

    const centroX = posicao.left + posicao.width / 2;
    const centroY = posicao.top + posicao.height / 2;

    for (let i = 0; i < 15; i++) {
    criarParticula(centroX, centroY, "xis");
}
});

let particulas = [];

function animar() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particulas.forEach((particula) => {

        particula.velocidadeY += particula.gravidade;

        particula.x += particula.velocidadeX;
        particula.y += particula.velocidadeY;
        particula.opacidade -= 0.004;

        if (particula.y + particula.tamanho >= canvas.height) {
            particula.y = canvas.height - particula.tamanho;
            particula.velocidadeY *= -0.7;
        }

        if (particula.tipo === "circulo") {
            ctx.font = `${particula.tamanho * 4}px Arial`;
            ctx.fillStyle = particula.cor;
            ctx.fillText("✔", particula.x, particula.y);
        } 
        else if (particula.tipo === "xis") {
            ctx.font = `${particula.tamanho * 4}px Arial`;
            ctx.fillStyle = particula.cor;
            ctx.fillText("×", particula.x, particula.y);
        }

    });
    particulas = particulas.filter(particula => particula.opacidade > 0);
    requestAnimationFrame(animar);
}

animar();

function criarParticula(x,y, tipo = "circulo"){
    let particula = {
        x: x,
        y: y,
        tipo: tipo,
        velocidadeX: (Math.random() -0.5) *6,
        velocidadeY: -Math.random() * 8,
        gravidade: 0.05,
        opacidade: 1,
        cor: tipo === "xis" ? "#ff0303" : "#00ff55",       
        tamanho: Math.random() * 4 + 2
    };
    particulas.push(particula);
}
