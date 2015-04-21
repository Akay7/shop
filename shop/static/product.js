var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function () {
$('.add_to_cart').click( function() {
    var product_id = $(this).attr("product_id");
    console.log("Click" + product_id);
    $.post(
    "/order_operation/",
    { product_id: product_id, operation: "add" }
    ).done( function () {
        console.log("done");
    }).fail( function () {
        console.log("fail");
    });
});
});

