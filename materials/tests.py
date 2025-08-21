from rest_framework.test import APITestCase
from users.models import User
from materials.models import Subscription, Lesson, Course


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='user@example.com')
        self.moderator = User.objects.create_user(email='moderator@example.com', is_staff=True)
        self.course = Course.objects.create(name='Курс', description='Описание курса', owner=self.user)
        self.lesson = Lesson.objects.create(name='Урок', description='Описание урока', url="https://example.com/video", course=self.course, owner=self.user)


    def test_lesson_create(self):
        pass

    def test_lesson_retrieve(self):
        pass

    def test_lesson_list(self):
        pass

    def test_lesson_update(self):
        pass

    def test_lesson_destroy(self):
        pass


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='user1@example.com')
        self.moderator = User.objects.create_user(email='moderator1@example.com', is_staff=True)
        self.course = Course.objects.create(name='Курс', description='Описание курса', owner=self.user)

    def test_course_create(self):
        pass

    def test_course_retrieve(self):
        pass

    def test_course_list(self):
        pass

    def test_course_update(self):
        pass

    def test_course_destroy(self):
        pass


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='user2@example.com')
        self.course = Course.objects.create(name='Курс подписки', description='Описание', owner=self.user)

    def test_subscribe_unsubscribe(self):
        pass