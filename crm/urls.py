from django.conf.urls import url
from crm import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
]