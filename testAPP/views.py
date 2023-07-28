import base64

from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Question, Option


# Create your views here.

def index(request):
    return HttpResponse('first index web!')


def show_question(request):
    return render(request, '../templates/question/import_question.html')


def save_question(request):
    # 接收数据并返回到当前页面
    if request.method == 'POST':
        # 获取题干信息
        image_file = request.FILES.get('image')
        post_content = request.POST['content']
        post_difficulty = request.POST['difficulty']
        post_type = request.POST.get('question_type')

        # 判断获取到的题目是否已存在，若存在则无需录入
        if Question.objects.filter(content=post_content).exists():
            datas = Question.objects.all().order_by('-id')      # 题干数据
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


def question_image(request, pk):
    question = get_object_or_404(Question, pk=pk)
    option_contents  = [option[0] for option in Option.objects.filter(question=pk).values_list('content')]
    print(option_contents)
    if question.image:
        image_data = question.image.read()
        # 将图片数据转换为 Base64 编码的字符串
        image_base64 = base64.b64encode(image_data).decode('utf-8')

        data = {
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

