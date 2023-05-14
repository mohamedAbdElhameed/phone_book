from django.urls import path

from .views import ContactCreateView, ContactDetailView, ContactListView, PhoneNumberCreateView

app_name = "contacts"

urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create/", ContactCreateView.as_view(), name="contact_create"),
    path("<int:pk>/", ContactDetailView.as_view(), name="contact_detail"),
    path("<int:pk>/phone_number/create/", PhoneNumberCreateView.as_view(), name="phone_number_create"),
]
