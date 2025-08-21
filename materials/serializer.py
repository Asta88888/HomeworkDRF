from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.models import Course, Lesson, Subscription
from materials.validators import UrlValidator


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="url")]


class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_lesson_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lesson_count', 'lessons', 'is_subscribed']

    def get_is_subscribed(self, course):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return Subscription.objects.filter(user=user, course=course).exists()
