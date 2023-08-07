from django.urls import path

from . import views

urlpatterns = [
   path('', views.list_post, name='list_post'),
   path('detail/<int:id>/', views.detail_post, name='detail_post'),
   path('share_post/<int:id>/', views.share_post, name='share_post'),
]
