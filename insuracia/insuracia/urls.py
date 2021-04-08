from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "INSURANCIA"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
