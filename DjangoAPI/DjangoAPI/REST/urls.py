from rest_framework import routers

from REST.views import UserViewSet, GroupViewSet, DogViewSet

router = routers.DefaultRouter()

router.register("users", UserViewSet)
router.register("groups", GroupViewSet)

router.register("dogs", DogViewSet)