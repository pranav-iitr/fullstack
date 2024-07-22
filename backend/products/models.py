from django.db import models
from User.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Audiobook(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='audiobooks')
    cover_image = models.ImageField(upload_to='covers/')
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    average_rating = models.FloatField(default=0)
    total_reviews = models.IntegerField(default=0)
    seo_title = models.CharField(max_length=255,default="")
    seo_description = models.TextField(default="")
    seo_keywords = models.TextField(default="")

    

    def __str__(self):
        return self.title
    

class Review(models.Model):
    audiobook = models.ForeignKey(Audiobook, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True,blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True,blank=True,default=None)
    def __str__(self):
        return f'Review by {self.user.first_name} for {self.audiobook.title}'
    def save(self, *args, **kwargs ) :
        
        self.audiobook.average_rating = (self.audiobook.average_rating*self.audiobook.total_reviews + self.rating) // (self.audiobook.total_reviews + 1)
        self.audiobook.total_reviews += 1
        self.audiobook.save()
        super().save( *args, **kwargs)
    
