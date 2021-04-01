from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    movies=serializers.HyperlinkedRelatedField(
        view_name='movie',
        many=True,
        read_only=True
    )
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'year', 'summary')