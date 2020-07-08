from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager           

# Create your models here.

class UserProfileManager(BaseUserManager):
    ## helps django to work with our custom user model ##

    def create_user(self,name, email, password=None):
        """Create new user profile object """
        if not email :
            raise ValueError('User Must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        #set_password will encrypt the password 
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """ to create new super user"""
        user = self.create_user(email,name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user





class UserProfile(AbstractBaseUser, PermissionsMixin):
    # ======represent "user profile" inside our system====
    email =  models.EmailField(max_length=254, unique = True)
    name = models.CharField(max_length=254)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get users full name """
        return self.name

    def get_short_name(self):
        """ Used to get a Users Short name. """
        return self.name

    def __str__(self):
        """ Django uses this when it needs to convert the object to string """

        return str(self.email)

