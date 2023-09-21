from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField()
    
    def __str__(self) -> str:
        return  self.first_name.capitalize() +" "+ self.last_name.capitalize()


class Tag(models.Model):
    caption = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.caption.capitalize()


class Posts(models.Model):
    title = models.CharField(max_length=40,null=True)
    image = models.ImageField(upload_to='posts/',blank=True)
    date = models.DateField(auto_now=True,null=True)
    slug = models.SlugField(null=True,default="",blank=True,unique=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)
    tag = models.ManyToManyField(Tag,blank=True)
    description = models.TextField(validators=[MinLengthValidator(10)],default='')

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
