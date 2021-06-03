from django.db import models


class Guess(models.Model):
    word = models.CharField(max_length=20)

    class Meta:
        db_table = 'guess'
