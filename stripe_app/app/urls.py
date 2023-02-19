from django.urls import path

from .views import (CancelView, CreateCheckoutSessionView, HomePageView,
                    ItemPageView, SuccessView)

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('', HomePageView.as_view(), name='home_page'),
    path('item/<int:pk>', ItemPageView.as_view(), name='item'),
    path(
        'buy/<int:pk>/',
        CreateCheckoutSessionView.as_view(),
        name='create-checkout-session'
    )
]
