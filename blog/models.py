from django.db import models



# Create your models here.


class Blog(models.Model):
    
    FULLSTACK = 'FS'
    DEVOPS = 'AWS'
    DATA = 'DS'
    path = [(FULLSTACK, 'FullStack'),
            (DEVOPS, 'DevOps'), (DATA, 'DataScience'), ]
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    Title = models.CharField(max_length=50)
    Content = models.TextField()
    Image = models.ImageField(upload_to='img/', null=True, blank=True,)
    Category = models.CharField(
        choices=path, default="FullStack", max_length=3)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="Draft")
    date = models.DateTimeField(auto_now_add=True)
    user =models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True,null=True, )


