from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, attrs):
        url = attrs.get(self.field)
        if url and "youtube.com" not in url:
            raise ValidationError("Можно прикреплять только ссылки на YouTube (youtube.com).")
