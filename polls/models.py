from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    def __who__(self):
        return "It is me!"
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)#是否是一天之内发布的

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    def __who__(self):
        return "I made the choice"
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
