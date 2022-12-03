from importlib.resources import _

from django.db import models


class Product(models.Model):

    class Category(models.TextChoices):
        RESTOBAR = 'RB', _('Restobar')
        CAFE = 'CF', _('Cafe')
        CANTEEN = 'CN', _('Canteen')
        NIGHT_CLUB = 'NC', _('Night club')
        BAR = 'B', _('Bar')

    name = models.CharField(max_length=150)
    # city = models.Choices
    # parking = models.Choices
    av_check = models.CharField(max_length=30)
    # pay_type = models.Choices(PayType.name)

    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    work_hours = models.CharField(max_length=150)
    count_places = models.IntegerField
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.BAR)

    def __str__(self):
        return f'{self.pk} | {self.name}'
