from model_utils.models import TimeStampedModel

from django.db import models


class Question(TimeStampedModel):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Choice(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
