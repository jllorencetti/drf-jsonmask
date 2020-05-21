from __future__ import unicode_literals

from rest_framework import response, views as rest_views, viewsets

from drf_jsonmask.decorators import data_predicate
from drf_jsonmask.utils import apply_json_mask_from_request
from drf_jsonmask.views import OptimizedQuerySetMixin

from .models import Ticket

from .serializers import (  # CommentSerializer,; UserSerializer,
    TicketSerializer,
)


class OptimizedTicketViewSetMixin(OptimizedQuerySetMixin):
    @data_predicate('author')
    def load_author(self, queryset):
        return queryset.prefetch_related('author')

    @data_predicate('comments')
    def load_comments(self, queryset):
        return queryset.prefetch_related('comments')

    @data_predicate('comments.author')
    def load_comment_authors(self, queryset):
        return queryset.prefetch_related('comments__author')


class TicketViewSet(OptimizedTicketViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class RawViewSet(rest_views.APIView):

    def get(self, request, *args, **kwargs):
        data = {
            'a': 'test',
            'b': {
                'nested': 'test',
            },
            'c': {
                'a': {
                    'b': True,
                },
            },
            'd': {
                'a': {
                    'c': 'value',
                    'd': 'value',
                },
            },
        }
        data = apply_json_mask_from_request(data, request)
        return response.Response(data=data)
