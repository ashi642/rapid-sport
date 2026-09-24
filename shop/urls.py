from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "shop/",
        views.shop,
        name="shop"
    ),

    path(
        "product/<int:id>/",
        views.product_detail,
        name="product_detail"
    ),

    path(
        "custom-jersey/",
        views.custom_jersey,
        name="custom_jersey"
    ),

    path(
        "cart/",
        views.cart,
        name="cart"
    ),

    path(
        "cart/add/<int:id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    path(
        "cart/remove/<int:id>/",
        views.remove_from_cart,
        name="remove_from_cart"
    ),

    path(
        "cart/update/",
        views.update_cart,
        name="update_cart"
    ),

    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),

    path(
        "order-success/<int:id>/",
        views.order_success,
        name="order_success"
    ),

    path(
        "dashboard/login/",
        views.dashboard_login,
        name="dashboard_login"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "dashboard/logout/",
        views.dashboard_logout,
        name="dashboard_logout"
    ),
]