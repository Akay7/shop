from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ProductsListView.as_view()),
    url(r'^(?P<pk>\d+)/', views.ProductDetailView.as_view()),
    url(r'^(?P<slug>[-\w]+)/', views.TagListView.as_view()),
]