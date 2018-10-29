$(document).ready(function() {
    var table = $('#serverlist').DataTable( {
        stateSave: true,
        "deferRender": true,
        "ajax": "/servers",
        "columns": [
            { "data": "v" },    // version
            { "data": "l" },    // country
            { "data": "n" },    // name
            { "data": "p" },    // player count
            { "data": "t" },    // hours
            { "data": "h" },    // hive
            { "data": "m" },    // mode
            { "data": "a" },    // player count for table sorting
            { "data": "b" },    // day or night for sorting by time
            { "data": "c" },    // minutes
            { "data": "s" }
        ],
        "order": [[ 3, "desc" ]],
        "lengthMenu": [ [25, 50, 100, -1], [25, 50, 100, "All"] ],
        "columnDefs": [
        {
            "render": function (data, type, row) {
                switch (data) {
                    case '2':
                        return '<span class="badge badge-pill badge-secondary">0.62</span>';
                    case '3':
                        return '<span class="badge badge-pill badge-info">0.63</span>';
                }
            }, "targets": [0]
        },
        {
            "render": function (data, type, row) {
                var p = parseInt(row.a, 10);
                var m = parseInt(data, 10);
                var r = Math.min(p, m) + '<small class="text-muted mr-1">/' + m + '</small>';
                if (p > m) {
                    r += '<span title="' + (p - m) + ' in queue" class="badge badge-warning">' + (p - m) + ' <i class="fas fa-hourglass-half"></i></span>';
                }
                return r;
            }, "targets": [3]
        },
        {
            "render": function (data, type, row) {
                var h = parseInt(row.t, 10);
                var l = 'dark';
                var i = 'moon';
                if (h >= 5 && h < 19) {
                    l = 'light';
                    i = 'sun';
                }
                return '<span title="Speed: ' + row.s + 'x" class="badge badge-' + l + '">' + row.t + ':' + row.c + ' <i class="fas fa-' + i + '"></i></span>';
            }, "targets": [4]
        },
        {
            "render": function (data, type, row) {
                switch (data) {
                    case 'p':
                        return '<span class="badge badge-danger">Public</span>';
                    case 'c':
                        return '<span class="badge badge-success">Private</span>';
                    case 't':
                        return '<span class="badge badge-danger">3PP</span>';
                    case 'f':
                        return '<span class="badge badge-success">1PP</span>';
                }
            }, "targets": [5, 6]
        },
        {
            "render": function (data, type, row) {
                 return '<span title="' + data + '" class="flag-icon flag-icon-' + data + '"></span>';
            }, "targets": [1]
        },
        { "visible": false, "targets": [7, 8, 9, 10] },
        { "orderData": 7, "targets": 3 },
        { "orderData": 8, "targets": 4 },
        { "className": "text-center", "targets": [4,5,6] },
        { "orderable": false, "targets": [0, 1, 5, 6] }
        ]
    });

    hint = setInterval(hi, 15000 );

    function hi() {
        table.ajax.reload(null, false);
    }
    function stopHi() {
        clearInterval(hint);
    }

});
