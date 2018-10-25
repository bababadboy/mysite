from django.contrib import admin

# Register your models here.

from .models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']  #根据pub_date筛选结果
    search_fields = ['question_text']   #根据question_text搜索
    list_display = ('question_text','pub_date','was_published_recently')
admin.site.register(Question,QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','choice_text','votes')

admin.site.register(Choice,ChoiceAdmin)
