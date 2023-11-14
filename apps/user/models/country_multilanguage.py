from django.db import models
from apps.user.models import Country


class CountryMultilanguage(models.Model):

    name = models.CharField(max_length=50, null=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='country_multilanguages')
    multilanguage_id = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['country', 'multilanguage_id'],
                name='unique_country_multilanguage_id_combination'
            )
        ]

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)
