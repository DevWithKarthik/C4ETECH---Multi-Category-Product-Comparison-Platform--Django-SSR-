from django.db import models

# Create your models here.

class BrandTablets(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Tablet(models.Model):
    brand = models.ForeignKey(BrandTablets, on_delete=models.CASCADE,  related_name="tablets")
    name = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"
    
class TabletOverview(models.Model):
    tablet = models.ForeignKey(Tablet, on_delete=models.CASCADE, related_name="overviews")
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.text
    
class TabletKeyspecs(models.Model):
    tablet = models.ForeignKey(Tablet, on_delete=models.CASCADE, related_name="keyspecs")
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.text

