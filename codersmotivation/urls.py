from django.urls import path
from . import views
from authentication.views import LoginView



urlpatterns = [
    path('', views.index, name="index"),
    path('api/post/',views.Postapi.as_view())
    path('comments/', views.CommentAPIView.as_view(), name='comment_api'),
    path('comments/<int:pk>', views.CommentAPIView.as_view(), name='comment_api_get'),
    path('posts/<int:pk>/like/', LikeView.as_view()),
    path('posts/<int:pk>/unlike/', UnlikeView.as_view()),
]


