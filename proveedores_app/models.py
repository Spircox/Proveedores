from django.db import models
from django.contrib.auth.models import User

class Proveedores(models.Model):
    bfirstname = models.CharField(max_length=60)
    bemail = models.EmailField(max_length=50)
    bnit = models.CharField(max_length=30)
    bfile = models.BooleanField(default=False)
    bfile2 = models.BooleanField(default=False)
    bfile3 = models.BooleanField(default=False)
    bfile4 = models.BooleanField(default=False)
    fecha_s = models.DateTimeField(blank=True, null=True)
    id_usr = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'Proveedores_veri'
