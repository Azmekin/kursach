from django.db import models

class Chawo(models.Model):
    quest = models.TextField(max_length=51)
    ans = models.TextField(max_length=500)

    def __str__(self):
        return f'question: {self.quest}, ' \
               f'answer: {self.ans}, ' \

# Create your models here.
