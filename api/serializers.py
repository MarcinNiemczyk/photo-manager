from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Photo
        fields = ('id', 'title', 'album_id', 'width', 'height', 'color', 'image', 'url')
        read_only_fields = ('width', 'height', 'color', 'url')
        extra_kwargs = {
            'image': {'write_only': True}
        }

    def get_image_url(self, obj):
        return obj.image.url
