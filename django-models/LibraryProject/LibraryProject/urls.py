from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
    # You can also add a root path if desired:
    # path('', include('relationship_app.urls')),
]
