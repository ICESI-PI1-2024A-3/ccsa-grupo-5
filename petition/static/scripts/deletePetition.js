function confirmDelete(petitionId) {
    var confirmation = confirm("¿Estás seguro de que quieres eliminar esta solicitud?");
    if (confirmation) {
        document.getElementById('deleteForm' + petitionId).submit();
    }
}