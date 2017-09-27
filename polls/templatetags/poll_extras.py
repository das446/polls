from django import template
from polls.models import *

register = template.Library()

register.simple_tag(lambda q, c: Vote.get(q=q,c=c).votes, name='getVotes')