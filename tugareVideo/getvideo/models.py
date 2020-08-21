from django.db import models

class Video(models.Model):
    video_title = models.CharField("Título do Vídeo", max_length=255, blank=False, null=False)
    video_country = models.CharField("País do Vídeo", max_length=255, blank=False, null=False)
    video_thumb = models.CharField("Tempo do thumbnail", max_length=10, blank=False, null=False)
    video_url = models.CharField("URL Google Drive", max_length=255, blank=False, null=False)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.video_title
