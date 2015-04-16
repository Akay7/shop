from .models import Product


class CartMiddleware:
    def process_template_response(self, request, response):
        if not request.is_ajax():

            response.context_data['cart'] = request.session["cart"]
            print(response.context_data)
            return response
        else:
            print('ajax')
