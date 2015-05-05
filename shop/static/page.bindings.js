$('.add_to_cart').click( function() {
    var product_id = $(this).attr("product_id");
    add(product_id);
});
