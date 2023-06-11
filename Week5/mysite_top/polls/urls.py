from django.urls import path
from polls.views import (posts,
                         profile,
                         add_category_view,
                         add_post_view,
                         AddCategoryView,
                         PostList,
                         manage_categories)

urlpatterns = [
    # path('posts/', posts, name='posts'),
    path('posts/', PostList.as_view(), name='posts'),
    path('profile/', profile),
    # path('add-category/', add_category_view, name='add-category'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('add-post/', add_post_view, name='add-post'),
    path('manage-categories/', manage_categories)
]