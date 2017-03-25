from django.db import models

class App(models.Model):
    ccx = models.CharField(max_length=3, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.ccx

    class Meta:
        ordering = ['ccx']
