from catalog.models import Articles
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articles
        fields = '__all__'
        extra_kwargs = {'author': {'required': False}, 'genre': {'required': False}}