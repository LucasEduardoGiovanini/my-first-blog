from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #defino que meu modelo é um objeto (models.Model diz que o nosso modelo (o Post) é um modelo django, então o django sabe que deve salvar no banco.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #meu método de publicar o blog
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title