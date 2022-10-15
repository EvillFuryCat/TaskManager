from rest_framework import serializers
from .models import tags, user, task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone",
        )


class TagSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        tag_name = value.title
        return tag_name

    class Meta:
        model = tags.Tag
        fields = ("title",)


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = task.Task
        fields = (
            "title",
            "description",
            "date_creation",
            "date_change",
            "deadline",
            "author",
            "executor",
            "tags",
            "priority",
            "status",
        )
