from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=300)
    number = models.CharField(max_length=300,unique=True,null=False)
    email = models.EmailField(unique=True, null=False)
    address = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=300,unique=True,null=False)
    description = models.TextField()
    price = models.FloatField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    published_date = models.DateField()
    stock = models.IntegerField()
    def __str__(self):
        return self.name
    

    
