function confirmDelete(id) {
    var confirmation = confirm("¿Estás seguro de que quieres eliminar este elemento?");
    if (confirmation) {
        document.getElementById('deleteForm' + id).submit();
    }
}