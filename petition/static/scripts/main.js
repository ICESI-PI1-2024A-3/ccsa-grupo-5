document.addEventListener("DOMContentLoaded", function () {
  setNavbarContainerHeight();

  var links = document.querySelectorAll(".nav-link");

  links.forEach(function (link) {
    link.addEventListener("click", function () {
      links.forEach(function (otherLink) {
        otherLink.classList.remove("active");
      });
      this.classList.add("active");
    });
  });
});

function setNavbarContainerHeight() {
  var bodyHeight = document.body.scrollHeight; // Altura total del contenido de la página
  var navbarContainer = document.querySelector('.navbarContainer');
  navbarContainer.style.height = bodyHeight + 'px'; // Establece la altura del contenedor navbarContainer igual a la altura total del contenido de la página
}

// Llama a la función setNavbarContainerHeight() cuando el DOM esté completamente cargado y también cuando se cambie el tamaño de la ventana
window.addEventListener('resize', setNavbarContainerHeight);

document.querySelector(".bars__menu").addEventListener("click", function () {
  animateBars();
  toggleNavbar();
});

var line1__bars = document.querySelector(".line1__bars-menu");
var line2__bars = document.querySelector(".line2__bars-menu");
var line3__bars = document.querySelector(".line3__bars-menu");

function animateBars() {
  line1__bars.classList.toggle("activeline1__bars-menu");
  line2__bars.classList.toggle("activeline2__bars-menu");
  line3__bars.classList.toggle("activeline3__bars-menu");
}

function toggleNavbar() {
  var navbarContainer = document.getElementById("navbarContainer");
  navbarContainer.classList.toggle("active");

  var topSection = document.querySelector(".logo");
  topSection.classList.toggle("move-right");

  // Eliminar el margen izquierdo cuando se agrega la clase .move-right
  if (topSection.classList.contains("move-right")) {
    topSection.style.marginLeft = "0";
    topSection.style.display = "none";
  } else {
    // Restablecer el margen izquierdo a su valor original cuando se elimina la clase .move-right
    topSection.style.marginLeft = "50px"; // Puedes ajustar el valor según sea necesario
    topSection.style.display = "block";
  }

  var leftContent = document.querySelector(".left-content");
  leftContent.classList.toggle("move-right");
}

