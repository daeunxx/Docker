from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

import member.api

app_name='member'

router = routers.DefaultRouter()
router.register('members', member.api.MemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/doc', get_swagger_view(title='Rest API Document')),
    path('api/v1/', include((router.urls, 'member'), namespace='api'))
]
