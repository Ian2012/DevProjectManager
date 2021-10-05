from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(
            email=self.normalize_email(email),
            **kwargs,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Company(models.Model):
    name = models.CharField(max_length=32)
    nit = models.CharField(max_length=10, help_text="Insert nit without period or middle dash")
    phone = models.CharField(max_length=14)
    direction = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return self.name


class User(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Project(models.Model):
    name = models.CharField(max_length=32)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='projects')

    def __str__(self):
        return self.name


class UserStory(models.Model):
    description = models.CharField(max_length=32)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='stories')

    def __str__(self):
        return f"{self.description} - {self.project.name}"


class Ticket(models.Model):
    class STATE(models.IntegerChoices):
        ACTIVE = 1
        IN_PROCCES = 2
        FINISHED = 3

    user_story = models.ForeignKey(UserStory, on_delete=models.CASCADE, related_name='tickets')
    description = models.CharField(max_length=64)
    state = models.IntegerField(choices=STATE.choices, default=STATE.ACTIVE, blank=True)
    canceled = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['state']


class TicketComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    message = models.CharField(max_length=512)
