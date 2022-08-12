from django.urls import path

from .views import api, template


urlpatterns = [
    path("", template.BlogListView.as_view(), name="blogs"),
    path("<slug:slug>/", template.BlogDetailView.as_view(), name="blog"),
]
