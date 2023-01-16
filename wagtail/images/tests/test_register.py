from django.template import Variable
from django.test import TestCase

from wagtail.images.models import Image, Rendition
from wagtail.images.templatetags.wagtailimages_tags import ImageNode
from wagtail.images.tests.utils import get_test_image_file


class ImageNodeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an image for running tests on
        cls.image = Image.objects.create(
            title="Test image",
            file=get_test_image_file(),
        )

    def test_register_format(self):
        self.assertTrue(False)