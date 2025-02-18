function resultado_signo() {
    let formData = new FormData(document.getElementById("zodiaco"));
    
    fetch("/zodiacoChino", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("resultado").innerHTML = `
            <h3>Hola <i>${data.nombre} ${data.apaterno} ${data.amaterno}</i></h3>
            <p>Tienes <strong>${data.edad}</strong> años</p>
            <p>Tu signo zodiacal chino es <strong>${data.signo_chino}</strong></p>
            <img src="${data.imagen}" width="80" alt="${data.signo_chino}">
        `;
    });
}