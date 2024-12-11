from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Create your models here.
class Joinery(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name="Название товара"
                             )
    short_descr = models.TextField(verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Описание")
    material = models.CharField(max_length=100,
                                verbose_name='Материал'
                                )
    cost = models.DecimalField(max_digits=19,
                               decimal_places=2,
                               verbose_name="Стоимость",
                               default=0
                               )
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Столярное изделие"
        verbose_name_plural = "Столярные изделия"


class Ceramics(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name="Название товара"
                             )
    short_descr = models.TextField(verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Описание")
    material = models.CharField(max_length=100,
                                verbose_name='Материал'
                                )
    cost = models.DecimalField(max_digits=19,
                               decimal_places=2,
                               verbose_name="Стоимость", default=0
                               )
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name="Категория"
                                 )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Керамическое изделие"
        verbose_name_plural = "Керамические изделия"