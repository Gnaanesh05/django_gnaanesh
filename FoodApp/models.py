from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Food(models.Model):
    name=models.CharField(max_length=30)
    carbs=models.FloatField()
    protein=models.FloatField()
    calories=models.FloatField()
    calcium=models.FloatField()

    def __str__(self):
        return self.name 
    
class Consume_Food(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed=models.ForeignKey(Food,on_delete=models.CASCADE)