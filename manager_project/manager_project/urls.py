# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url

import manager.views as manager_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^worker_list/', manager_view.WorkerListView.as_view())  # URLとViewを組み合わせる！
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]