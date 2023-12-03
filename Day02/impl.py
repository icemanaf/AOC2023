#returns true if one of the items in tuple a is greater than or equal to b's items
def greater_than(a,b):
    return (a[0]>b[0] or a[1]>b[1] or a[2]>b[2])

#given a string like "1 red,6 blue,3 green create an rgb tuple"
def create_rgb(s):
    dict ={"red":0,"green":0,"blue":0}

    rgbs=[x.strip() for x in s.split(',')]
    
    for x in rgbs:
        item=x.split(' ')
        dict[item[1]]=item[0]
    return (int(dict["red"]),int(dict["green"]),int(dict["blue"]))


def part_one():
    sum=0
    f=open("D:\Projects\AOC2023\Day02\input.txt","r")

    #current bag items
    current_rgb=(12,13,14)

    for line in f:
        valid=True
        items=line.split(':')
        game=int((items[0])[4:])
        
        iterations=items[1].split(';')
        for iteration in iterations:
            rgb=create_rgb(iteration)
            if (greater_than(rgb,current_rgb)):
                valid=False
                break
        if valid:
            sum=sum+game

    f.close()
    return sum


def part_two():
    sum=0
    f=open("D:\Projects\AOC2023\Day02\input.txt","r")

    #current bag items
    current_rgb=(12,13,14)

    for line in f:
       
        items=line.split(':')
      
        collection=[]

        iterations=items[1].split(';')
        for iteration in iterations:
            rgb=create_rgb(iteration)
            collection.append(rgb)
        
        r_min=max([x[0] for x in collection])
        g_min=max([x[1] for x in collection])
        b_min=max([x[2] for x in collection])
        sum=sum+ (r_min*g_min*b_min)

    f.close()
    return sum

