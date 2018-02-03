from django.db import models

# Create your models here.
class Inscricao(models.Model):

    id          = models.AutoField(primary_key=True)
    nome        = models.CharField('Nome', max_length=100, null=False, blank=False)
    rg          = models.BigIntegerField('RG',unique=True, null=False, blank=False)
    orgao       = models.CharField('Órgão expedidor', max_length=50, null=False, blank=False)
    telefone    = models.CharField('Telefone', max_length=20, null=True, blank=False)
    email       = models.EmailField('Email', max_length=50, null=False, blank=False)
    observacoes = models.TextField('Descrição', blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

#####

    def __str__(self):
        return 'ID: '+str(self.id)+' | Nome: '+self.nome+' | RG: '+str(self.rg)+' | Email: '+self.email
    class Meta:
        verbose_name        = 'Inscrição'
        verbose_name_plural = 'Inscrições'
