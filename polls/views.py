#二、使用通用模板
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'top5'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    # same as above, no changes needed.
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_msg':"Wrong choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        #HttpResponseRedirect只有一个参数，是重定向网址
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

#一、改良视图之前
# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse,Http404,HttpResponseRedirect
# from .models import Choice,Question
# from django.template import loader
# from django.shortcuts import render,get_object_or_404
# from django.urls import reverse

# def index(request):
#     #1. return HttpResponse("<p>Hello, world</p>. You're at the polls index.")

#     #2.
#     # top5 = Question.objects.order_by('pub_date')[:5]
#     # output = '<br>'.join([q.question_text for q in top5])#list genorator
#     # return HttpResponse(output)

#     #3.
#     # top5 = Question.objects.order_by('pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context= {
#     #     "top5":top5
#     # }
#     # #把上下文加载到模板中，其实就是把context作为参数传入/polls/template/polls/index.html文件
#     # return HttpResponse(template.render(context,request))

#     #4.
#     top5 = Question.objects.order_by('pub_date')[:5]
#     context= {
#         "top5":top5
#     }
#     #使用shortcuts.render便捷函数，可以免去HttpResponce
#     return render(request,'polls/index.html',context)

# def detail(request,question_id):
#     #1.
#     #return HttpResponse("You're looking at the question %s" % question_id)

#     #2.
#     # try:
#     #     question = Question.objects.get(pk = question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question not exist!")
#     # return HttpResponse(question,request)

#     #3.在2的基础上改进，直接使用shortcut.render快捷函数
#     # try:
#     #     question = Question.objects.get(pk = question_id)
#     #     context = {
#     #         'question':question
#     #     }
#     # except Question.DoesNotExist:
#     #     raise Http404("Question not exist!")
#     # return render(request,'polls/detail.html',context)

#     #4.在3的基础上改进，使用get_object_or_404()函数,免去手动抛出异常的步骤
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{'question':question})
    
# def result(request,question_id):
#     result = get_object_or_404(Question,pk=question_id)
#     return render(request,'/polls/result.html',{'result':result})


def vote(request,question_id):
    #1. return HttpResponse("You're voting the question %s" % question_id)
    #2.
    question = get_object_or_404(Question,pk=question_id)
    

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_msg':"Wrong choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        #HttpResponseRedirect只有一个参数，是重定向网址
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
    
