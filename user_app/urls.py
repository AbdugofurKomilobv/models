from django.urls import path
from .views import add_student, delete_user, edit_user, user_login, admin_panel, teacher_panel, student_panel,add_teacher

urlpatterns = [
    path("", user_login, name="login"),
    path("admin-panel/", admin_panel, name="admin_panel"),
    path("teacher-panel/", teacher_panel, name="teacher_panel"),
    path("student-panel/", student_panel, name="student_panel"),

    path('add-student/', add_student, name='add_student'),
    path('add-teacher/', add_teacher, name='add_teacher'),
     path('edit-user/<int:user_id>/', edit_user, name='edit_user'),
      path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
]
