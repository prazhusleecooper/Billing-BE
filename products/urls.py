from django.conf.urls import url
from products import views

urlpatterns = [
    url(r'^createProduct/$', views.createProduct),
    url(r'^allProducts/$', views.getAllProducts)
]