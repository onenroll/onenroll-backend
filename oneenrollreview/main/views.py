# Importing Models
from .models import *

# Importing Serializer
from .serializers import *

# Rest Modules
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend #Filter

class schoolReviewViewSet(viewsets.ModelViewSet):
    queryset = schoolReview.objects.all()
    serializer_class = schoolReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['schoolId']

class schoolInformationViewSet(viewsets.ModelViewSet):
    queryset = schoolInformation.objects.all()
    serializer_class = schoolInformationSerializer

class userInformationViewSet(viewsets.ModelViewSet):
    queryset = userInformation.objects.all()
    serializer_class = userInformationSerializer

class reviewPhotoViewSet(viewsets.ModelViewSet):
    queryset = reviewPhoto.objects.all()
    serializer_class = reviewPhotoSerializer

class schoolReviewCommentViewSet(viewsets.ModelViewSet):
    queryset =  schoolReviewComment.objects.all()
    serializer_class = schoolReviewCommentSerializer

