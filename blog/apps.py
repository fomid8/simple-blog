from django.apps import AppConfig
from django.conf import settings
from elasticsearch_dsl import connections


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

connections.create_connection(
    alias="default",
    hosts=settings.ELASTICSEARCH_DSL["default"]["hosts"],
    http_auth=settings.ELASTICSEARCH_DSL["default"].get("http_auth"),
    ca_certs=settings.ELASTICSEARCH_DSL["default"].get("ca_certs"),
)