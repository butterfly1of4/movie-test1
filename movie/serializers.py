from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # queryset=Movie.objects.all(),
    class Meta:
        model=Movie
        fields = ['id', 'display_title', 'byline', 'opening_date', 'headline', 'summary_short', 'url', 'image']

# class MovieSerializer(serializers.HyperlinkedModelSerializer):

#     movies = serializers.HyperlinkedRelatedField(
#         # )
#         view_name='full_list',
#         many=True,
#         read_only=True
#     )
#     movies= serializers.ModelSerializer.serializer_url_field(
#         view_name='movies')

#     class Meta:
#         model = Movie
#         fields = ('id', 'display_title', 'byline', 'opening_date',
#                   'headline', 'summary_short', 'url', 'image')
