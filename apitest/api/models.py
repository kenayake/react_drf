from django.db import models
class Prodi(models.Model):
    prodi = models.CharField(max_length=200)
    def __str__(self):
        return self.prodi
    

class Mahasiswa(models.Model):
    name = models.CharField(max_length=100)
    nim = models.CharField(max_length=100)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photo/')
    def __str__(self):
        return self.name
# Create your models here.
