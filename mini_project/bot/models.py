from django.db import models

# Create your models here.
class BotData(models.Model):
    category = models.CharField(max_length=100, default="N/A")
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'BotData'
        verbose_name_plural = 'BotDataset'

    def __str__(self):
        return self.title


    
