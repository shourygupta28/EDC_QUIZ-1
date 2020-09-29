from django.db import models
from home.models import User

class Questions(models.Model):
    ques_type = (('Text', 'Text'),
                 ('MCQ', 'MCQ'),)

    ques_no     = models.IntegerField()
    slot        = models.IntegerField(default=0)
    ques        = models.CharField(max_length=50)
    option1     = models.CharField(max_length=100, null=True, blank=True)
    option2     = models.CharField(max_length=100, null=True, blank=True)
    option3     = models.CharField(max_length=100, null=True, blank=True)
    option4     = models.CharField(max_length=100, null=True, blank=True)
    ques_type   = models.CharField(choices=ques_type, max_length=5)
    correct_ans = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ques

    def has_prev(self):
        if self.ques_no > 1:
            return self.ques_no - 1
        else:
            return False
    
    def has_next(self):
        if self.ques_no < 15:
            return self.ques_no + 1
        else:
            return False

class Answer(models.Model):
    candidate   = models.OneToOneField(User, related_name = 'user_ans', on_delete=models.CASCADE, null=True, blank=True)
    answer1     = models.CharField(default='', null=True, max_length=100)
    answer2     = models.CharField(default='', null=True, max_length=100)
    answer3     = models.CharField(default='', null=True, max_length=100)
    answer4     = models.CharField(default='', null=True, max_length=100)
    answer5     = models.CharField(default='', null=True, max_length=100)
    answer6     = models.CharField(default='', null=True, max_length=100)
    answer7     = models.CharField(default='', null=True, max_length=100)
    answer8     = models.CharField(default='', null=True, max_length=100)
    answer9     = models.CharField(default='', null=True, max_length=100)
    answer10    = models.CharField(default='', null=True, max_length=100)
    answer11    = models.CharField(default='', null=True, max_length=100)
    answer12    = models.CharField(default='', null=True, max_length=100)
    answer13    = models.TextField(default='', null=True, max_length=100)
    answer14    = models.TextField(default='', null=True, max_length=100)
    answer15    = models.TextField(default='', null=True, max_length=100)

    # def __str__(self):
    #     return self.candidate + " - " + self.answer1 + " - " + self.answer2

