from django.urls import path
from . import views


app_name = "isap"

urlpatterns = [
    path("", views.base, name="home"),
    # path("post/<int:pk>", views.PostDetailView.as_view(), name="post")
    
]
