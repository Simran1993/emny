"""
URL configuration for expense_tracker project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/transactions/', include('apps.transactions.urls')),
    path('api/categories/', include('apps.categories.urls')),
    path('api/budgets/', include('apps.budgets.urls')),
    path('api/subscriptions/', include('apps.subscriptions.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
    path('api/integrations/', include('apps.integrations.urls')),
    path('api/integrations/plaid/', include('apps.integrations.plaid.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
