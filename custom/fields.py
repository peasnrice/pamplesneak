from django.db import models

class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase
