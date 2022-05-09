from django.db import models


class TimeStampedModel(models.Model):
    """Time Stamped Model Definition"""
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    """ Category model definition """
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Todo(models.Model):
    """Todo model definition"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='todos')

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title




