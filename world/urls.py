from django.urls import path
from . import views

urlpatterns=[
	path('', views.index,name='index'),
	path('sign_up',views.next,name='sign_up'),
	path('login',views.login,name='login'),
	path('form',views.form,name='form'),
]


