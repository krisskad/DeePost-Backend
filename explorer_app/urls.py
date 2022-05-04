from django.urls import path, include
from . import views

urlpatterns = [
    path('get_imgur/<int:page>/', views.ImagesView.as_view(), name="imgur"),
    # path('get_imgur/<int:pk>/', views.GetViewSet, name="imgur"),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('post/', views.PostDetail.as_view(), name='post'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post'),
]
