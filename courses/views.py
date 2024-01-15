from courses.models import Course
from courses.serializers import CourseSerializer
from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

