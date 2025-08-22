from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from materials.models import Subscription, Lesson, Course


# class LessonTestCase(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create(email='user@example.com')
#         self.moderator = User.objects.create(email='moderator@example.com', is_staff=True)
#         self.course = Course.objects.create(name='Курс', description='Описание курса', owner=self.user)
#         self.lesson = Lesson.objects.create(name='Урок', description='Описание урока', url="https://example.com/video", course=self.course, owner=self.user)
#
#
#     def test_lesson_create(self):
#         pass
#
#     def test_lesson_retrieve(self):
#         pass
#
#     def test_lesson_list(self):
#         pass
#
#     def test_lesson_update(self):
#         pass
#
#     def test_lesson_destroy(self):
#         pass


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='user1@example.com')
        self.moderator = User.objects.create(email='moderator1@example.com', is_staff=True)
        self.course = Course.objects.create(name='Курс', description='Описание курса', owner=self.user)
        self.client.force_authenticate(user=self.user)


    def test_course_create(self):
        url = reverse("materials:course-list")
        data = {
            "name": "Курс тест",
            "description": "Описание тестового курса"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_retrieve(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.course.name
        )

    def test_course_list(self):
        url = reverse("materials:course-list")
        response = self.client.get(url)
        data = response.json()
        # print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = {
            'count': 1, 'next': None, 'previous': None, 'results':
                [
                    {'id': self.course.pk,
                     'name': self.course.name,
                     'preview': None,
                     'description':
                         self.course.description,
                     'owner': self.course.owner.pk
                     }
                ]
        }
        self.assertEqual(
            data, result
        )


    def test_course_update(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {
            "name": "Курс тест",
            "description": "Описание тестового курса"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Курс тест"
        )

    def test_course_delete(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )


# class SubscriptionTestCase(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create_user(email='user2@example.com')
#         self.course = Course.objects.create(name='Курс подписки', description='Описание', owner=self.user)
#
#     def test_subscribe_unsubscribe(self):
#         pass