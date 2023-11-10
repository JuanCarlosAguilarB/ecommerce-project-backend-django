from django.urls import path

from .views import ListCategoriesView, ListProductsByCategoryView

urlpatterns = [
    path('categories/', ListCategoriesView.as_view()),
    path('categories/<int:category_id>/products/', ListProductsByCategoryView.as_view()),
]
