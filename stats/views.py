from django.shortcuts import render


# Create your views here.


def all_stats(request):
  
    return render(request, "all_stats.html")