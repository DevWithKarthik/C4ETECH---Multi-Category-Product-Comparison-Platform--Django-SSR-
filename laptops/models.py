from django.db import models

# Create your models here.

class BrandLaptop(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Laptop(models.Model):
    brand = models.ForeignKey(BrandLaptop, on_delete=models.CASCADE,  related_name="laptops")
    name = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"
    
class LaptopOverview(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name="overviews")
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.text
    
class LaptopKeyspecs(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name="keyspecs")
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.text

