from rest_framework import serializers
from oyan.catalog.models import Articles

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articles
        fields = '__all__'