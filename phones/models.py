from django.db import models


# id, name, price, image, release_date, lte_exists и slug. Поле id - должно быть основным ключом модели.
class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=200)
    release_date =models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)