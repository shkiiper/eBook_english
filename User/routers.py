from rest_framework.routers import SimpleRouter
from .views import UserViewSet, NoteViewSet, LevelViewSet, TestTypeViewSet, \
    QuestionViewSet, TestingViewSet, DictionaryViewSet, ReviewViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')
router.register(r'notes', NoteViewSet, basename='note')
router.register('levels', LevelViewSet)
router.register('testtypes', TestTypeViewSet)
router.register('questions', QuestionViewSet)
router.register('testing', TestingViewSet)
router.register('Dictionary', DictionaryViewSet)
router.register(r'reviews', ReviewViewSet)
urlpatterns = [
]