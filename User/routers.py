from rest_framework.routers import SimpleRouter

from testing.views import CompletedTestViewSet
from .views import UserViewSet, TokenObtainPairView, NoteViewSet, DictionaryViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'dictionaries', DictionaryViewSet, basename="dictionaries")
router.register(r'completedtests', CompletedTestViewSet, basename="test")
urlpatterns = [
]