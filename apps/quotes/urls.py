from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^add_quote$',views.add_quote),
    url(r'^show_posts$',views.show_your_posts),
    url(r'^like$',views.like)
]