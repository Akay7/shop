from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ProductsListView.as_view()),

    url(r'^order_operation/$', views.OrderOperation.as_view(), name="order-operation"),
    url(r'^add_to_cart/$', views.ProductToCart.as_view(), name="add-to-cart"),

    url(r'^(?P<pk>\d+)/', views.ProductDetailView.as_view(), name="product-detail"),
    url(r'^(?P<slug>[-\w]+)/', views.TagListView.as_view()),

]