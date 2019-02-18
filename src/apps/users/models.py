from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from apis.models import BaseModel

from users.manager import CustomUserManager

# AbstractBaseUser - To use the basic authentication of django user model
class User(AbstractBaseUser, BaseModel):
	"""Model to Store User Details"""
	email = models.EmailField(max_length=254, unique=True)
	name = models.CharField(max_length=254, null=True, blank=True)
	# default behaviour of user is member
	is_admin = models.BooleanField(default=False)
	# to temporary deactivate the user
	is_active = models.BooleanField(default=True)
	# Below for superuser
	is_staff = models.BooleanField(default=False, blank=True)

	# Marking USERNAME_FIELD as email
	USERNAME_FIELD = 'email'

	objects = CustomUserManager()

	def has_perm(self, perm, obj=None):
		return self.is_staff

	def has_module_perms(self, app_label):
		return self.is_staff

	def save(self, *kwg, **kwargs):
		"""
		Overiding model method to set the password
		"""
		self.set_password(self.password)
		super(User, self).save(*kwg, **kwargs)

