from django.urls import path

from user import views


urlpatterns = [
    path('create/parent/', views.ParentCreate.as_view(), name='create-parent'),
    path('create/student/', views.StudentCreate.as_view(), name='create-student'),
    path('create/teacher/', views.TeacherCreate.as_view(), name='create-teacher'),
    path('parent/<int:pk>/', views.ParentDetail.as_view(), name='detail-parent'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='detail-student'),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view(), name='detail-teacher'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
]

