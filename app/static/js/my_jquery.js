$(".export_excel").click(function() {

    let url = window.location.search;

    let for_download = {
        'Test': {
            'first': 'first'
        },
        'Test2': {
            'second': 'second'
        }
    };

    $.ajax({
        type: "POST",
        url: "/create_excel/" + url,
        data: JSON.stringify(for_download),
        contentType: "application/json; charset=utf-8",
        async: false
    }).done((response) => {
        var param = "/create_excel?";
        param += "way=" + response;
        console.log(param)
        $("a[id='export']").attr('href', param);
    });
});