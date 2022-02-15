from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    BaseView,
    ArtistDetailView,
    AlbumDetailView,
    RegistrationView,
    LoginView,
    AccountView,
    CartView,
    DeleteFromCartView,
    AddToCartView,
    ChangeQTYView,
    AddToWishlist,
)

urlpatterns = [
    # endpoint-ы для корзины
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('cart/', CartView.as_view(), name='cart'),

    # общие
    path('', BaseView.as_view(), name='base'),
    path('account/', AccountView.as_view(), name='account'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('add-to-wishlist/<int:album_id>/', AddToWishlist.as_view(), name='add_to_wishlist'),
    path('<str:artist_slug>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('<str:artist_slug>/<str:album_slug>/', AlbumDetailView.as_view(), name='album_detail'),

]

