from django.shortcuts import render
from .forms import AnswerForm
from .models import Questions, Answer

def question(request):
    ques = Questions.objects.filter(slot=1).order_by("ques_no")

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.candidate = request.user
            f.save()

    context = { 
        'form':AnswerForm(),
        'questions':ques,
    }
    
    print(Answer.objects.all())
    return render(request, 'questions/index.html', context)