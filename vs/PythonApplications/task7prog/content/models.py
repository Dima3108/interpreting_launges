from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
class authors(models.Model):
    name=models.TextField()
class type_of_painting(models.Model):
    type=models.TextField()
class iatp(models.Model):
    name=models.TextField()
    type=models.ForeignKey(type_of_painting,on_delete=models.CASCADE)
    authorid=models.ForeignKey(authors,on_delete=models.CASCADE)
# Create your models here.
