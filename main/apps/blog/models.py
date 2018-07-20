# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "Blog name should be more than 5 characters"
        if len(postData['desc']) < 5:
            errors["desc"] = "Blog desc should be more than 10 characters"
        return errors

class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()