from django.db import models

class Entry(models.Model):
    item = models.TextField()
    count = models.IntegerField()

    def __str__(self):
        return self.item
