from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    author_name = models.CharField(_('Name'), max_length=255)
    author_email = models.EmailField(_('Email'))
    content = models.TextField(_('Content'))


class Attachment(models.Model):
    message = models.ForeignKey(Message, verbose_name=_('Message'))
    file = models.FileField(_('Attachment'), upload_to='attachments')
