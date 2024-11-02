from django.urls import path

from .admin_views import BundledProductAutocompleteView
from .views import ProductSkuSearchView, ProductView, SupplierProductsView, SupplierView


urlpatterns = [
    path(
        'product',
        ProductView.as_view(),
        name='product',
    ),
    path(
        'suppliers',
        SupplierView.as_view(),
        name='suppliers',
    ),
    path(
        'supplier-products',
        SupplierProductsView.as_view(),
        name='supplier-products',
    ),
    path(
        'product-sku-search',
        ProductSkuSearchView.as_view(),
        name='product-sku-search',
    ),
    path(
        'bundled-product-autocomplete',
        BundledProductAutocompleteView.as_view(),
        name='bundled-product-autocomplete',
    ),
]
