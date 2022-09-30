from django.db import models
from .user import User
from .tags import Tag


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="task")
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True, verbose_name="deadline")
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="author", verbose_name="author")
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, related_name="task_executor", verbose_name="executor"
    )
    tags = models.ManyToManyField(Tag, related_name="Tag", verbose_name="Tag")


    class Priority(models.TextChoices):

        HIGH = "H"
        MEDIUM = "M"
        LOW = "L"
        NO_PRIORITY = "None"

        PRIORITY = [
            (HIGH, "High"),
            (MEDIUM, "Medium"),
            (LOW, "Low"),
            (NO_PRIORITY, "None"),
        ]

    priority = models.CharField(
        max_length=255, choices=Priority.choices, default=Priority.NO_PRIORITY
    )

    class Status(models.TextChoices):

        NEW_TASK = "new_task"
        IN_DEVELOPMENT = "in_development"
        IN_QA = "in_qa"
        IN_CODE_REVIEW = "in_code_review"
        READY_FOR_RELEASE = "ready_for_release "
        RELEASED = "released"
        ARCHIVED = "archived"

    status = models.CharField(
        max_length=255,
        choices=Status.choices,
        default=Status.NEW_TASK,
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task'
        
    