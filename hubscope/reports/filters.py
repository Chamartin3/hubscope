from hubscope.mixins import DatatablesMixin, datatableFilters
from django.db.models import Q
from django.utils.timezone import localdate
from rest_framework import filters
import ast
from termcolor import  cprint


from hubscope.reports.models import Report
# @property
# def status(self):

#   if not self.editable:
#       return 'cerrada'
# 
#   if self.value is not None:
#         return 'entregada'
#   
#   waiting = (self.end -localdate()).days    
#   if(waiting > -1):
#         return 'esperando'
#   
# is_open = (self.deadline - localdate()).days
#   if(is_open>-1):
#         return 'abierta'
#   
# return 'atrasada'

# STATUSES = {
#     'cerrada': lambda qs : qs.filter( editable=False ),
#     'entregada': lambda qs : qs.filter( ~Q(num_value=None) ),
#     'esperando': lambda qs : qs.filter( end__lt=localdate() ),
#     'abierta': lambda qs : qs.filter( deadline__lt=localdate() ),
#     'atrasada': lambda qs : qs.filter( deadline__gt=localdate() )
# }

class reportFilters(datatableFilters):
    # def filter_by_status(self, status):
    
    #     if status == 'cerrada':
    #         return self.base_queryset.filter( editable=False )
        
    #     qs = self.base_queryset.filter(editable=True)
    #     if status == 'entregada':
    #         return qs.filter(~Q(num_value=None))
        
    #     qs = qs.filter(num_value=None)
    #     if status == 'esperando':
    #         return qs.filter(end__gte=localdate() )
            
    #     qs = qs.filter(end__lt=localdate())
    #     if status == 'abierta':
    #         return qs.filter(deadline__gt=localdate() )
        
    #     if status == 'atrasada':
    #         return qs.filter(deadline__lt=localdate() )

        
    #     print( f'{status} is not a recogniced status for Reports' )  
    #     import pdb; pdb.set_trace()
    #     raise 


    def filter_queryset(self, request, queryset, view):
        '''
        Filters the by an specific field using as reference an specific field name
        '''
        cprint('filtering', 'cyan')
        self.base_queryset = queryset
        
        queryset = Report.objects.filter(end=None, metric__tipo='E').union(queryset)
        
        property_filters = request.query_params.get('property_filters', None)
        if property_filters is None:
            return queryset
        property_filters = ast.literal_eval(property_filters)
        status = property_filters.get('status', None)
        if status:
            try:
                queryset = Report.objects.by_status(status).intersection(queryset)
            except Exception as e:
                cprint(e,'red')
                import pdb; pdb.set_trace()
            # queryset = self.filter_by_status(status)

        # import pdb; pdb.set_trace()

        queryset = super(reportFilters, self).filter_queryset(request, queryset, view)

        return queryset.order_by('-begin')


class reportFiltersMixin(DatatablesMixin):
    filter_backends = [ datatableFilters, reportFilters ]
    """docstring for DatatablesMixin"""
