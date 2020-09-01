from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class schoolInformation(models.Model):
    schoolId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    schoolName = models.CharField(max_length=300, blank=True, default='')
    
    def __str__(self):
        return self.schoolName

class userInformation(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userName = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return self.userName

class schoolReview(models.Model):
    reviewId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userId = models.ForeignKey(userInformation,on_delete=models.CASCADE)
    schoolId = models.ForeignKey(schoolInformation,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    userRating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    userReview = models.TextField(blank=True,default='')
    userPhotosURL = ArrayField(models.TextField(),blank=True,null=True)
    isReviewHelpful = ArrayField(models.CharField(max_length=36),blank=True,null=True)
    isReviewNotHelpful = ArrayField(models.CharField(max_length=36),blank=True,null=True)
    isReviewAbusive = ArrayField(models.CharField(max_length=36),blank=True,null=True)
    def __str__(self):
        return str(self.userRating) + " " + str(self.userReview) 

class reviewPhoto(models.Model):
    photoID  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userID  = models.ForeignKey(userInformation,on_delete=models.CASCADE)
    schoolID = models.ForeignKey(schoolInformation,on_delete=models.CASCADE)
    userPhotosURL = models.ImageField(upload_to='schoolReview/')
    def __str__(self):
        return str(self.userPhotosURL)


class schoolReviewComment(models.Model): 
    commentID =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reviewID  = models.ForeignKey(schoolReview,on_delete=models.CASCADE)
    userId = models.ForeignKey(userInformation,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    userComment = models.TextField(blank=True,default='')
    isReviewAbusive = ArrayField(models.CharField(max_length=36),blank=True,null=True)

    
