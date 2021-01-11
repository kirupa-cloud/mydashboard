from django.urls import path
from .views import *

from rest_framework.routers import SimpleRouter
from homeutils.views import UtilityNew, UtilityUpdate, UtilityPayment, UtilityPaymentview

router = SimpleRouter(trailing_slash=False)
router.register("utilinfo", UtilityUpdate)
router.register("groceryinfo", GroceryInfoView)

# router.register("utilpayment", UtilityPaymentview)
# urlpatterns = router.urls

urlpatterns = router.urls + [
    path('utilpayment/', UtilityPayment.as_view({'get': 'retrieve', 'post' : 'create'})),
    path('detail/', DetailView.as_view())
]

# urlpatterns = [
#     path('utilityinfo/', UtilityInfoView.as_view()),
#     path('UtilityDetails/<str:pk>/', UtilityDetails.as_view()),
# ]
