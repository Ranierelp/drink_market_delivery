from rest_framework.routers import DefaultRouter

from user.views.api import CustomerViewSet

router = DefaultRouter()
router.register('customer', CustomerViewSet)