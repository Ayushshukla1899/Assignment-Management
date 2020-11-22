from django.urls import path

from . import views 
urlpatterns =[

    path('',views.home,name='home'),
    path('portal', views.portal, name='portal'),
    path('login', views.login, name='login' ),
    path('dashboard',views.dashboard, name='dashboard'),
    path('signup',views.signup, name='signup'),
    path('class_students',views.class_students, name='class_students'),
]