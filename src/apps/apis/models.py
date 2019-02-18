from django.db import models

class BaseModel(models.Model):
	"""Basic fields for each model"""
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

	def delete(self, *args, **kwargs):
		"""Soft Deleting the record"""
		self.is_deleted = True
		self.save()
