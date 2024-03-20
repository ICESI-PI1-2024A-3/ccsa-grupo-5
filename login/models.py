from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)
    
class User(models.Model):
    """_
    This is the abstrac base for all of users.  
    """
    REQUIRED_FIELDS = [
        'name', 
        'lastName',  
        'password1',
        'password2',
        'email',
        ]
    
    USERNAME_FIELD = 'identification'
    
    User = settings.AUTH_USER_MODEL
    """
    All of the users are associated with a profile to contribute with the authentication
    """
    name = models.CharField (max_length = 35)
    """
    The name of the user
    
    Type: str
    """
    lastName = models.CharField (max_length = 35)
    """
    The last name of the user
    
    Type: str
    """
    identification = models.CharField (max_length = 15, primary_key=True, unique=True)
    """
    The government identification
    
    Type: str
    """
    password1 = models.CharField (max_length = 20)
    """
    The main password
    
    Type: str
    """
    
    password2 = models.CharField (max_length = 20)
    """
    This field is used to verify the main password at the register or an password update
    
    Type: str
    """
    
    email = models.CharField (max_length = 30)
    """
    This is the email of the user 
    
    Type:str
    """
    
    @property
    def is_anonymous (self):
        return False
    
    @property
    def is_authenticated(self):
        return True
    
    objects = CustomUserManager() 
    
    class Meta:
        abstract = True

class HiringManager (User):
    """
    This class has the minimum access permision and is 
    ralted with petitions by a foreing key
    """
    pass
        
    
    
class HiringLeader (User):
    """
    This is the leader, this user can manage HiringManagers.
    This user has a medium access to the system.
    This class inherits from hiring manager because a hiring leader also
    can do the same tasks
    
    """
    
    hiringManagers = models.ManyToManyField (HiringManager, related_name="hiringManager_list_to_a_leader")
    """
    All of Hiring managers in the system, this relationship 
    means de control on the hiring managers
    
    Type: list of hiring managers
    """
     
class Administrator (User):
    """
    This is the administrator, this user usually just
    sees the data about the hiring proccess. But, can manages
    the hiring leaders and the hiring leaders. This class 
    inherits from HiringLeader because an administrator also can
    do the same tasks of a Hiring leader
    """
    
    hiringManagersList = models.ManyToManyField (HiringManager, related_name="hiringManager_list_to_the_administrator")
    """
    All of Hiring managers in the system, this relationship 
    means de control on the hiring managers
    
    Type: list of hiring managers
    """
    hiringLeaders = models.ManyToManyField (HiringLeader, related_name="hiringLeader_list")
    """
    All of Hiring leaders in the system, this relationship 
    means de control on the hiring leaders
    
    Type: list of hiring leaders
    """