from rest_framework.routers import SimpleRouter
from hubscope.reports import views


router = SimpleRouter()

router.register(r'company', views.CompanyViewSet)
router.register(r'asignment', views.AsignmentViewSet)
router.register(r'indicator', views.IndicatorViewSet)
router.register(r'report', views.ReportViewSet)
router.register(r'metric', views.MetricViewSet)

urlpatterns = router.urls
