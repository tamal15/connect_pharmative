from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='media')
    price=models.IntegerField()
    new_product=models.BooleanField(default=False)
    slug=models.SlugField(unique=True)

    def __str__(self):
     return self.name

class Form(models.Model):
    c_fname=models.CharField(max_length=50)
    c_lname=models.CharField(max_length=45)
    c_email=models.CharField(max_length=50)
    c_subject=models.CharField(max_length=45)
    c_message=models.CharField(max_length=30)

    def __str__(self):
     return self.c_fname

