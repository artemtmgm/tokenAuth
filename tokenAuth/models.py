from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.forms import models


class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None,
                    company_name=None, phone=None, type_user=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            phone=phone,
            type_user=type_user
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    company_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    type_user = models.CharField(max_length=30, blank=True, null=True)

    USERNAME_FIELD = 'email'

    objects = MyAccountManager()

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return str(self.email)
