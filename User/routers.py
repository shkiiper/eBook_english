from rest_framework.routers import SimpleRouter
from .views import UserViewSet, NoteViewSet, LevelViewSet, TestTypeViewSet, \
    QuestionViewSet, TestingViewSet, DictionaryViewSet, ReviewViewSet
#routers в Django представляет набор инструментов, которые помогают автоматически создавать URL-маршруты для представлений на основе моделей (viewsets) в Django REST Framework.


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