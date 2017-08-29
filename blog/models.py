from django.db import models
from django.utils import timezone
        
class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name="Autor")
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    text = models.TextField(verbose_name="Treść")
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name="Utworzono")
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name="Opublikowano")
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200, verbose_name="Autor")
    text = models.TextField(verbose_name="Treść")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Utworzono")
    approved_comment = models.BooleanField(default=False, verbose_name="Zaakceptowane")

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


