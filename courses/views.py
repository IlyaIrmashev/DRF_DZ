from django.db.models import Count
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from courses.models import Course, Lesson, Payment
from courses.paginators import CoursesPaginator
from courses.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, CourseListSerializer, \
    LessonDetailSerializer, PaymentListSerializer, SubscriptionSerializer, PaymentRetrieveSerializer, \
    PaymentCreateSerializer, PaymentSerializer
from rest_framework import viewsets, generics

from courses.tasks import send_mail_about_update
from users.permissions import IsBuyer, IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseDetailSerializer
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]
    queryset = Course.objects.annotate(lessons_count=Count('lesson'))
    default_serializer = CourseSerializer
    pagination_class = CoursesPaginator
    serializers = {
        'list': CourseListSerializer,
        'retrieve': CourseDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.object.all()
    serializer_class = CourseSerializer

    def perform_update(self, serializer):
        serializer.save()
        email = serializer.context['request'].user.email
        send_mail_about_update.delay(email)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CoursesPaginator
    permission_classes = [IsAuthenticated]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('date_payment',)
    permission_classes = [IsAuthenticated]
    pagination_class = CoursesPaginator


class PaymentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentRetrieveSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer, IsModerator]


class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class PaymentDeleteAPIView(generics.DestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()
