
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings # to import static in deployment
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # djoser authentication conf
    path('auth/', include('djoser.urls')),

    # jwt custom token
    path('auth/', include('accounts.urls')),

    # # # jwt default token
    # path('auth/', include('djoser.urls.jwt')),

    # google OAuth2 conf
    path('auth/', include('djoser.social.urls'))
]

urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # to import static in deployment
