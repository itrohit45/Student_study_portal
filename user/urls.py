from django.urls import path
from . import views

urlpatterns = [
    path('',views.Login.as_view(),name='login'),
    path('logout',views.logout_user,name='logout'),
    path('signup',views.sign_up,name='signup'),

]