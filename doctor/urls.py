from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('specialization', views.SpecializationViewSet)
router.register('designation', views.DesignationViewSet)
router.register('available_time', views.AvailableTimeViewSet)
router.register('list', views.DoctorViewSet)
router.register('Review', views.ReviewViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
