from django.db import models

class ReportsManager(models.Manager):
    def by_company(self,company):
        self.filter(company=company)

    def by(self, **kwargs):
        ''' Optiene los reportes filtrados por 
        tiempo begin, end
        compañia
        o metrica
        '''
        

        for k,v in kwargs.items():
            if k == 'begin':
                query['begin__gte'] = v
            elif k == 'end':
                query['end__lte'] = v
            else:
                query[k] = v

        return self.filter(**query)