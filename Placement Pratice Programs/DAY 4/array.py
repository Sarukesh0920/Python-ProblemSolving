a=[2,3,4,5,6,7]
b=[1,2,3,4,5,6]
n=len(a)
add_array=[]
for i in range(n):
    add_array.append(a[i]+b[i])
print("ADD Array:",add_array)

sub_array=[]
for i in range(n):
    sub_array.append(a[i]-b[i])
print("Sub Array:",sub_array)

multi_array=[]
for i in range(n):
    multi_array.append(a[i]*b[i])
print("Multi Array:",multi_array)

div_array=[]
for i in range(n):
    if b[i]!=0:
        div_array.append(a[i]/b[i])
    else:
        div_array.append(none)
print("Div Array",div_array)