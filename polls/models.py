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

    was_published_recently.boolean=True #修改布尔值的样式
    was_published_recently.short_description = 'published recently?' #简写
    was_published_recently.admin_order_field = 'pub_date'#排序方式为pub_date
    '''
    用于描述数据的元数据Meta
    '''
    class Meta:
        ordering = ['pub_date','question_text']



class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    def __who__(self):
        return "I made the choice"
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
