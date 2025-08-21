from django.contrib import admin
from .models import Course, Lesson, Subscription

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    search_fields = ('name', 'description')
    list_filter = ('owner',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'owner')
    search_fields = ('name', 'description')
    list_filter = ('course', 'owner')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'created_at')
    list_filter = ('course', 'user')
