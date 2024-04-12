from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from restaurant.items.api.views import CategoryViewset, ItemViewset
from restaurant.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("items", ItemViewset)
router.register("categories", CategoryViewset)


app_name = "api"
urlpatterns = router.urls
