from django.db import models


class Round(models.Model):
    hint_1 = models.CharField(max_length=30)
    hint_2 = models.CharField(max_length=30)
    hint_3 = models.CharField(max_length=30)
    hint_4 = models.CharField(max_length=30)
    hint_5 = models.CharField(max_length=30)
    solution = models.CharField(max_length=30)

    def __str__(self):
        return f"round {self.pk}"