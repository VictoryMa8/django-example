from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField("date published")
    def __str__(self):
        return self.name

class Decision(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.description
    def has_good_rating(self):
        return self.rating > 5

class Aftermath(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description