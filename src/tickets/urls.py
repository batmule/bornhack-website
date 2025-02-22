from django.urls import path

from .views import shop_ticket_list_view
from .views import ShopTicketDetailView
from .views import ShopTicketDownloadView

app_name = "tickets"

urlpatterns = [
    path("", shop_ticket_list_view, name="shopticket_list"),
    path(
        "<uuid:pk>/download/",
        ShopTicketDownloadView.as_view(),
        name="shopticket_download",
    ),
    path("<uuid:pk>/edit/", ShopTicketDetailView.as_view(), name="shopticket_edit"),
]
