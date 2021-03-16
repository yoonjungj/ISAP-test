from django.urls import path
from isap import views

app_name = "isap"

urlpatterns = [
    path("", views.index, name="index")
    # path("post/<int:pk>", views.PostDetailView.as_view(), name="post")
]
