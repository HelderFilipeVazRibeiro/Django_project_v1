from django.db import models

class MinhaImagem(models.Model):
    imagem = models.ImageField(upload_to='media/')