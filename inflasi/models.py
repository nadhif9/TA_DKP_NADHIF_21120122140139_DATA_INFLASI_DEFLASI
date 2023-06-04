from django.db import models
from datetime import datetime

class Barang(models.Model):
    nama_barang = models.CharField(max_length=20)
    harga_barang = models.IntegerField()
    harga_barang2 = models.IntegerField()
    dibuat = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nama_barang
    def Hitung_Inflasi(self):
        global harga_barangf, harga_barang2f
        harga_barang = int(self.harga_barang)  
        harga_barang2 = int(self.harga_barang2) 
        hasil = (harga_barang2 - harga_barang)/harga_barang2 * 100
        hasil = round(hasil, 2)
        return hasil
    def Inflasi_Deflasi(self):
        harga_barang = int(self.harga_barang)  
        harga_barang2 = int(self.harga_barang2)  
        hasil = (harga_barang2 - harga_barang)/harga_barang2 * 100
        if(hasil > 0):
            hasil = "Inflasi"
        else:
            hasil = "Deflasi"
        return hasil
    def harga_barangf(self):
        harga_barang = int(self.harga_barang)
        return f"{harga_barang:,}"
    def harga_barang2f(self):
        harga_barang2 = int(self.harga_barang2)
        return f"{harga_barang2:,}"