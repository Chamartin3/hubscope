
class CompanyViewSet(DatatablesMixin, ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    page_size = 3


    # def list(self, request, *args, **kwargs):
    #     import pdb; pdb.set_trace()