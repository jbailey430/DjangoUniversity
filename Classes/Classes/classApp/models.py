from django.db import models


class DjangoClasses(models.Model):
    title = models.CharField(max_length=60)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.IntegerField()
    duration = models.FloatField()

    objects = models.Manager()


    def __str__(self):
        return self.name



class1 = DjangoClasses(title="Math",name="Math201", courseNumber=201,duration=2.5)
class1.save()
class2 = DjangoClasses(title="History",name="History101", courseNumber=101,duration=1.5)
class2.save()
class3 = DjangoClasses(title="Anatomy",name="Bio401", courseNumber=401,duration=3.5)
class3.save()

