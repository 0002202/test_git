import base64
import random

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import Question, Option
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return HttpResponse('first index web!')


def show_question(request):
    if request.method == 'GET':
        search_key = request.GET.get('search_key')
        print(search_key)
        if search_key:
            # 将用户进行输入的值与数据库中存储的题目进行相比
            questions = Question.objects.filter(Q(content__icontains=search_key)).order_by('id')
        else:
            questions = Question.objects.all().order_by('id')
        data = {
            "question_list": questions,
        }
        print(data)
        return render(request, '../templates/question/show_question_list.html', context=data)


def save_question(request):
    # 接收数据并返回到当前页面
    if request.method == 'POST':
        # 获取题干信息
        image_file = request.FILES.get('image')
        post_content = request.POST['content']
        post_difficulty = request.POST['difficulty']
        post_type = request.POST.get('question_type')
        type_question = request.POST.get('type_question')     # 题目分类

        # 判断获取到的题目是否已存在，若存在则无需录入
        if Question.objects.filter(content=post_content).exists():
            datas = Question.objects.all().order_by('-id')  # 题干数据
            data = {
                'msg': datas,
                'error_message': '该问题已存在，无需录入',

            }
            return render(request, '../templates/question/import_question.html', context=data)  # 可以已弹窗的形式
        else:
            # 创建一个新的 Question 对象，将图片文件保存到数据库中
            question = Question(
                content=post_content,
                difficulty=post_difficulty,
                image=image_file,
                question_type=post_type,
                label=type_question,
            )
            question.save()
            # 获取选项内容，存在多个选项所以需要循环存储
            question_foreignkey = Question.objects.filter(content=post_content).first()
            for i in range(1, 5):  # 4个选项
                post_option = request.POST.get('option{}'.format(i))
                # 为正确答案时则将该选项记做正确答案
                correct_options = request.POST.get('correct_options')
                if int(correct_options) == i:
                    option = Option(question=question_foreignkey, content=post_option, is_correct=True)
                    option.save()
                    continue
                option = Option(question=question_foreignkey, content=post_option)
                option.save()
        # 将数据存入后，进行读取数据
        datas = Question.objects.all().order_by('-id')
        data = {
            'msg': datas,
            'error_message': '',
        }
        # 将数据存入到数据库中
        return render(request, '../templates/question/import_question.html', context=data)
    return render(request, '../templates/question/import_question.html')


def question_image(request, pk):
    question = get_object_or_404(Question, pk=pk)
    option_contents = [option[0] for option in Option.objects.filter(question=pk).values_list('content')]
    random.shuffle(option_contents)  # 将随机打乱顺序
    if question.image:
        image_data = question.image.read()
        # 将图片数据转换为 Base64 编码的字符串
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        data = {
            # 'pk': pk,   # 放弃了返回原始题号，因为需要重新生成题号
            'content': question.content,
            'question_type': question.get_question_type_display(),
            'image': image_base64,
            'options': option_contents
        }
        return render(request, '../templates/question/show_question.html', context=data)
    else:
        data = {
            'content': question.content,
            'question_type': question.get_question_type_display(),
            'options': option_contents,
        }
        return render(request, '../templates/question/show_question.html', context=data)


@csrf_exempt
def is_correct(request):
    # 用于接收用户返回的数据进行判断，由于使用ajax进行提交数据，则将忽略掉csrf认证
    if request.method == 'POST':
        msg, user_correct = '', False
        user_content = request.POST.get('content')
        user_option = request.POST.getlist('option')
        try:
            # 查询数据
            question = Question.objects.get(content=user_content)
            correct_options = Option.objects.filter(question=question, is_correct=True)  # 查询题干对应的正确选项
            correct_option_contents = [option.content for option in correct_options]  # 可能有多个正确选项
            if set(user_option) == set(correct_option_contents):
                msg = 'success'
                user_correct = True
                # 后面可以将该部分数据记录答题记录中
        except:
            msg = 'error'
        res = {
            'msg': msg,
            'is_correct': user_correct,
        }
        return JsonResponse(res)