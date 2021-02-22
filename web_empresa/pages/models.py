from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    modified = models.DateTimeField(verbose_name="Fecha de actualización", auto_now=True)
    
    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title
            