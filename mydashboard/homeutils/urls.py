from django.urls import path
from .views import *

from rest_framework.routers import SimpleRouter
from homeutils.views import UtilityNew, UtilityUpdate

router = SimpleRouter(trailing_slash=False)
router.register("util", UtilityUpdate, "homeutils")
urlpatterns = router.urls

# urlpatterns = [
#     path('utilityinfo/', UtilityInfoView.as_view()),
#     path('UtilityDetails/<str:pk>/', UtilityDetails.as_view()),
# ]
