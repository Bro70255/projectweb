from django.db import models


class Destination(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()


    def __str__(self):
        return self.title