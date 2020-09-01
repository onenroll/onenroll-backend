from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'schoolReview', views.schoolReviewViewSet)
router.register(r'userInformation', views.userInformationViewSet)
router.register(r'schoolInformation', views.schoolInformationViewSet)
router.register(r'reviewPhoto', views.reviewPhotoViewSet)
router.register(r'schoolReviewComment', views.schoolReviewCommentViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [path('', include(router.urls)), path('api-auth/',
               include('rest_framework.urls', namespace='rest_framework'
               ))
               # path('', views.populatedatabase, name= 'home'),
               ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)              # For handling media files request