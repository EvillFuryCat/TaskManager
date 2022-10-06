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
    tag = serializers.CharField(sourse="get_race_display", read_only=True)

    class Meta:
        model = tags.Tag
        fields = "title"


class StatusSerializer(serializers.ModelSerializer):
    status = serializers.CharField(sourse="get_race_display", read_only=True)

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
    tags = TagSerializer(many=True)
    statuses = StatusSerializer()

    class Meta:
        model = task.Task
        fields = (
            "id",
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
