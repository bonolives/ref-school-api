#***
from django.urls import path
from . import views
#######################*******
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('staffs/', views.StaffView.as_view(), name='staff-list-create'),
    path('staffs/<int:pk>', views.SingleStaffView.as_view()),
    path('students/', views.StudentView.as_view()),
    path('students/<int:pk>', views.SingleStudentView.as_view()),
    path('courses/', views.CourseView.as_view()),
    path('courses/<int:pk>', views.SingleCourseView.as_view()),
    path('departments/', views.DepartmentView.as_view()),
    path('departments/<int:pk>', views.SingleDepartmentView.as_view()),
    path('clubs/<int:pk>', views.SingleClubView.as_view()),
    path('clubs/', views.ClubView.as_view()),
    #swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]