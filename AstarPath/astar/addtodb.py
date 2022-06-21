from models import adjancedmap,heuristic


with open("romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = float(line[1].strip())
           
            member = heuristic(city=node, Hval=sld)
            member.save()

file = open("romania.txt", 'r')
for string in file:
        line = string.split(',')
        ct1 = line[0]
        ct2 = line[1]
        dist = float(line[2])
        member = heuristic(firstCity=ct1, secondCity=ct2,cost=dist )
        member.save()
       
