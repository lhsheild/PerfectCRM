from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View
from django import forms
from django.contrib import auth


class UserForm(forms.Form):
    pass


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.is_ajax():
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        response = {'user': None, 'err_msg': ''}
        user_obj = auth.authenticate(username=user, password=pwd)
        if user_obj:
            response['user'] = user
        else:
            response['err_msg'] = '用户名或密码错误！'
        return JsonResponse(response)


def get_valid_img(request):
    if request.method == 'GET':
        def get_random_color():
            import random
            return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

        from PIL import Image, ImageDraw, ImageFont
        from io import BytesIO
        img = Image.new('RGB', (350, 46), get_random_color())
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('static/font/fzsbt.ttf', 32)
        draw.text((0, 10), 'weicome to py', get_random_color(), font)
        f = BytesIO()
        img.save(f, 'png')
        data = f.getvalue()

        return HttpResponse(data)


def register(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'reg.html', locals())


class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html')


class CustomerList(View):
    def get(self, request):
        return render(request, 'sales/customers.html')
