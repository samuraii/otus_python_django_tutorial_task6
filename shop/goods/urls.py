from django.conf.urls import url
from django.urls import path
from goods import views

urlpatterns = [
    url('^$', views.goods),
    path('good/<int:good_id>', views.good)
]
