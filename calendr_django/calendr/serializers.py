from rest_framework import serializers
from .models import User, Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )

    event_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )

    class Meta:
        model = User
        fields = ('id', 'events', 'event_url', 'username')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    event_url = serializers.ModelSerializer.serializer_url_field(
        view_name='event_detail'
    )

    class Meta:
        model = TeamSerializer
        fields = ('id', 'user', 'user_id', 'event_url',
                  'title', 'description', 'date',)

# Do we need a calendar serializer?
# class CalendarSerializer(serializers.HyperlinkedModelSerializer):
