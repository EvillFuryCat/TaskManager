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
    class Meta:
        model = tags.Tag
        fields = ("title",)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = task.Task.Status
        fields = (
            "NEW_TASK",
            "IN_DEVELOPMENT",
            "IN_QA",
            "IN_CODE_REVIEW",
            "READY_FOR_RELEASE",
            "RELEASED",
            "ARCHIVED",
        )


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    status = StatusSerializer()

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
