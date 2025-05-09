from django.db import models


# === BANCO DE DADOS ===
class usuario(models.Model):
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome