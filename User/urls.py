from django.urls import path, include
from .routers import router
from .views import TokenObtainPairView

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]