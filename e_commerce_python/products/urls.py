from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryRetrieveUpdateDestroyView

urlpatterns = [
    path('categories', CategoryListView.as_view(), name='category_list'),
    path('admin/categories', CategoryCreateView.as_view(), name='category_create'),
    path('admin/categories/<int:pk>', CategoryRetrieveUpdateDestroyView.as_view(), name='category_retrieve_update_destroy'),
]