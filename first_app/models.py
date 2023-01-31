from django.db import models
from django.utils import timezone

# Create your models here.
def user_directory_path(instance,filename):
    return 'first_app/{0}/{1}'.format(instance,filename)

class post(models.Model):

    class PostObjects():
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options=(('draft','Draft'),('published','published'))

    title=models.CharField(max_length=200)
    thumnail=models.ImageField(upload_to=user_directory_path,blank=True,null=True)
    excerpt=models.TextField(null=True)
    content=models.TextField(null=True)
    slug=models.SlugField(max_length=250,unique_for_date='published',null=False,unique=True)
    published=models.DateTimeField(default=timezone.now)
    #author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_user')
    status=models.CharField(max_length=10,choices=options,default='draft')
    objects=models.Manager()
    postobjects=PostObjects
    

    class meta():
        ordering=('-published')
    
    def __str__(self):
        return self.title