from django.db import models

class Workspace(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	description = models.TextField()
	# Temporalmente, eliminamos el ForeignKey a Owner para crear la migración básica
	owner_id = models.ForeignKey('account.Owner', on_delete=models.CASCADE) # owner_id activado
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Department(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	description = models.TextField()
	workspace_id = models.ForeignKey('Workspace', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name