from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.permissions import IsAdminUser
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
        openapi.Info(
            title='Hakwon API',
            default_version='v0.0.1',
            description='API for Hakwon App',
            contact=openapi.Contact(email='podobongbong@kakao.com'),
        ),
        public=True,
        permission_classes=(IsAdminUser,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('academy/', include(('academy.urls', 'academy'), namespace='academy')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

