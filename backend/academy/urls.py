from django.urls import path

from academy import views


urlpatterns = [
    path('', views.AcademyList.as_view(), name='list-create'),
    path('<int:pk>/', views.AcademyDetail.as_view(), name='detail'),
    path('<int:pk>/students/', views.AcademyStudents.as_view(), name='detail-students'),
    path('<int:pk>/review/', views.AcademyReview.as_view(), name='detail-review'),
]

