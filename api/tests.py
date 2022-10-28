from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from api.models import Photo
from api.services import get_dominant_color


class PhotoTestCase(TestCase):
    def setUp(self):
        image_bytes = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04'
            b'\x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x44\x01\x00\x3b '
        )
        photo_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_bytes,
            content_type='image/jpeg'
        )
        self.photo = Photo.objects.create(
            title='foo',
            album_id=1,
            image=photo_image,
            color=get_dominant_color(photo_image.name)
        )
        self.photo_expected_values = {
            'title_length': 255,
            'width': 1,
            'height': 1,
            'color': '#040404'
        }

    def test_title_max_length(self):
        max_length = self.photo._meta.get_field('title').max_length
        self.assertEqual(max_length, self.photo_expected_values['title_length'])

    def test_width_is_correct(self):
        self.assertEqual(self.photo.width, self.photo_expected_values['width'])

    def test_height_is_correct(self):
        self.assertEqual(self.photo.height, self.photo_expected_values['height'])

    def test_dominant_color_is_correct(self):
        self.assertEqual(self.photo.color, self.photo_expected_values['color'])
