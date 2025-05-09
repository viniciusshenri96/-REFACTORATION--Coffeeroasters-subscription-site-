from django.db import models

class usuario(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
