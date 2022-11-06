from django.db import models


# Create your models here.
class Level(models.Model):
    level_map = models.CharField(max_length=2500)
    width = models.IntegerField()
    height = models.IntegerField()
    x_start = models.IntegerField()
    y_start = models.IntegerField()
    num = models.IntegerField(unique=True)

    def __str__(self):
        return f'number = {self.num} width = {self.width} height = {self.height}'
