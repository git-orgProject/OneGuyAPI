import random
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse

from django.shortcuts import render, redirect

from user import models
from user.models import UserModel, UserForm

from common.code import new_code_str
def index(request):
    pass



def login(request):
    if request.method == "POST":
            login_form = UserForm(request.POST)
            message = "请检查填写的内容！"
            if login_form.is_valid():
                phone = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                try:
                    user = models.UserModel.objects.filter(phone=phone).first()
                    if user.password == password:
                        return redirect('index/')
                    else:
                        message = "密码不正确！"
                except:
                    message = "用户不存在！"
            return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def new_img_code(request):

    # 创建画布
    img = Image.new('RGB', (120, 40), (100, 100, 0))

    # 从画布中获取画笔
    draw = ImageDraw.Draw(img, 'RGB')

    # 创建字体对象和字体颜色
    font_color = (0, 20, 100)
    font = ImageFont.truetype(font='static/fonts/buding.ttf',
                              size=30)

    valid_code = new_code_str(6)
    request.session['code'] = valid_code

    # 开始画内容
    draw.text((5, 5), valid_code, font=font, fill=font_color)

    for _ in range(500):
        x = random.randint(0, 120)
        y = random.randint(0, 40)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        draw.point((x, y), (r, g, b))

    # 将画布写入内存字节数组中
    from io import BytesIO
    buffer = BytesIO()
    img.save(buffer, 'png')  # 写入

    return HttpResponse(content=buffer.getvalue(),
                        content_type='image/png')
def register(request):
    pass



def logout(request):
    pass




