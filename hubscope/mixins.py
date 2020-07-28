"""Mixins generales"""
from rest_framework import filters

from rest_framework import serializers
from rest_framework import pagination
from rest_framework.response import Response
import math
import ast
from rest_framework import  serializers


class datatableFilters(filters.SearchFilter, filters.OrderingFilter):
    """
    Filter using all the variables sent through a datatable_filters options
    """
    def filter_queryset(self, request, queryset, view):
        ''' Filters the by an specific field using as reference an specific field name'''
        queryset = super(datatableFilters, self).filter_queryset(request, queryset, view)

        datatable_filters = request.query_params.get('datatable_filters', None)
        if datatable_filters is None:
            return queryset

        filters = ast.literal_eval(datatable_filters)
        filters={k:v for k,v in filters.items() if v is not None or v != ''}

        OR_OPTION=filters.pop('OR_OPTION', None)
        if OR_OPTION is None:
            return queryset.filter(**filters).distinct()

        # import pdb; pdb.set_trace()
        queryelem = ''
        for (k,v) in filters.items():
            queryelem = queryelem + f' Q({k}={v})  |'
        queryelem = queryelem[:-1]
        newqueryset = f'queryset = queryset.filter({queryelem}).distinct()'
        exec(newqueryset)
        return queryset

class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def paginate_queryset(self, queryset, request, view=None):
        fields=request.query_params.get('ordering',None)
        if fields:
            queryset=queryset.order_by(*fields.split(','))

        response=super(CustomPagination, self).paginate_queryset(queryset, request, view)
        return response

    def get_ordering(self, request, queryset, view):
        response=super(CustomPagination, self).get_ordering(request, queryset, view)
        # import pdb; pdb.set_trace()
        return response

    def get_paginated_response(self, data):

        # import pdb; pdb.set_trace()

        last=math.ceil(self.page.paginator.count/self.page_size)

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'pagination':{
                'total': self.page.paginator.count,
                'per_page': self.page_size,
                'current_page': self.page.number,
                'last_page': last,
                'per_page': self.page_size,
                'next_page_url': self.get_next_link(),
                'prev_page_url': self.get_previous_link(),
                'from':self.page.start_index(),
                'to':self.page.end_index()
            },
            'results': data
        })


class DatatablesMixin(object):
    filter_backends = [datatableFilters]
    ordering_fields = '__all__'
    pagination_class = CustomPagination

    """docstring for DatatablesMixin"""
