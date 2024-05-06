document.addEventListener("DOMContentLoaded", function () {
  const btnAbrirModal = document.querySelector("#notification-btn");
  const btnCerrarModal = document.querySelector("#btn-cerrar-modal");
  const modal = document.querySelector("#modal");

  btnAbrirModal.addEventListener("click", () => { modal.showModal(); });
  btnCerrarModal.addEventListener("click", () => { modal.close(); });

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
