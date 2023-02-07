from django.db import models

class Students(models.Model):
    bfirstname = models.CharField(max_length=50)
    blastname = models.CharField(max_length=10)
    bemail = models.EmailField(max_length=30)
    bnit = models.CharField(max_length=15)
    bfile = models.BooleanField(default=False)
    bfile2 = models.BooleanField(default=False)

    class Meta:
        db_table = 'Estudiantes'
