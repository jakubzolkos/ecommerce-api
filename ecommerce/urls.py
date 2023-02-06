from django.contrib import admin
from django.urls import path

from ecommerce.drf.views import (
    CategoryList,
    ProductByCategory,
    ProductInventoryByWebId,
)
from ecommerce.search.views import SearchProductInventory

urlpatterns = [
    # Admin login
    path("admin/", admin.site.urls),
    # Default view, set to category list
    path("", CategoryList.as_view()),
    # Category list
    path("api/inventory/category/all/", CategoryList.as_view()),
    # Search items with a given category
    path("api/inventory/products/category/<str:query>/", ProductByCategory.as_view()),
    # Find items with a given web id e.g. the same product but different sizes, colors
    path("api/inventory/<int:query>/", ProductInventoryByWebId.as_view()),
    # Find all products related to query string
    path("api/search/<str:query>/", SearchProductInventory.as_view()),
]
