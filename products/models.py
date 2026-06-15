from django.db import models

# Create your models here.
class Kitoblar(models.Model):
    CHOICE = [
        ('black', 'Qora'),
        ('white', 'Oq'),
        ('red', 'Qizil'),
        ('blue', 'Kok'),
        ('gray', 'Kulrang'),
    ]
    nashr = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    year = models.IntegerField()
    desc = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    color = models.CharField(max_length=12, choices=CHOICE)
    photo = models.ImageField(upload_to= 'kitob/',  null=True, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "kitoblar "
        ordering = ['-id']