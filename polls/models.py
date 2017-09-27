import datetime
from django.utils import timezone
from django.db import models

class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    choice_set = models.ManyToManyField('Choice', through='Vote', related_name='choices')
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def __str__(self):
        return self.question_text


class Vote(models.Model):
    question = models.ForeignKey(Question, related_name='votes')
    choice = models.ForeignKey(Choice, related_name='votes')
    votes = models.IntegerField(default=1)

    @staticmethod
    def addVote(q,c): #should this be given a question or a string
        connection=Vote.get(q=q,c=c)
        if connection is None:
            Vote.objects.create(question=q, choice=c, votes=1)
        else:
            connection.increaseVote(amnt=1)
            connection.save()

    @staticmethod
    def get(q,c):
        q=Question.objects.filter(question_text=q)
        c=Choice.objects.filter(choice_text=c)
        v=Vote.objects.filter(question=q, choice=c)
        if len(v) > 0:
            return v[0]
        else:
            return None

    def increaseVote(self,amnt):
        self.votes+=amnt

    def __str__(self):
        return self.question.question_text + ' ' + self.choice.choice_text + ' '+ str(self.votes)

