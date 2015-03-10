from django.db import models

# Create your models here.
class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __self__(self):
        return self.slug
class Category( models.Model ):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.title

class EntryQuerySet(models. QuerySet):
    def published(self):
        return  self.filter( publish=True )


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    # category = models.ManyToOneRel(Category)

    object = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Law Entry"
        verbose_name_plural = "Law Entries"
        ordering = ["-created"]
