from django.db import models
from django.conf import settings


class Client(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, help_text="Nombre completo del cliente.")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    

class Comment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='comments', help_text="Cliente al que pertenece el comentario.")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments', help_text="Usuario que hizo este comentario.")
    text = models.TextField(null=False, blank=False, help_text="Contenido del comentario.")
    date = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora en que se creó el comentario")

    def __str__(self):
        return f"Comentario de {self.user.username if self.user else 'Usuario Eliminado'} en {self.client.name} ({self.date.strftime('%Y-%m-%d')})"
    
    class Meta:
        ordering = ['-date']