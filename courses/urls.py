from courses.apps import CoursesConfig
from courses.views import CourseViewSet
from rest_framework.routers import DefaultRouter

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r'сourses', CourseViewSet, basename='courses')

urlpatterns = router.urls
