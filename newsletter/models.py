from django.db import models


class Newsletter(models.Model):
    class Meta:
        # Prevent duplicate signups
        constraints = [
            models.UniqueConstraint(fields=['full_name', 'email'],
                                    name='unique name/email')
        ]
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
