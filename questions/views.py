from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AnswerForm
from .models import Questions, Answer
from home.models import User
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

# def calculate_marks(request):
#     answers = Answer.objects.all()

#     for answer in answers:
#         for slot in range(1, 5):
#             correct_answer = Answer()
#             if answer.candidate.slot == slot:
#                 temp = "Slot" + str(slot)
#                 u = User.objects.get(name=temp)
#                 correct_answer = Answer.objects.get(candidate=u)
#                 break
            
            
#         for i in range(1, 13):
#             ans = "answer" + str(i)
#             if answer.__getattribute__(ans) == correct_answer.__getattribute__(ans):
#                 answer.candidate.points += 10
#                 answer.save()
#         print(answer.candidate, answer.candidate.points)

#     return redirect('thank-you')