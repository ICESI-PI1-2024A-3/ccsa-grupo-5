document.addEventListener("DOMContentLoaded", function() {
    // Obtén el nombre de la página actual
    var currentPage = window.location.pathname.split("/").pop();

    // Asigna la clase 'active' al elemento de navegación correspondiente
    var navElement = document.getElementById("nav-" + currentPage);
    if (navElement) {
        navElement.classList.add("active");
    }
});