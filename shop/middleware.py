from .models import Product


class CartMiddleware:
    def process_template_response(self, request, response):
        '''
        if "cart" not in request.session:
            request.session["cart"] = {}
        response.context_data['cart'] = request.session["cart"]
        #print(response.context_data)
        '''
        # TODO: return response with correct data
        return response
