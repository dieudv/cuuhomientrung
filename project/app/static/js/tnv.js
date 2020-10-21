var dataTable = $('#tbl-tnv').DataTable({
    destroy: true,
    data: new Array(),
    columns: [
        {
            title: "Tên"
        },
        {
            title: "Số điện thoại"
        },
    ],
    "language": {
        "search": "Tìm Kiếm",
        "paginate": {
            "first": "Về Đầu",
            "last": "Về Cuối",
            "next": "Tiến",
            "previous": "Lùi"
        },
        "order": [
            [0, "desc"]
        ],
        "info": "Hiển thị _START_ đến _END_ của _TOTAL_ mục",
        "infoEmpty": "Hiển thị 0 đến 0 của 0 mục",
        "lengthMenu": "Hiển thị _MENU_ mục",
        "loadingRecords": "Đang tải...",
        "emptyTable": "Không có gì để hiển thị",
    }
});

fetch("/api/app/tinhnguyenvien/?format=json&type=json", {
    method: "GET"
}).then(response => response.text()).then((res) => {
    let json_data = JSON.parse(res);
    json_data.forEach(obj => {
        if (obj.status === 1 && obj.phone.length >= 10) {
            row = [
                obj.name,
                '<a href="tel:' + obj.phone + '">' + obj.phone + '</a>',
            ];
            dataTable.row.add(row).draw(false);
        }
    });
}).catch((error) => {
    console.log(error);
});
