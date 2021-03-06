
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model): # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
# The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username



#chapter 5 all of this
#__str__() #Java daki toString()dir! Gerekeli olunca kullan!!

class Category(models.Model):
    maxLength=128 #chp 7 maxlength assigned here
    name = models.CharField(max_length=maxLength, unique=True) #chp 7 burda category. agerek yok aynı class icindedir.
    views = models.IntegerField(default=0) #exercise chp5
    likes = models.IntegerField(default=0) #exercise chp5
    slug = models.SlugField(unique=True)#chp6

    def save(self, *args, **kwargs): #chp6 3 lines below
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #cascade bu foreign key silininca bunula alakalı herşeyi sil demek
    #category foreign keydir ve baglandıgı sey da Category olandir!
    title = models.CharField(max_length=Category.maxLength) #chp7 cateegory.maxlength
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
