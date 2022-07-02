from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Category")
    def __str__(self):
        return self.name




class Book(models.Model):
    status_book = [
        ('available',"available"),
        ('rented',"rented"),
        ('soled',"soled"),

    ]

    title = models.CharField(_("title"), max_length=250)
    author =models.CharField(_("author"), max_length=250, null = True , blank = True)
    photo_book = models.ImageField(_("photo"), upload_to='photos', null = True , blank = True)
    photo_author = models.ImageField(_("photo by aothor"), upload_to='photos', null = True , blank = True)
    pages = models.IntegerField(_("pages"), null = True , blank = True)
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2, null = True , blank = True)
    retal_price_day = models.DecimalField(_("retal_price_day"), max_digits=5, decimal_places=2, null = True , blank = True)
    retal_period = models.IntegerField(_("retal_period"), null = True , blank = True)
    active = models.BooleanField(_("active"), default=True)
    status = models.CharField(_("status"), max_length=50 , choices=status_book)
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.PROTECT, null = True , blank = True)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Book")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
