from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from api.models import Photo
from api.services import get_dominant_color
from api.serializers import PhotoSerializer


class PhotoTestCase(TestCase):
    def setUp(self):
        image_bytes = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04'
            b'\x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x44\x01\x00\x3b'
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

    def test_title_max_length(self):
        max_length = self.photo._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_width_is_correct(self):
        self.assertEqual(self.photo.width, 1)

    def test_height_is_correct(self):
        self.assertEqual(self.photo.height, 1)

    def test_dominant_color_is_correct(self):
        self.assertEqual(self.photo.color, '#040404')

    def test_color_invalid_hex_code(self):
        invalid_hex_codes = [
            '#foo', 'ddd', '#zzz', 'FFFFFF', '#barbaz', '#90909o', '#f0f0f0f'
        ]
        for code in invalid_hex_codes:
            with self.assertRaises(ValidationError):
                self.photo.color = code
                self.photo.full_clean()

    def test_color_valid_hex_code(self):
        valid_hex_codes = [
            '#ddd', '#f0f0f0', '#dddddd', '#ffffff', '#123456', '#777'
        ]
        for code in valid_hex_codes:
            self.photo.color = code
            self.photo.full_clean()


class PhotoSerializerTestCase(TestCase):
    def setUp(self):
        image_bytes = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04'
            b'\x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x44\x01\x00\x3b'
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
        self.serializer_data = {
            'title': 'bar',
            'albumId': 1,
            'url': 'https://git-scm.com/images/logos/logomark-orange.png'
        }

        self.serializer = PhotoSerializer(instance=self.photo)

    def test_output_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'title', 'albumId', 'width',
                                            'height', 'color', 'image'])

    def test_album_id_output_is_snake_case(self):
        field_source = self.serializer._declared_fields['albumId'].source
        self.assertEqual(field_source, 'album_id')

    def test_output_image_is_url_format(self):
        data = self.serializer.data
        self.assertEqual(data['image'], self.photo.image.url)

    def test_valid_input_image_url(self):
        serializer = PhotoSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_input_image_url(self):
        self.serializer_data['url'] = 'foobar'
        serializer = PhotoSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertCountEqual(serializer.errors, ['url'])
