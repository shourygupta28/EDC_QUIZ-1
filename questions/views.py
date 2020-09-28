from django.shortcuts import render
from .models import Questions

# Create your views here.
def question(request):
    ques = Questions.objects.filter(slot=1).order_by(ques_no)

    context = {
        'ques':ques,
    }
    return render(request, 'questions/index.html', context)