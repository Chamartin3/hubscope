from termcolor import cprint

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






    try:
        return locals()[key]
    except Exception as e:
        cprint(f'Callback {key} error', 'white','on_red')
        print(e)
        import pdb; pdb.set_trace()