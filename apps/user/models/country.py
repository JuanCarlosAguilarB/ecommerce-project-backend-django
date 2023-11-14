from django.db import models


class Country(models.Model):
    """
    Model by create and save a Country.
    """
    id = models.AutoField(primary_key=True)
    alpha_2_code = models.CharField(max_length=6, null=True)
    abbreviation_name = models.CharField(
        max_length=50, null=True, blank=True)
    dial_code = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.name
