from django.db import models
from user.models import User
# Create your models here.

from django.contrib.auth import get_user_model
from problem.models import Problem


class UserScore(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    solved_problems = models.ManyToManyField(Problem, blank=True)
    crypto_score = models.IntegerField(default=0)
    system_score = models.IntegerField(default=0)
    linux_score = models.IntegerField(default=0)
    web_score = models.IntegerField(default=0)

    def add_score(self, score, category):
        if category == 'Crypto':
            self.crypto_score += score
        elif category == 'System':
            self.system_score += score
        elif category == 'Linux':
            self.linux_score += score
        elif category == 'Web':
            self.web_score += score
        self.total_score += score
        self.save()

    def has_solved(self, problem):
        return problem in self.solved_problems.all()
    
    def __str__(self):
        return self.user.email
    
