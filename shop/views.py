from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse

from .models import Product, Tag, Order, PositionInOrder


class OrderOperation(generic.View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        order = request.session.get("order", Order.objects.create())

        operation = request.POST.get("operation")
        if operation == "add":
            order.add_one(product_id)


class ProductToCart(generic.View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        cart = request.session.get("cart", {})

        items = cart.get(product_id, 0) + 1
        cart[product_id] = items

        request.session["cart"] = cart
        #print(request.session["cart"])

        return JsonResponse({'boom': "true"})


class ProductsListView(generic.ListView):
    model = Product
    template_name = 'shop/products_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'shop/product_detail.html'


class TagListView(generic.DetailView):
    model = Tag
    template_name = 'shop/tag_products_list.html'