from django.apps import AppConfig


class HelloConfig(AppConfig):
    name = 'hello'

    def ready(self):
        import hello.signals