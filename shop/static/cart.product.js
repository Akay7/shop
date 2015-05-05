var add = function(product_id, callback){
    $.post(
        "/order_operation/",
        { "product_id": product_id, "operation": "add" },
        function(data) {
            callback(null, data);
        }
    ).fail(function () {
        console.log("fail");
    });
}

