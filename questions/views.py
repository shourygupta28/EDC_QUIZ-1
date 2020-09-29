from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import AnswerForm
from .models import Questions, Answer
import datetime

@login_required
def question(request):
    if not (request.user.start_time):
        u = request.user
        u.start_time = datetime.datetime.now()
        u.save()
    ques = Questions.objects.filter(slot=1).order_by("ques_no")

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.candidate = request.user
            f.save()

    context = { 
        'form': AnswerForm(),
        'questions': ques,
        'end_time': (request.user.start_time + datetime.timedelta(minutes=15)).strftime("%B %d, %Y %H:%M:%S")
    }
    
    print(request.user.start_time, context['end_time'])
    return render(request, 'questions/index.html', context)