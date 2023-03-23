from django.urls import path
from . import views
from authentication.views import LoginView

urlpatterns={
  # Registration urls
  path('',views.index,name='index'),
  path('/registration', views.UserCreate.as_view(), name="index"),
  path('/login', LoginView.as_view(), name="login"),
  # path('login/',views.LoginView.as_view,name='login'),
  # path('logout/',views.LogoutView.as_view,name='logout')

}
