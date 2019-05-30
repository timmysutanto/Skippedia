from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nim = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Komentar(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    isi_komentar = models.CharField(max_length=300)

    def __str__(self):
        return self.isi_komentar

class Rating(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.rate)

