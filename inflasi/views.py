from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Barang


def index(request):
    latest_Barang_list = Barang.objects.order_by('-id')
    print(latest_Barang_list)
    context = {"latest_Barang_list": latest_Barang_list}
    return render(request, "inflasi/index.html", context)

def detail(request, barang_id):
    latest_Barang_list_id = Barang.objects.order_by("nama_barang")
    barang = get_object_or_404(Barang, pk=barang_id)
    print(Barang.Hitung_Inflasi)
    return render(request, "inflasi/detail.html", {"barang": barang})