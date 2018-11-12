from django.db import models


class Ligne_Creesp_Lib(models.Model):
    Lib_origine = models.CharField(max_length=200)
    Lib_1 = models.CharField(max_length=200)
    Lib_2 = models.CharField(max_length=200)
    Lib_3 = models.CharField(max_length=200)
    Lib_4 = models.CharField(max_length=200)
    Lib_5 = models.CharField(max_length=200)
    Lib_6 = models.CharField(max_length=200)
    Lib_7 = models.CharField(max_length=200)
    Lib_8 = models.CharField(max_length=200)
    Lib_9 = models.CharField(max_length=200)
    Lib_10 = models.CharField(max_length=200)
    Lib_Choisi = models.CharField(max_length=200,blank=True)
