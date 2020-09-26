from django.db import models


class Status(models.TextChoices):
    EN = 'EN', 'Enviado'
    RV = 'RV', 'Revisado'
    RE = 'RE', 'Reprovado'
    AP = 'AP', 'Aprovado'
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title  = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.EN,
    )

    def __str__(self):
        return self.title