from fileinput import close


def get_first_and_last_numbers(s):
    stack=[]
    for c in s:
       asciiVal=ord(c)
       if (asciiVal>=48 and asciiVal<=57):
           stack.append(c)
    return int(stack[0]+stack.pop())


def get_first_and_last_number_index(s):
    stack=[]
    index=0
    for c in s:
        asciiVal=ord(c)
        if (asciiVal>=48 and asciiVal<=57):
            stack.append((c,index))
        index=index+1
    if len(stack)>0:
        return (stack[0],stack.pop())
    else:
        return (('0',len(s)),('0',0))

def get_first_and_last_numbers_ex(s):

    lookUp=["one","two", "three","four","five","six","seven","eight","nine"]

    literal_number_results=get_first_and_last_number_index(s)

    first_num=int(literal_number_results[0][0])
    first_num_index=literal_number_results[0][1]

    last_num=int(literal_number_results[1][0])
    last_num_index=literal_number_results[1][1]
    #now check the strings before and after the indexes for 'new' numbers

    val=1
    for num in lookUp:
        
        temp_first_index=s.find(num)
        temp_last_index=s.find(num)

        if (temp_first_index>-1 and temp_first_index<first_num_index):
            first_num=val
            first_num_index=temp_first_index
        

        if (temp_last_index>-1):
            
             #maximise temp_last_index for this number
            max_index=max([i for i in range(len(s)) if s.startswith(num,i)])
            if (max_index>last_num_index):
                last_num_index=max_index
                last_num=val

        val=val+1
    
    return  int(str(first_num)+str(last_num))


def part_one():
    sum=0
    f=open("D:\Projects\AOC2023\Day01\input.txt","r")
    for line in f:
       sum += get_first_and_last_numbers(line)
    f.close()
    return sum

def part_two():
    sum=0
    f=open("D:\Projects\AOC2023\Day01\input.txt","r")
    for line in f:
        val_new= get_first_and_last_numbers_ex(line)
        sum =sum + val_new
       
    f.close()
    return sum