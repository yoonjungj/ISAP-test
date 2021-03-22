from django.shortcuts import render
from math import ceil
from django.core.paginator import Paginator
from . import models

# Create your views here.


# def all_pva(request):
#     page = request.GET.get("page")
#     pva_list = models.PVA.objects.all()
#     paginator = Paginator(pva_list, 10)
#     pva = paginator.get_page(page)
#     return render(request, "pva/home.html", {"pva": pva})
