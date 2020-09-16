from termcolor import cprint
from statistics import mean


def procesing(key):
    """retona un callback de proceamisnto con base un nombre

    Args:
        key (Srt): Nombre del callback
    """    

    def Simple(metric_dict, metric_name):
        """procesamiento simple, toma una sola metrica y la suma como en un Reduce y retorna el valor total

        Args:
            metric_dict (dict): diccionario que contiene una lista de dias con los valores
            metric_name (Str): Nombre de la metrica

        Returns:
            Int: resultado de la suma de los valores del dictionario de metricas
        """        
        val = 0
        for day in metric_dict[ metric_name ]:
            val = val + day['value']
        return val
    
    def Acumulado(metric_dict, components):
        cname = components['value']
        dayslist= [d['value'] for d in metric_dict[ cname ] ]
        return sum(dayslist)   

    def Cociente(metric_dict, components):
        numerator_name = components['numerator']
        denominator_name = components['denominator']
        numerator_val = sum( [d['value'] for d in metric_dict[ numerator_name ] ])
        denominator_val = sum( [d['value'] for d in metric_dict[ denominator_name ] ])
        if denominator_val == 0:
            denominator_val=1
        return numerator_val/denominator_val
        

    def Estado(metric_dict, components):
        cname = components['value']
        dayslist= [d['value'] for d in metric_dict[ cname ] ]
        avg = mean(dayslist)
        return round(avg,2)

    def Porcentaje(metric_dict, components):
        return Cociente(metric_dict, components)*100
        

    def Producto(metric_dict, components):
        pass
        







    try:
        return locals()[key]
    except Exception as e:
        cprint(f'Callback {key} error', 'white','on_red')
        print(e)
        import pdb; pdb.set_trace()