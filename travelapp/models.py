from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picss',max_length=100)
    desc = models.TextField(max_length=250)

    def __str__(self):
        return self.name
