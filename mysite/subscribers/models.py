from django.db import models


class Subscribers(models.Model):
    """A subscriber model"""

    email = models.CharField(blank=False, null=False, help_text="Email address", max_length=100)
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text="First and Last name")

    def __str__(self):
        """String representation of this object"""
        return self.full_name

    class Meta:  # noqa
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
