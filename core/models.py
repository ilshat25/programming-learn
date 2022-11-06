from django.db import models


# Create your models here.
class Level(models.Model):
    level_map = models.CharField(max_length=2500)
    width = models.IntegerField(default=-1)
    height = models.IntegerField(default=-1)
    x_start = models.IntegerField(default=-1)
    y_start = models.IntegerField(default=-1)
    x_finish = models.IntegerField(default=-1)
    y_finish = models.IntegerField(default=-1)
    num = models.IntegerField(unique=True)

    def __str__(self):
        return f'number = {self.num} width = {self.width} height = {self.height}'
