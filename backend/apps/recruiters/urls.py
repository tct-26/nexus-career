from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CompanyProfileView, RecruiterOpportunityViewSet
from .alumni_views import CompanyVerifiedAlumniListView

router = DefaultRouter()
router.register(
    "opportunities",
    RecruiterOpportunityViewSet,
    basename="recruiter-opportunity",
)

urlpatterns = [
    path("companies/<int:company_id>/alumni/", CompanyVerifiedAlumniListView.as_view(), name="company-verified-alumni"),
    path("company/", CompanyProfileView.as_view(), name="recruiter-company-profile"),
    path("", include(router.urls)),
]
