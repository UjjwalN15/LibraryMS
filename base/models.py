from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=300)
    number = models.CharField(max_length=300,unique=True,null=True)
    email = models.EmailField(unique=True, null=True)
    address = models.CharField(max_length=300, null=True)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=300,unique=True,null=False)
    description = models.TextField()
    price = models.FloatField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    published_date = models.DateField()
    pdf_file = models.FileField(upload_to='books/pdf/', null=True, blank=True)
    def __str__(self):
        return self.name
    

    
