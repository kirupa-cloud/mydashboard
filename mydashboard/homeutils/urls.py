from django.urls import path
from .views import *

from rest_framework.routers import SimpleRouter
from homeutils.views import UtilityNew

router = SimpleRouter(trailing_slash=False)
router.register("util", UtilityNew, "homeutils")
urlpatterns = router.urls

# urlpatterns = [
#     path('utilityinfo/', UtilityInfoView.as_view()),
#     path('UtilityDetails/<str:pk>/', UtilityDetails.as_view()),
# ]
