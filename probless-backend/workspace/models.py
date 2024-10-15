from django.db import models

class Workspace(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	description = models.TextField()
	# Temporalmente, eliminamos el ForeignKey a Owner para crear la migración básica
	user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, null=True, blank=True) # owner_id activado
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Department(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
	description = models.TextField()
	workspace_id = models.ForeignKey('Workspace', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name