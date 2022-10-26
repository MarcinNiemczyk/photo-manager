from rest_framework import serializers
from .models import Photo
from .services import download_image


class PhotoSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField('get_image_url')
    url = serializers.URLField(write_only=True, label='URL')

    class Meta:
        model = Photo
        fields = ('id', 'title', 'album_id', 'width', 'height', 'color', 'image', 'url')
        read_only_fields = ('width', 'height', 'color', 'image')

    def get_image_url(self, obj):
        return obj.image.url

    def create(self, validated_data):
        url = validated_data['url']
        filename = download_image(url)

        photo = Photo()
        photo.title = validated_data['title']
        photo.album_id = validated_data['album_id']
        photo.image.name = filename
        photo.save()
        return photo
