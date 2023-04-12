from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

import member.api

app_name='member'

router = routers.DefaultRouter()
router.register('members', member.api.MemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
 ]
