from django.shortcuts import render, redirect
from .KM import *
client_num=-1
# Create your views here.
def index(request):
    global client_num
    if client_num==9:
        client_num=0
    else:
        client_num+=1
    return render(request,'KM_index.html',{'hh':"heading",'client_num':client_num})

def draw(request):
    global kmeans_array
    cn=int(request.POST['client_num'])
    try:
        data= to2Darray(request.POST['datapoint'])
        if(len(data)==0):
            return redirect("/")
        K=request.POST['K']
        kmeans_array[cn].set_init(int(K), data)
    except:
        pass
    
    try:
        if(request.POST['clear']=="yes"):
            return redirect("/")
        if(request.POST['random']=="yes"):
            kmeans_array[cn].random()
        else:
            kmeans_array[cn].step()
    except:
        pass
    ret=kmeans_array[cn].points_with_centroids()
    print("\nclient"+str(cn)+"\n"+str(ret)+"\n")
    return render(request,
        'KM_step.html',{'hh':"heading", 
        'inn':ret[0], 
        'centroid':ret[1],
        'client_num':cn}
        )