from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ticket(BaseModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.deletion.SET_NULL,
        related_name='tickets',
        # Normally you wouldn't allow this to be null,
        # but it'd be unfortunate to lose a bunch of tickets
        # if a user account gets deleted
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.title


class Comment(BaseModel):
    ticket = models.ForeignKey(Ticket, on_delete=models.deletion.CASCADE, related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.deletion.SET_NULL,
        related_name='comments',
        # Normally you wouldn't allow this to be null,
        # but it'd be unfortunate to lose a bunch of tickets
        # if a user account gets deleted
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.body[:50]
