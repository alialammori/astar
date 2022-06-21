from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import adjancedmap,heuristic
import queue

def index(request):
  nodes = adjancedmap.objects.all().values()
  hh = heuristic.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'mymembers': nodes,
    'heur':hh,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addher(request):
  template = loader.get_template('addher.html')
  return HttpResponse(template.render({}, request))

def fsp(request):
  template = loader.get_template('fsp.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['second']
  d=int(request.POST['cost'])
  row = adjancedmap(firstCity=x, secondCity=y,cost=d )
  row.save()
  return HttpResponseRedirect(reverse('home'))

def addrecordher(request):
  x = request.POST['city']
  d=float(request.POST['hval'])
  row = heuristic(city=x, Hval=d )
  row.save()
  return HttpResponseRedirect(reverse('home'))

def delete(request, id):
  member = adjancedmap.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('home'))

def deleteher(request, id):
  member = heuristic.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('home'))

def update(request, id):
  mymember = adjancedmap.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updateher(request, id):
  mymember = heuristic.objects.get(id=id)
  template = loader.get_template('updateher.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  x = request.POST['first']
  y = request.POST['second']
  d=float(request.POST['cost'])
  member = adjancedmap.objects.get(id=id)
  member.firstCity = x
  member.secondCity = y
  member.cost = d
  member.save()
  return HttpResponseRedirect(reverse('home'))

def updaterecordher(request, id):
  x = request.POST['city']

  d=float(request.POST['cost'])
  member = heuristic.objects.get(id=id)
  member.city = x

  member.Hval = d
  member.save()
  return HttpResponseRedirect(reverse('home'))

def fspastar(request):
    
    startNode=request.POST['src']
    goalNode=request.POST['dist']
    nodes = adjancedmap.objects.all().values()
    hh = heuristic.objects.all().values()
    graph=makegraph(nodes)
    
    heuristics=makeheur(hh)
    print(heuristics)
    path=Astar(startNode, heuristics, graph, goalNode)
    print(path)
   
    template = loader.get_template('result.html')
    context = {
      'path': path,
      
    }
    return HttpResponse(template.render(context, request))
def Astar(startNode, heuristics, graph, goalNode):
    priorityQueue = queue.PriorityQueue()
    distance = 0
    path = []
    print(heuristics[startNode])

    priorityQueue.put((heuristics[startNode] + distance, [startNode, 0]))

    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current[0])
        distance += int(current[1])

        if current[0] == goalNode:
            break

        priorityQueue = queue.PriorityQueue()

        for i in graph[current[0]]:
            if i[0] not in path:
                priorityQueue.put((heuristics[i[0]] + int(i[1]) + distance, i))

    return path

  
def makegraph(nodes):
    graph = {}
    node_val=[0]*3
    print(node_val)

    j=0
    for n in nodes:
        node_val[0] =n['firstCity']
        node_val[1]=n['secondCity']
        node_val[2]=n['cost']
        if node_val[0] in graph and node_val[1] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

        elif node_val[0] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            graph[node_val[1]] = [[node_val[0], node_val[2]]]

        elif node_val[1] in graph:
            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

            graph[node_val[0]] = [[node_val[1], node_val[2]]]

        else:
            graph[node_val[0]] = [[node_val[1], node_val[2]]]
            graph[node_val[1]] = [[node_val[0], node_val[2]]]
        
    return graph
def makeheur(hh):
    heir = {}

    j=0
    for n in hh:
       
        
         heir[n['city']]=n['Hval']
         
    return heir



