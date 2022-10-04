from django.urls import URLPattern, path
from . import views


urlpatterns=[
    path("",views.home,name="home"),
    path("tasks",views.tasks,name="tasks"),
    path("tasks/create",views.create_task,name="create_task"),
    path("tasks/detail/<int:task_id>/",views.task_detail,name="task_detail"),
    path("tasks/completed",views.task_completed,name="task_completed"),#mostrar tareas completadas
    path("tasks/detail/<int:task_id>/complete",views.complete_task,name="complete_task"),#marcar tarea como completada
    path("tasks/detail/<int:task_id>/delete",views.delete_task,name="delete_task"),
]