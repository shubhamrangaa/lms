from unicodedata import category
from tutorials.models import Images,Videos,Keywords,ContentType,Tutorial
# from custom_users.
from rest_framework import serializers
from custom_users.models import UserProfile

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = '__all__'

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'

class TutorialSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    images = ImageSerializer(many=True)
    videos = VideoSerializer(many=True)
    keywords = KeywordSerializer(many=True)
    category = ContentTypeSerializer()
    
    class Meta:
        model = Tutorial
        fields = (
            'pk',
            'uuid',
            'title',
            'description',
            'author',
            'updated',
            'timestamp',
            'comments',
            'category',
            'keywords',
            'images',
            'videos'
        )
        