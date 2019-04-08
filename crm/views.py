from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View
from django import forms
from django.contrib import auth
from crm.models import UserInfo
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    user = forms.CharField(min_length=5)
    pwd = forms.CharField(min_length=5)
    r_pwd = forms.CharField(min_length=5)
    email = forms.EmailField(min_length=5)

    def clean_user(self):
        val = self.cleaned_data.get('user')
        user = UserInfo.objects.filter(username=val).first()
        if user:
            raise ValidationError('用户名已使用！')
        else:
            return val

    def clean_pwd(self):
        val = self.cleaned_data.get('pwd')
        if val.isdigit():
            raise ValidationError('密码不能为纯数字！')
        else:
            return val

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')
        if pwd and r_pwd and r_pwd != pwd:
            raise ValidationError('两次密码不一致')
        else:
            return self.cleaned_data

    def clean_email(self):
        val = self.cleaned_data.get('email')
        import re
        if re.search(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', val):
            return val
        else:
            raise ValidationError('请输入正确邮箱地址')


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
