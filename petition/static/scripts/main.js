document.addEventListener("DOMContentLoaded", function () {
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

  var leftContent = document.querySelector(".left-content");
  leftContent.classList.toggle("move-right");
}
