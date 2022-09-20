from django.urls import path
from . import views

urlpatterns={
  # Registration urls
  path('',views.index,name='index'),
  path('login/',views.LoginView.as_view,name='login'),
  path('logout/',views.LogoutView.as_view,name='logout')

}
