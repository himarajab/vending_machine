from django.contrib import admin
from django.urls import include, path
from users.api import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users-api/', include('users.api.urls', namespace='users-api'))
]


