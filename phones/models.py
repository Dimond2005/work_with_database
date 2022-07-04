from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    image = models.CharField(max_length=90)
    release_date = models.CharField(max_length=30)
    lte_exists = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
