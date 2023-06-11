from django.contrib import admin
from django.urls import path, include
from polls.views import (posts,
                         profile,
                         add_category_view,
                         add_post_view,
                         AddCategoryView,
                         AddPostView,
                         PostList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('accounts/', include('accounts.urls'))
]