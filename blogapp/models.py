from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from autoslug import AutoSlugField# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError('User must provide a email')

        user = self.model(
            email = email,
            name = name
        )


        user.set_password(password)
        user.save(using = self._db)

        return user


    def modNotes(self, email, name, password = None):
        user = self.create_user(email,name,password)

        user.is_mod = True
        user.is_nUser = True
        user.is_staff = False
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password = None):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.is_nUser = False
        user.is_mod = False

        user.save(using = self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length = 50,unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_mod = models.BooleanField(default=False)
    is_nUser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    coins_scored = models.IntegerField(default=100,null=True,blank=True)
    rank = models.IntegerField(default=0)
    bookmarks = models.ManyToManyField('blogapp.Notes', blank=True)
    is_emailVerified = models.BooleanField(default=False)


    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.name} ({self.coins_scored})"

class Subject(models.Model):

    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    teacherurl = models.CharField(max_length=300,null=True,blank=True)
    img = models.ImageField(upload_to='subImage/',null=True,blank=True)
    def __str__(self):
        return self.name

class Module(models.Model):

    name = models.CharField(max_length=50)
    sub = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Notes(models.Model):

    typ = (

        ('Assignment','Assignment'),
        ('Experiment','Experiment'),
        ('Notes','Notes'),
        ('ReferenceBook','Reference Book'),
        ('LectureSlides','Lecture Slides'),
        ('PYQ','PYQ'),



    )

    mods = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )




    desc = models.TextField(max_length=500,null=True,blank=True)
    mod = models.CharField(max_length=5,choices=mods,null=True,blank=True)
    file = models.FileField(upload_to='notes/')
    author = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    likes = models.ManyToManyField(UserAccount,related_name="notes_like",default=0)
    views = models.PositiveIntegerField(default=0)
    buy=models.ManyToManyField(UserAccount,related_name="buy_notes")
    typeN = models.CharField(max_length=50,null=True,blank=True,choices=typ)
    docid = models.CharField(max_length=300,null=True,blank=True)
    sub =  models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
    slug = AutoSlugField(populate_from = 'sub',unique=True,null=True,default=None)




    nDetail = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):

        niu = f'{self.sub.name} - {self.mod} {self.typeN} by {self.author}'

        return niu

    def acceptStatus(self):

        return f'/acceptStatus/{self.slug}/'

    def attachLink(self):
        return f'/addDriveLink/{self.slug}/'

    def comnt(self):
        return f'/notes/{self.slug}/comment/'


class Comment(models.Model):
    toU = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    fromU = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name='fromCmnt')
    note = models.ForeignKey(Notes,on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from = 'fromU',unique = True)
    cmnt = models.TextField()
    cmntDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cmnt} by {self.toU.name}'

    def reply(self):

        return f'/notes/{self.note.slug}/comment/{self.slug}/'

    def seeR(self):
        return f'/seeRply/{self.slug}/'


class CmntReply(models.Model):

    cmtRply = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    cmntR = models.TextField()
    frR = models.TextField()
    slug = AutoSlugField(populate_from = 'cmntR',unique = True)

    def __str__(self):
        return f'{self.frR} from {self.frR}'

class Reminder(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField(auto_now=False,auto_now_add=False)
    description = models.TextField(blank=True)