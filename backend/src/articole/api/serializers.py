from rest_framework import serializers

from articole.models import Articol

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articol
        fields = ('title' , 'content')
