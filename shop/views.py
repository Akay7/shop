from django.views import generic
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, Http404

from .models import Product, Tag, Order


class OrderOperation(generic.View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        order_id = request.session.get("order_id", None)

        if order_id is None:
            order = Order.objects.create()
            request.session["order_id"] = order.id
        else:
            order = Order.objects.get(id=order_id)

        operation = request.POST.get("operation")
        if operation == "add":
            return JsonResponse(order.add_one(product_id))
        elif operation == "del":
            order.del_one(product_id)
        elif operation == "set":
            qty = request.POST.get("qty")
            order.set_qty(product_id, qty)

        # todo: Return added object in JSON or
        # Correct/Not correct response for deleting object
        return JsonResponse({'correct': "true"})

    def get(self, request):
        raise Http404


class ProductsListView(generic.ListView):
    model = Product
    template_name = 'shop/products_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'shop/product_detail.html'


class TagListView(generic.DetailView):
    model = Tag
    template_name = 'shop/tag_products_list.html'


class OrderDetailView(generic.TemplateView):
    template_name = 'shop/order_detail.html'
