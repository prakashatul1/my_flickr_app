from rest_framework import serializers
from flickr.models import Flickrgroup, Photo, Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('nsid', 'name', 'group')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flickrgroup
        fields = ('nsid', 'group_name','photo_set')


class PhotoSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo_id', 'secret', 'server', 'farm', 'title', 'owner_name', 'image',
                  'image_url', 'group')