from django.db import models

# Create your models here.
class Ticket(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user_id = models.ForeignKey('account.User', on_delete=models.CASCADE)
	priority = models.TextField()
	assigned_department_id = models.ForeignKey('workspace.Department', on_delete=models.CASCADE)
	staus = models.TextField()
