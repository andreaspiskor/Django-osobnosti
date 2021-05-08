from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

class Druh(models.Model):
    oznaceni_druhu = models.CharField(max_length=50, unique=True, verbose_name="Označení druhu osobnosti",
                                      help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    OBLAST = (
        ('herec', 'Herec'),
        ('politik', 'Politik'),
        ('sportovec', 'Sportovec'),
        ('zpěvák', 'Zpěvák'),
        ('celebrita', 'Celebrita'),
    )
    oblast = models.CharField(max_length=20, choices=OBLAST, blank=True, default='celebrita', verbose_name="Oblast",
                              help_text='Vyberte označení oblasti')

    class Meta:
        ordering = ["oznaceni_druhu"]
        verbose_name = 'Druh zaměření'
        verbose_name_plural = 'Druh zaměření'

    def __str__(self):
        return f"{self.oznaceni_druhu}, {self.oblast}"

class Osobnosti(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name="Jméno osobnosti",
                             help_text='Zadejte jméno o maximální délce 50 znaků')

    prijmeni = models.CharField(max_length=50, verbose_name="Přijmení osobnosti",
                             help_text='Zadejte přijmení o maximální délce 50 znaků')

    popis = models.TextField(blank=True, null=True, verbose_name="Popis osobnosti")
    foto = models.ImageField(upload_to='osobnosti/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka osobnosti")
    druh = models.ForeignKey(Druh, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["druh","jmeno"]
        verbose_name = 'Osobnost'
        verbose_name_plural = 'Osobnosti'

    def __str__(self):
        return f"{self.jmeno}, {self.prijmeni}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
