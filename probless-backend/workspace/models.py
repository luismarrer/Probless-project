from django.db import models
from django import forms


class Workspace(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_at = models.DateTimeField(null=True)
	owner_id = models.ForeignKey('account.Owner', on_delete=models.CASCADE)

class Department(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	workspace_id = models.ForeignKey('workspace.Workspace', on_delete=models.CASCADE)
