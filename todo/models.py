from django.db import models
import datetime
from django.utils import timezone 

# Create your models here.
class Todo(models.Model):
    """一个todo一般具有如下属性：
    title（分类）、text（内容）、added_time（添加时间）、finished_time（完成时间）
    """
    title = models.CharField(max_length = 100)
    text = models.CharField(max_length = 200)
    added_time = models.DateTimeField('Added time',auto_now_add=True)
    finished_time = models.DateTimeField('Finished time',auto_now_add=True)

    def __str__(self):
        return self.text