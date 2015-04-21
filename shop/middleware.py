from .models import Order


class CartMiddleware:
    def process_template_response(self, request, response):
        if "order_id" in request.session:
            order_id = request.session["order_id"]
            response.context_data["order"] = Order.objects.get(id=order_id)

        return response
