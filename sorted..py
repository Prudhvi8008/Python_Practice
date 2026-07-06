a=['1','2333','333']
b=['ss','ee','eeeeee']
print(sorted(a,key=lambda x:len(x),reverse=True))
print(sorted(b))
d={"sai":12,"sivan":23}
print(sorted(d.items(),key=lambda x:x[1]))
print(sorted(d,key=lambda x:d[x]))
print(sorted("prudhvi"))
print("".join(sorted("prudhvi")))
