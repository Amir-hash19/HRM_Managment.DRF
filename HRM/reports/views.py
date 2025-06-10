from rest_framework.generics import CreateAPIView, ListAPIView
from accounts.permissions import IsManager
from rest_framework.permissions import IsAuthenticated
from .models import ReportLog
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .serializers import ReportLogSerializer
from django.db.models import F
from django.contrib.postgres.search import TrigramSimilarity



class ReportLogPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 90




class ListReportLogView(ListAPIView):
    permission_classes = [IsAuthenticated, IsManager]
    serializer_class = ReportLogSerializer
    pagination_class = ReportLogPagination

    
    def get_queryset(self):
        search_query = self.request.query_params.get('search')
        qs = ReportLog.objects.select_related()

        if search_query:
            qs = qs.annotate(
                similarity = TrigramSimilarity('title', search_query)

            ).filter(similarity__gt=0.3).order_by("-similarity")

        return qs    
        





