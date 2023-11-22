from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):   #By default name come in db
        return self.name

class Employees(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    address=models.TextField()        
    #phone=models.IntegerField()
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
