from django.shortcuts import render
from math import ceil
from django.core.paginator import Paginator
from . import models

# Create your views here.


def new(request) :
    return render(request, 'r3/new.html')

# def all_R3(request):
#     page = request.GET.get("page")
#     R3_list = models.R3.objects.all()
#     paginator = Paginator(R3_list, 10)
#     R3 = paginator.get_page(page)
#     return render(request, "R3/home.html", {"R3": R3})
