from django.contrib.auth.models import User
from django.db import models

class Chawo(models.Model):
    quest = models.TextField(max_length=51)
    ans = models.TextField(max_length=500)

    def __str__(self):
        return f'question: {self.quest}, ' \
               f'answer: {self.ans}, ' \



class Goods(models.Model):
    Name = models.TextField(max_length=51)
    cost = models.IntegerField(default=0)
    rate=models.IntegerField(default=5)
    image=models.TextField(max_length=100)
    owner=models.ForeignKey(User, on_delete=models.CASCADE,)
    sold_type=models.BooleanField(default=False)
    resourse_typee=models.SmallIntegerField(default=0)

    def __str__(self):
        return f'name: {self.Name}, ' \
               f'cost: {self.cost}, '\
               f'owner: {self.owner}'\
               f'rate: {self.rate}'


class Vallet(models.Model):
    web=models.TextField(max_length=100)
    money=models.IntegerField(default=0)
    vallet_number=models.TextField(max_length=200)
    owner=models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return f'web: {self.web}, ' \
               f'money: {self.money}, '\
               f'vallet_number: {self.vallet_number}'\



# Create your models here.
