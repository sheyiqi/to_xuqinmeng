t_num=0
s_num=0
a=0
f=open("data.txt","r")
for word in f.read().split('\t'):
    if word[0]=="T":
        if a!=1:
            a=1
            t_num+=1
    if word[0]=="S":
        if a!=0:
            a=0
            s_num+=1
ts= t_num+s_num
t = t_num / ts
s = s_num / ts
print ("T:%s  %f" % (t_num,t))
print ("S:%s  %f" % (s_num,s))
print ("T_TransformTo_S:%s" % s_num)
f.close()
