from django.db import models

# Create your models here.

class MathFormulas(models.Model):
    math_formula = models.CharField(max_length=100)


    def __str__(self):
        return 'self.math_formula'
