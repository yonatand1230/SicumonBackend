from decimal import Decimal

class Utils:
    def replace_decimals(obj):
        keys = list(obj)
        for k in keys:
            if type(obj[k])==Decimal: obj[k]=int(obj[k])
        return obj