function calculate() {
    const expression = document.getElementById("expression").value;
    const result = eval(expression);
    document.getElementById("result").textContent = result;
  }


function clearResult() {
    document.getElementById("result").textContent = "";
}




function submit(){
    const expression = document.getElementById("frase");
    expression.addEventListener("input",exibirFrase);
}

function atualizarFrase() {

    const frase = document.getElementById('fraseInput').value;
  

    const fraseOutput = document.getElementById('fraseOutput');
    fraseOutput.textContent = frase;
  

    const legenda = document.querySelector('.legenda');
    legenda.classList.add('show');
  }

  function apagarTexto(){
    document.getElementById("fraseOutput").textContent = "";
  }


  function introduzNome() {

    const nome = document.getElementById('nomeInput').value;
    const nome2 = document.getElementById('nomeInput').value;
    const nome3 = document.getElementById('nomeInput').value;

    const nomeOutput = document.getElementById('nomeOutput');
    nomeOutput.textContent = nome;

    const nomeOutput2 = document.getElementById('nomeOutput2');
    nomeOutput2.textContent = nome2;

    const nomeOutput3 = document.getElementById('nomeOutput3');
    nomeOutput3.textContent = nome3;

  }

  function apagarNome(){
    document.getElementById("nomeOutput").textContent = "";
  }
  
  function inserirData() {
    const data = new Date();

    const meses = [
      "janeiro", "fevereiro", "março", "abril", "maio", "junho",
      "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ];
    const mesAtual = meses[data.getMonth()];

    const dataFormatada = `${data.getDate()} de ${mesAtual}, ${data.getFullYear()}`;
    
    const elemento = document.getElementById("data-atual");
    elemento.innerHTML = dataFormatada;
  }
  
  window.onload = inserirData;

  