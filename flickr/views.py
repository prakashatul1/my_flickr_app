from rest_framework.permissions import IsAuthenticated
from flickr.models import Profile, Flickrgroup, Photo
from rest_framework import viewsets
from flickr.serializers import UserSerializer, GroupSerializer, PhotoSeralizer

# Create your views here.


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Profile.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Flickrgroup.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """

    queryset = Photo.objects.all()
    serializer_class = PhotoSeralizer
    permission_classes = (IsAuthenticated,)
