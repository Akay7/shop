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

