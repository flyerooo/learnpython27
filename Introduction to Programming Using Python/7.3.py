alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
alist.sort(key = lambda x: -x["age"])
print alist