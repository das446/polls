import datetime
from django.utils import timezone
from django.db import models

class Choice(models.Model):
    choice_text=models.CharField(max_length=200)

    @staticmethod
    def get(c): #returns the choice or makes a new one if it doesn't exist
        choice = Choice.objects.filter(choice_text=c)
        if len(choice) > 0:
            return choice[0]
        else:
            return Choice(choice_text=choice)

    def __str__(self):
        return self.choice_text

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    choice_set = models.ManyToManyField('Choice', through='Vote', related_name='choices')
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def removeChoice(self,choice):
        vote=Vote.get(q=self,c=choice)
        Vote.get(q=self, c=choice).delete()

    def addChoice(self,choice):
        self.save()
        Vote.addVote(q=self,c=choice,amnt=0)

    def removeAllChoices(self):
        for choice in self.choice_set.all():
            self.removeChoice(choice)



    def __str__(self):
        return self.question_text


class Vote(models.Model):
    question = models.ForeignKey(Question, related_name='votes')
    choice = models.ForeignKey(Choice, related_name='votes')
    votes = models.IntegerField(default=0)

    @staticmethod
    def addVote(q,c,amnt=1):
        connection=Vote.get(q=q,c=c)
        q.save()
        c.save()

        if connection is None:
            return Vote.objects.create(question=q, choice=c, votes=amnt)
        else:
            connection.increaseVote(amnt=amnt)
            connection.save()
            return connection

    @staticmethod
    def get(q,c):
        q=Question.objects.filter(question_text=q)
        c=Choice.get(c=c)
        v=Vote.objects.filter(question=q, choice=c)
        if len(v) > 0:
            return v[0]
        else:
            return None

    def increaseVote(self,amnt):
        self.votes+=amnt

    def __str__(self):
        return self.question.question_text + ' ' + self.choice.choice_text + ' '+ str(self.votes)

