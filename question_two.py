def get_special_line(filename,openmode,defstr):
    list_str = []
    with open(filename,openmode) as f:
        for x in f.readlines():
        	if x.startswith(defstr):
        		list_str.append(x)	
        return list_str

print(get_special_line('exam_file', 'rt', 'Name'))
