from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse

from .models import Product, Tag


# Create your views here.
class AjaxableResponseMixin(object):
    """
    Must using with FormView(CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class ProductToCart(generic.View):
    def get(self, request):
        print("get")
        return JsonResponse({"get":True})

    def post(self, request):
        print("post")
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