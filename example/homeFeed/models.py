# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Test(models.Model):
	# name = models.CharField(max_length=20)manage
	id = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 100, null = False)
	content = models.TextField(null = False)
	illustration = models.CharField(max_length = 100)


