from django.urls import path
from isap import views as isap_views


app_name = "core"

urlpatterns = [
    path("", isap_views.base, name="home")
    
    ]
