from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
  def create_user(self, user_id, name, email, password=None):
    if not user_id:
      raise ValueError('Users must have an user id')
    if not name:
      raise ValueError('Users must have an name')      
    if not email:
      raise ValueError('Users must have an email address')      

    user = self.model(
      user_id = user_id,
      name = name,
      email=self.normalize_email(email),
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self,  user_id, name, email, password):
    user = self.create_user(
      user_id,
      name,
      email,
      password=password,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user



class User(AbstractBaseUser):
  user_id = models.CharField('사용자 ID', max_length=50, unique=True)
  name = models.CharField('이름', max_length=50)
  email = models.EmailField('이메일',max_length=255, unique=True,)

  is_active = models.BooleanField('활성', default=True)
  is_admin = models.BooleanField('관리자', default=False)

  objects = UserManager()

  USERNAME_FIELD = 'user_id'
  REQUIRED_FIELDS = ['name', 'email']

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True

  @property
  def is_staff(self):
    return self.is_admin

  def __str__(self):
    return self.user_id

