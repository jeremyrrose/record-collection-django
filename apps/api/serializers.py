from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Record, Artist, Collection




class RecordSerializer(serializers.ModelSerializer):
    artist = serializers.ReadOnlyField(source='artist.name')

    class Meta:
        model = Record
        fields = ('id', 'title', 'artist', 'release_year', 'cover_image')

class ArtistSerializer(serializers.ModelSerializer):
    records = RecordSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'hot_100_hits', 'records')

class CollectionSerializer(serializers.ModelSerializer):
    records = RecordSerializer(many=True, read_only=True)
    record_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Record.objects.all(), source='records')
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Collection
        fields = ('id', 'owner', 'owner_id', 'records', 'record_ids')