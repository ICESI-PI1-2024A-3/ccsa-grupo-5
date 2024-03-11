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