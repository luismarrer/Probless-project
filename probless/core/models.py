from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.name}"


class Ticket(models.Model):
	PRIORITY_CHOICES = (
		('low', 'Low'),
		('medium', 'Medium'),
		('high', 'High'),
	)
	STATUS_CHOICES = (
		('open', 'Open'),
		('in_progress', 'In Progress'),
		('closed', 'Closed'),
	)

	title = models.CharField(max_length=255)
	description = models.TextField()
	documentation = models.TextField(blank=True, null=True)
	user_id = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
	priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
	assigned_department_id = models.ForeignKey('workspace.Department', on_delete=models.CASCADE)
	incoming_department_id = models.ForeignKey('workspace.Department', on_delete=models.CASCADE, related_name='incoming_department', null=True, blank=True)
	image = models.ImageField(upload_to='tickets/', null=True, blank=True)
	status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open')
	tags = models.ManyToManyField(Tag, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['created_at', 'priority', 'status']

	def __str__(self):
		return self.title

