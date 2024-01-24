from rest_framework import serializers


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('video'):
            if 'www.youtube.com' not in value.get('video'):
                raise serializers.ValidationError('Ссылки еа сторонние ресурсы запрещены, кроме YouTube')
