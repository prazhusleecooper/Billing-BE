from django.conf.urls import url
from customers import views

urlpatterns = [
    url(r'^createCustomer/$', views.createCustomer),
    url(r'^allCustomers/$', views.getAllCustomers)
]