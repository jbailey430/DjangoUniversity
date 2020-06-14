from django.db import models


class DjangoClasses(models.Model):
    title = models.CharField(max_length=60)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.IntegerField()
    duration = models.FloatField()

    objects = models.Manager()


    def __str__(self):
        return self.name



