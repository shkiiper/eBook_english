from django.urls import path, include
from .routers import router
from .views import TokenObtainPairView, UpdateUserAnswerAPIView

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('testing/<int:pk>/update_user_answer/', UpdateUserAnswerAPIView.as_view(), name='update-user-answer'),
]