from django.shortcuts import render, HttpResponse
from django.views import View


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')


def get_valid_img(request):
    if request.method == 'GET':
        def get_random_color():
            import random
            return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

        from PIL import Image, ImageDraw
        from io import BytesIO
        img = Image.new('RGB', (350, 46), get_random_color())
        draw = ImageDraw.Draw(img)
        draw.text()
        f = BytesIO()
        img.save(f, 'png')
        data = f.getvalue()

        return HttpResponse(data)


class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html')


class CustomerList(View):
    def get(self, request):
        return render(request, 'sales/customers.html')
