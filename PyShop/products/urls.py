from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new', views.new),
    # path('usernumbertest/', views.usernumbertest, name='form_submit'),
    path('usernumbertest', views.user_number_test)
]