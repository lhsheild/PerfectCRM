from django.conf.urls import url
from crm import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='sales_index'),
    url(r'^customer/$', views.CustomerList.as_view(), name='customer_list'),
]