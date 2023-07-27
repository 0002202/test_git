import base64

from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Question


# Create your views here.

def index(request):
    return HttpResponse('first index web!')


def show_question(request):
    return render(request, '../templates/question/import_question.html')


def save_question(request):
    # 接收数据并返回到当前页面
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        post_content = request.POST['content']
        post_answer = request.POST['answer']
        post_difficulty = request.POST['difficulty']
        post_type = request.POST.get('question_type')
        # 判断获取到的题目是否已存在
        if Question.objects.filter(content=post_content, answer=post_answer).exists():
            datas = Question.objects.all().order_by('-id')
            data = {
                'msg': datas,
                'error_message': '该问题已存在，无需录入',

            }

            return render(request, '../templates/question/import_question.html', context=data)  # 可以已弹窗的形式

        else:
            # 创建一个新的 Question 对象，将图片文件保存到数据库中
            question = Question(
                content=post_content,
                answer=post_answer,
                difficulty=post_difficulty,
                image=image_file,
                question_type=post_type,
            )
            question.save()
        # 将数据存入后，进行读取数据
        datas = Question.objects.all().order_by('-id')
        data = {
            'msg': datas,
            'error_message': '',
        }
        # 将数据存入到数据库中
        return render(request, '../templates/question/import_question.html', context=data)


def question_image(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if question.image:
        image_data = question.image.read()
        # 将图片数据转换为 Base64 编码的字符串
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        data = {
            'content': question.content,
            'question_type': question.get_question_type_display(),
            'image': image_base64
        }
        return render(request, '../templates/question/show_question.html', context=data)
    else:
        data = {
            'content': question.content,
            'question_type': question.get_question_type_display(),
        }
        return render(request, '../templates/question/show_question.html', context=data)

