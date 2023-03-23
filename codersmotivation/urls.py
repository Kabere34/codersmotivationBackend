from django.urls import path
from . import views
from authentication.views import LoginView



urlpatterns = [
    path('', views.index, name="index"),
    path('api/post/',views.Postapi.as_view())
]


