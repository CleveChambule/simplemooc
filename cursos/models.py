from django.db import models


# Create your models here.

class CursoManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(nome__icontains=query) |
                                          models.Q(descricao__icontains=query))


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    descricao = models.TextField('Descricao simples', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_data = models.DateField('Data de inicio',
                                  null=True, blank=True)
    image = models.ImageField(
        upload_to='cursos/imagens', verbose_name='Imagem',
        null=True, blank=True)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    objects = CursoManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']