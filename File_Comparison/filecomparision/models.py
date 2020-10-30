# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class File_Upload(models.Model):

    title = models.CharField(max_length=30)

    file_1 = models.FileField(blank=True,null=True)

    file_2 = models.FileField(blank=True, null=True)
