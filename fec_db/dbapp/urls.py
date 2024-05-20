from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('form/', views.form_view, name='form_view'),
    path('success/', views.success_view, name='success_view'),
    path('redirect_to_form/', views.redirect_to_form, name='redirect_to_form'),
    path('list/', views.member_list, name='member_list'),  # URL for the list view
    path('edit/<int:pk>/', views.edit_member, name='edit_member'),  # URL for the edit view
    path('confirm_delete/', views.confirm_delete, name='confirm_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

