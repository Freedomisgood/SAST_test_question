operating_system_dict = {
    'Debian': 1993,
    'Red Hat Enterprise Linux': 2003,
    'Windows': 1985,
    'Mac OS': 1984,
    'Windows7': 2009,
}

def get_os(dicts,year):
    list1 = [x for x in dicts.values() if x>year]
    list2=[]
    for x,y in dicts.items():
        if y in list1:
            list2.append(x)
    list2.sort(reverse=1)
    return list2

get_os(operating_system_dict,1990)