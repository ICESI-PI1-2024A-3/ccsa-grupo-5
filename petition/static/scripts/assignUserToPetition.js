document.addEventListener('DOMContentLoaded', function() {
    var assignButton = document.getElementById('assign-button');
    var form = document.getElementById('assign-gestor-form');

    assignButton.addEventListener('click', function(event) {
        var selectedUser = document.getElementById('user').value;

        if (!selectedUser) {
            event.preventDefault(); // Detener el envío del formulario

            // Mostrar mensaje de error
            alert('Debes seleccionar un gestor');
        }
    });
});