from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from materials.models import Subscription, Lesson, Course
from unittest.mock import ANY


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@example.com")
        self.other_user = User.objects.create(email="other@example.com")
        self.moderator = User.objects.create(email="moderator@example.com", is_staff=True)
        self.course = Course.objects.create(name="Курс", description="Описание курса", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="Урок",
            description="Описание урока",
            url="https://youtube.com/video",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse("materials:lessons_create")
        data = {
            "name": "Урок тест",
            "description": "Описание тестового урока",
            "url": "https://youtube.com/video1",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_retrieve(self):
        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_list(self):
        url = reverse("materials:lessons_list")
        response = self.client.get(url)
        data = response.json()

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "course": self.course.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "preview": None,
                    "url": self.lesson.url,
                    "owner": self.lesson.owner.id,
                    "last_notification_sent": None,
                    "updated_at": ANY,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    # def test_lesson_update(self):
    #     url = reverse("materials:lessons_update", args=(self.lesson.pk,))
    #     data = {"name": "Тест урока", "description": "Описание теста урока"}
    #     response = self.client.patch(url, data)
    #     data = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(data.get("name"), "Тест урока")

    def test_lesson_destroy(self):
        url = reverse("materials:lessons_destroy", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_destroy_lesson_not_owner(self):
        self.client.force_authenticate(user=self.other_user)
        url = reverse("materials:lessons_destroy", args=[self.lesson.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Lesson.objects.filter(pk=self.lesson.pk).exists())

    def test_destroy_lesson_by_moderator(self):
        self.client.force_authenticate(user=self.moderator)
        url = reverse("materials:lessons_destroy", args=[self.lesson.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Lesson.objects.filter(pk=self.lesson.pk).exists())


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user1@example.com")
        self.moderator = User.objects.create(email="moderator1@example.com", is_staff=True)
        self.course = Course.objects.create(name="Курс", description="Описание курса", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_create(self):
        url = reverse("materials:course-list")
        data = {"name": "Курс тест", "description": "Описание тестового курса"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_retrieve(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)

    def test_course_list(self):
        url = reverse("materials:course-list")
        response = self.client.get(url)
        data = response.json()
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "name": self.course.name,
                    "preview": None,
                    "description": self.course.description,
                    "owner": self.course.owner.pk,
                    "last_notification_sent": None,
                    "updated_at": ANY,
                }
            ],
        }
        self.assertEqual(data, result)

    # def test_course_update(self):
    #     url = reverse("materials:course-detail", args=(self.course.pk,))
    #     data = {"name": "Курс тест", "description": "Описание тестового курса"}
    #     response = self.client.patch(url, data)
    #     data = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(data.get("name"), "Курс тест")

    def test_course_delete(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user2@example.com")
        self.course = Course.objects.create(name="Курс подписки", description="Описание", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscribe_unsubscribe(self):
        url = reverse("materials:subscription-toggle")
        print(url)
        response = self.client.post(url, {"course_id": self.course.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())
        self.assertEqual(response.json()["message"], "Подписка добавлена")

        response = self.client.post(url, {"course_id": self.course.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())
        self.assertEqual(response.json()["message"], "Подписка удалена")
