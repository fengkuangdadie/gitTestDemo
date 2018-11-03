from django.contrib.auth.models import User, Group
from rest_framework import serializers

from REST.models import Dog


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("url", "name")


class DogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dog
        fields = ("url", "d_name", "d_legs")