from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    """Social media settings for our custom website"""

    facebook = models.URLField(blank=True, null=True, help_text="Facebook url")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter url")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube url")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ], heading="Social Media Settings")
    ]