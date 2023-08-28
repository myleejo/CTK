from django.db import models

# Create your models here.


class Problem(models.Model):
    problem_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    score = models.IntegerField()
    category = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    ssh_path = models.CharField(max_length=100)

