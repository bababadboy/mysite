from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Todo
import json
from django.core import serializers #序列化的包

# Create your views here.
@require_http_methods(["GET"])
def add_todos(request):
    response = {}
    try:
        todo = Todo(text=request.GET.get('text'))
        todo.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_todos(request):
    response = {}
    try:
        todos = Todo.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", todos))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)