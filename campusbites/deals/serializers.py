from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['price', 'description', 'event_name', 'address',
                   'calorie_per_dollar', 'date_of_event', 'time_of_event']