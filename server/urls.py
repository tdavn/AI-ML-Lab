"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

import homepage.views
# import predict.views

urlpatterns = [
    path("", homepage.views.index, name="index"),
    path("demo/", include('homepage.urls')),
    # path('model/', include('predict.urls')),
    # path('classify/', predict.views.predict_chances, name='submit_prediction'),
    # path('results/', predict.views.view_results, name='results'),
    path("db/", homepage.views.db, name="db"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += endpoints_urlpatterns
