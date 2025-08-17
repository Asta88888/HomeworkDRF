from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lesson_count', 'lessons']


