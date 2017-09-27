from django.test import TestCase
from django.urls import reverse
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question, Choice, Vote

def create_question(question_text, days):
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)

class M2MTests(TestCase):
    def setUp(self):
        time = timezone.now()
        who=Question.objects.create(question_text='Who?',pub_date=time)
        what=Question.objects.create(question_text='What?',pub_date=time)
        when=Question.objects.create(question_text='When?',pub_date=time)

        yes=Choice.objects.create(choice_text='Yes')
        no=Choice.objects.create(choice_text='No')

        Vote.addVote(q=who, c=yes)
        Vote.addVote(q='Who?',c='Yes')
        Vote.addVote(q=who, c=no)
        Vote.addVote(q=what, c=yes)
        Vote.addVote(q=what, c=no)
        Vote.addVote(q=when, c=yes)
        Vote.addVote(q=when, c=no)



    def test_WhoYes2(self):
        v=Vote.get(q='Who?',c='Yes')
        self.assertEqual(v.votes, 2)

    def test_WhatNo1(self):
        v=Vote.get(q='What?',c='No')
        self.assertEqual(v.votes, 1)