document.getElementById("toggleObservationsBtn").addEventListener("click", function() {
    var observationsContainer = document.getElementById("observationsContainer");
    var toggleObservationsBtn = document.getElementById('toggleObservationsBtn');
    if (observationsContainer.style.display === "none") {
        observationsContainer.style.display = "block";
        toggleObservationsBtn.textContent = 'Ocultar Observaciones';
    } else {
        observationsContainer.style.display = "none";
        toggleObservationsBtn.textContent = 'Mostrar Observaciones';
    }
});