from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Name

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        # fields = ('url', 'username', 'reference', 'hash')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        # fields = ('url', 'name', 'files')

class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Name
        fields = ('name', 'reference', 'hash_1')