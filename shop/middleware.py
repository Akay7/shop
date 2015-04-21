from .models import Order


class CartMiddleware:
    def process_template_response(self, request, response):
        '''
        if "cart" not in request.session:
            request.session["cart"] = {}
        response.context_data['cart'] = request.session["cart"]
        #print(response.context_data)
        '''

        if "order_id" in request.session:
            order_id = request.session["order_id"]
            response.context_data["order"] = Order.objects.get(id=order_id)

        # TODO: return response with correct data
        return response
