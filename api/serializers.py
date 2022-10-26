from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField('get_image_url')
    url = serializers.URLField(write_only=True, label='URL')

    class Meta:
        model = Photo
        fields = ('id', 'title', 'album_id', 'width', 'height', 'color', 'image', 'url')
        read_only_fields = ('width', 'height', 'color', 'image')

    def get_image_url(self, obj):
        return obj.image.url
