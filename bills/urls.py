from django.conf.urls import url
from bills import views

urlpatterns = [
    url(r'^generateBill$', views.createBill),
    url(r'^allBills/$', views.getAllBills),
]