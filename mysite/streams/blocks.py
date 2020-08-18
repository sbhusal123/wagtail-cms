"""Stream fields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else"""

    title = blocks.CharBlock(required=True, help_text='Add your title.')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:  # noqa
        template = 'streams/title_and_text_block.html'
        icon = "edit"
        label = "Title and Text"


class RichTextBlock(blocks.RichTextBlock):
    """Rich text with all the features"""

    class Meta: #noqa
        template = "streams/rich_text_block.html"
        icon = "doc-full"
        label = "Full Rich Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and buttons"""

    title = blocks.CharBlock(required=True, help_text='Add your title.')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If button page above is selected,"
                                                                         "that will be used first"))
            ]
        )
    )

    class Meta: #noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff cards"



class SimpleRichTextBlock(blocks.RichTextBlock):
    """Rich text(limited) without all features"""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.field_options = {
            'required': required,
            'help_text': help_text,
            'validators': validators,
        }
        self.editor = editor
        self.features = [
            "bold",
            "italic",
            "link"
        ]

    class Meta: #noqa
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Simple Rich Text"


class CTABlock(blocks.StructBlock):
    """A simple call to action section"""

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, max_length=400, features=['bold', 'italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta: # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to action"
