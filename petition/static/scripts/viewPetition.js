let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] },
        { orderable: false, targets: [11] },
        { searchable: false, targets: [11] }
    ],
    pageLength: 10,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    dataTable = $("#dataTablePetition").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};


window.addEventListener("load", async () => {
    await initDataTable();
});