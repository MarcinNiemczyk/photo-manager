from rest_framework import serializers
from .models import Photo
from .services import download_image, get_dominant_color


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
        photo = Photo()
        photo = self.fill_data(photo, validated_data)
        photo.save()
        return photo

    def update(self, instance, validated_data):
        instance = self.fill_data(instance, validated_data)
        instance.save()
        return instance

    def fill_data(self, instance, validated_data):
        url = validated_data['url']
        filename = download_image(url)
        color = get_dominant_color(filename)

        instance.title = validated_data['title']
        instance.album_id = validated_data['album_id']
        instance.image.name = filename
        instance.color = color
        return instance
