# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def find_color(adj,node_colors):
    return node_colors [adj]
	
def check_colored(adj,check_list):
    return check_list [adj]

def give_color(node,adj_list,check_list,node_colors):
    adj_nodes_colors = []
    avail_colors = [0,1,2,3,4,5,6,7,8,9]
    for adj in adj_list[node]:
	if(check_colored(adj,check_list)):
	    used_color = find_color(adj,node_colors)
	    adj_nodes_colors.append(used_color) 
    avail_color_set = set(avail_colors)
    colored_set = set(adj_nodes_colors)
    ok_colors = avail_color_set - colored_set
    ok_colors_list = list(ok_colors)
    return ok_colors_list [0]



#class Coloring:
@csrf_exempt
def posted(request):
    #print "aaaa"
   # if request.method == 'POST':
    adj_list=eval(request.POST.get('name'))
    print adj_list
    print type(adj_list)
    nodes = range(len(adj_list))
    check_list = []
    i = 0
    while(i < len(adj_list)) :
	check_list.append(0) 
	i += 1
    colors = {
		0 : "red",
		1 : "blue",
		2 : "green",
		3 : "yellow",
		4 : "orange",
		5 : "magenta",
		6 : "#00FF00",
		7 : "#33FFFF",
		8 : "black",
		9 : "pink"
	}
    node_colors = {
    }
    for node in nodes:
	node_colors [node] = give_color(node,adj_list,check_list,node_colors)
	check_list [node] = 1	
    value_color = node_colors.values()
	#self.response.out.write(value_color)
    return HttpResponse(simplejson.dumps(value_color), mimetype='application/json')
    #return render_to_response(value_color)
	#HttpResponse(value_color)
