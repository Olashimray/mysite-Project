from django.db import models



Class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



Class choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
