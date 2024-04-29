let dataTable;
let dataTableIsInitialized = false;


let dataTableOptions = {
    language: {
        "lengthMenu": "Mostrar _MENU_ registros",
        "zeroRecords": "No se encontraron resultados",
        "info": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "infoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
        "infoFiltered": "(filtrado de un total de _MAX_ registros)",
        "sSearch": "Buscar:",
        "oPaginate": {
            "sFirst": "Primero",
            "sLast": "Último",
            "sNext": "Siguiente",
            "sPrevious": "Anterior"
        },
        "sProcessing": "Procesando...",
    },
    responsive: 'true',
    dom: 'Bfrtilp',
    buttons: [
        {
            extend: 'excelHtml5',
            text: '<i class="fas fa-file-excel"></i> ',
            titleAttr: 'Exportar a Excel',
            className: 'btn btn-success'
        },

    ],
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
        { orderable: false, targets: [10] },
        { searchable: false, targets: [10] }
    ],
    pageLength: 10,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        console.log("Destroying DataTable:", dataTable);
        dataTable.destroy();
    }

    console.log("Initializing DataTable...");
    dataTable = $("#dataTablePetition").DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};


window.addEventListener("load", async () => {
    await initDataTable();
});