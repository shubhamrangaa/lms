from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

# class UserProfile(models.Model):
#     # uuid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
#     # user_name = models.ForeignKey(User,on_delete=models.CASCADE)# or Foreign key?
#     user_name = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
#     # user_name = models.CharField(max_length=200,null=True,blank=True) 
#     email = models.CharField(max_length=200,null=True,blank=True)
#     mobile = models.CharField(max_length=10,null=True,blank=True) 
#     profile_image = models.CharField(max_length=200,null=True,blank=True)
#     first_name = models.CharField(max_length=200,null=True,blank=True)
#     last_name = models.CharField(max_length=200,null=True,blank=True)
#     # is_deleted = models.CharField(max_length=100,null=True,blank=True)
#     teacher = "teacher"
#     student = "student"
#     user_type = [(teacher,"teacher"),(student,"student")]
#     user_role = models.CharField(max_length=255, choices=user_type)

#     def __str__(self):
#         return str(self.user_name)



class MyUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth,user_role, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            user_role=user_role,
        )

        user.set_password(password)
        user.save()
        # user.save(using=self._db)
        return user

    def create_superuser(self,username, email, date_of_birth,user_role, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        if not password:
            raise ValueError('Users must have a password')

        user = self.create_user(
            username,
            email,
            date_of_birth,
            user_role,
            password,
        )

        user.is_superuser = True
        user.is_admin= True
        
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=20,unique=True) 
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=10,null=True,blank=True) 
    profile_image = models.URLField(null=True,blank=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    # is_deleted = models.CharField(max_length=100,null=True,blank=True)
    teacher = "teacher"
    student = "student"
    user_type = [(teacher,"teacher"),(student,"student")]
    user_role = models.CharField(max_length=255, choices=user_type)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth','username','user_role']

    def __str__(self):
        return self.username

    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




