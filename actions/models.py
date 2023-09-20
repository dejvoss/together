from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', db_index=True, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    # fields based on the generic relation to any model object used in app
    # generic relation is django feature that allows to connect any model to any other model
    # you can limit the types of models that can be connected to the generic relation
    # by specifying a limit_choices_to attribute in target_ct field
    target_ct = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name='target_obj',
        on_delete=models.CASCADE
    )
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)

    target = GenericForeignKey('target_ct', 'target_id')

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
