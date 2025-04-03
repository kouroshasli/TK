"""
Copyright (c) 2024 KouroshAsli
All rights reserved.

This project is the intellectual property of KouroshAsli.
Unauthorized copying, modification, distribution, or use of this project,
via any medium, is strictly prohibited.

Contact: kouroshasli@proton.me
Telegram: @kouroshasli
GitHub: https://github.com/kouroshasli/TK
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Wrap the main URLs with i18n_patterns
urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    prefix_default_language=True
) 