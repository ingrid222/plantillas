/*const personaje= document.getElementById("personaje");
const animacion_personaje= document.getElementById("animacion_personaje");

let x = 0; // posición inicial en el eje X
let y = 0; // posición inicial en el eje Y
let xSpeed = 5; // velocidad horizontal
let ySpeed = 5; // velocidad vertical

function updatePosition() {
    x += xSpeed;
    y += ySpeed;

    if (x + personaje.clientWidth >= animacion_personaje || x <= 0) {
        xSpeed = -xSpeed; // Cambia la dirección en el eje X
    }

    if (y + personaje.clientHeight >= animacion_personaje || y <= 0) {
        ySpeed = -ySpeed; // Cambia la dirección en el eje Y
    }

     // Aplica las nuevas posiciones
    personaje.style.left = x + "px";
    personaje.style.top = y + "px";

}

function animate() {
    updatePosition();
    requestAnimationFrame(animate);
}

animate();*/
