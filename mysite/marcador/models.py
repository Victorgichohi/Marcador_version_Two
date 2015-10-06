from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
#this imports compatibility algorithms to help in displaying information in human readable form
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

#gives this element compatibility view
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
#sets the display name taccording to name
class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

#this returns only the public bookmarks
class PublicBookmarkManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicBookmarkManager, self).get_queryset()
        return qs.filter(is_public=True)

#returns the name to determine if an id is set in that field
def __str__(self):
        return self.name
#python compatibility added to this class
@python_2_unicode_compatible
class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, verbose_name='owner',
        related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)

    #this returns only the public bookmarks too
    objects = models.Manager()
    public = PublicBookmarkManager()

#sets the bookmarks display name according to date created
class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

def __str__(self):
        return '%s (%s)' % (self.title, self.url)
#creates id field if not set
def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Bookmark, self).save(*args, **kwargs)
