from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class HomePage(Page):
    """Home Page Model"""
    templates = "templates/home/home_page.html"  # if not specified template loads from templates/app_name/page_class

    # Banner Content Fields
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,   # might cause migration problem, if previously not specified
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"  # use same as field name
    )

    # Call to action, create another wagtail page
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_rich_text", blocks.RichTextBlock()),
            ("simple_richtext", blocks.SimpleRichTextBlock()),
            ("cards", blocks.CardBlock()),
            ("call_to_action", blocks.CTABlock()),
        ],
        null=True,
        blank=True
    )

    # Created fields must be registered here
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
        StreamFieldPanel("content"),
    ]

    # only one home page per site
    max_count = 1

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
