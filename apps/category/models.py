from django.db import models


class Category(models.Model):

    parent = models.ForeignKey(
        'self', related_name='children',
        on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id} | {self.name}'
