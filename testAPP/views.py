from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Question


# Create your views here.

def index(request):
    return HttpResponse('first index web!')


def show_question(request):
    return render(request, '../templates/question/show_question.html')


def save_question(request):
    # 接收数据并返回到当前页面
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        post_content = request.POST['content']
        post_answer = request.POST['answer']
        post_difficulty = request.POST['difficulty']
        # 判断获取到的题目是否已存在
        if Question.objects.filter(content=post_content, answer=post_answer).exists():
            datas = Question.objects.all()
            data = {
                'msg': datas,
                'error_message': '该问题已存在，无需录入'
            }
            return render(request, '../templates/question/show_question.html', context=data)  # 可以已弹窗的形式

        else:
            # 创建一个新的 Question 对象，将图片文件保存到数据库中
            question = Question(
                content=post_content,
                answer=post_answer,
                difficulty=post_difficulty,
                image=image_file
            )
            question.save()
        # 将数据存入后，进行读取数据
        datas = Question.objects.all().order_by('-id')
        data = {
            'msg': datas,
            'error_message': ''
        }
        # 将数据存入到数据库中
        return render(request, '../templates/question/show_question.html', context=data)


def question_image(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if question.image:
        return HttpResponse(question.image.read(), content_type="image/jpeg")
    else:
        return HttpResponseNotFound()
