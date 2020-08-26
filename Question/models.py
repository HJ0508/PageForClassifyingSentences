from django.db import models

# Create your models here.

class QuestionInfo(models.Model):
    sentence = models.CharField(max_length=100)
    isPositive = models.SmallIntegerField(default=-1)
    isActivated = models.SmallIntegerField(default=-1)
    isTagged = models.BooleanField(default=False)

    def __str__(self):
        return self.sentence