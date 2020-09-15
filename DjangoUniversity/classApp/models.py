from django.db import models

# Create your models here.


class DjangoClasses(models.Model):
    CourseNum = models.IntegerField(max_length=10, primary_key=True)
    Title = models.CharField(max_length=60, default='', null=False)
    Instructor = models.CharField(max_length=60, default='', null=False)
    Duration = models.FloatField(null=False)

    objects = models.Manager()

    def __str__(self):
        return self.Title