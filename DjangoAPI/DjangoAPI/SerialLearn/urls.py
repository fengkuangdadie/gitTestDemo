from rest_framework import routers

from SerialLearn.views import BookViewSet

router = routers.DefaultRouter()

router.register("books", BookViewSet)