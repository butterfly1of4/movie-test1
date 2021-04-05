from rest_framework import serializers
from .models import Movie


# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Movie
#         fields = ('id', 'display_title', 'byline', 'opening_date', 'headline', 'summary_short', 'url', 'image')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    
    
    movies=serializers.HyperlinkedRelatedField(
        # queryset=Movie.objects.all(),
    # )
        view_name='full_list',
        many=True,
        read_only=True
    )
    movie_url = serializers.ModelSerializer.serializer_url_field(view_name='display_title')
    class Meta:
        model = Movie
        fields = ('id', 'display_title', 'byline', 'opening_date', 'headline', 'summary_short', 'url', 'image')