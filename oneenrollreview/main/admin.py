from django.contrib import admin
from .models import *

admin.site.register(schoolInformation)
admin.site.register(userInformation)
admin.site.register(schoolReview)
admin.site.register(schoolReviewComment)
admin.site.register(reviewPhoto)
