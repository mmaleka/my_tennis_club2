from django.db import models

# Create your models here.
class pingservor(models.Model):
    
    ping_server = models.CharField(max_length=7, blank=True, default='')
    # ping_server_quality = models.CharField(max_length=7, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.pk) + " - " + self.ping_server