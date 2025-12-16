from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.CharField(max_length=200)  # static path

    def __str__(self):
        return self.name


class Phone(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"


class Overview(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class KeySpec(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
