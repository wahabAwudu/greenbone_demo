from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .api_router import CustomDefaultRouter

from computers.views import ComputerViewSet


router = CustomDefaultRouter()
router.register("computers", ComputerViewSet, basename="computers")


# Swagger documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="GreenBone API",
        default_version='v1',
        description="GreenBone Demo Documentation",
        terms_of_service="#",
        contact=openapi.Contact(email="contact@greenbone.net"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include(router.urls)),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "GreenBone Super Admin"
admin.site.site_title = "GreenBone"
admin.site.index_title = "GreenBone Super Admin"
