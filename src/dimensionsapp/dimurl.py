from django.urls import path
from dimensionsapp.views import AuthorDetailView, SerieDetailView, JenreDetailView, PublishingHouseDetailView \
    , FormatBookDetailView, BindingDetailView, AgeRestrictionDetailView

urlpatterns = [
    path('author/<int:pk>/', AuthorDetailView.as_view()),
    path('serie/<int:pk>/', SerieDetailView.as_view()),
    path('jenre/<int:pk>/', JenreDetailView.as_view()),
    path('publishing/<int:pk>/', PublishingHouseDetailView.as_view()),
    path('format/<int:pk>/', FormatBookDetailView.as_view()),
    path('binding/<int:pk>/', BindingDetailView.as_view()),
    path('agerestriction/<int:pk>/', AgeRestrictionDetailView.as_view()),
]
