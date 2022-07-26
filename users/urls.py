from django.urls import path
from users import views

urlpatterns=[
    path('accounts/signup',views.SingupView.as_view(),name='sign-up'),
    path('accounts/signin',views.SinginView.as_view(),name='sign-in')
]