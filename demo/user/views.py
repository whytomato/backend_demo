# from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from user.models import User

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password_1=request.POST.get('password_1')
        password_2=request.POST.get('password_2')
        new_user=User(username=username,password=password_1)
        new_user.save()
        return JsonResponse({'errno':0,'msg':"注册成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})