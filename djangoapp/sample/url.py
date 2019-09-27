from django.conf.urls import url
from rest_framework import routers
from sample.views import StudentViewSet, UniversityViewSet

sample = routers.DefaultRouter()
sample.register(r'students', StudentViewSet, 'students')
sample.register(r'universities', UniversityViewSet, 'universities')


# urlpatterns = sample.urls


