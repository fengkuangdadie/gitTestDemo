from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^hello/', views.HelloView.as_view(msg="Haha")),
    url(r'^template/', views.HelloTemplate.as_view(template_name='Hello.html')),
]