from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 2 or len(postData['name']) > 101:
            errors['name'] = "Name must be between 2 and 100 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "The email you entered is not valid"
        if len(postData['email']) < 10 or len(postData['email']) > 36:
            errors['email'] = "Email must be between 10 and 35 characters."
        return errors

class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()
    
    def __repr__(self):
        return "<Users Object: {} {}".format(self.name, self.email)