from rest_framework import serializers
from .models import *
from django.db import models

class schoolInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolInformation
        fields = '__all__'


class userInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = userInformation
        fields = '__all__'

class schoolReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolReview
        depth = 1
        fields = '__all__'

class reviewPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviewPhoto
        fields = '__all__'

class schoolReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolReviewComment
        fields = '__all__'
