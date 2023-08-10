from django.db import models

class MyTaskModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    expire=models.DateField()
    finichs=models.BooleanField()
