from django.conf.urls import url, include
from student import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='stu_index'),
]
