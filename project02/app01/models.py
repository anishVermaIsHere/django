from django.db import models



class Food(models.Model):
    
    name=models.CharField(max_length=20)
    category=models.CharField(max_length=10)
    price=models.FloatField(max_length=10)
    offer=models.CharField(max_length=20)


class Category(models.Model):
    
    name=models.CharField(max_length=20)


class Order(models.Model):

	date=models.DateField()
	time=models.TimeField()





def __str__(self):
    return self.name
    




