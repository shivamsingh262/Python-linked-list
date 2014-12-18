# link list in python

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

head = Node(None)

def create_list(val):
    global head
    tmp = Node(val)
    if head.data == None:
        head = tmp
    else:
        q = head
        while q.next != None:
            q = q.next
        q.next = tmp

def print_list(ob):
    while ob.data != None:
        print ob.data
        ob = ob.next

def add_begin(val):
    global head
    tmp = Node(val)
    tmp.next = head
    head = tmp

def add_end(val):
    global head
    q = head
    tmp = Node(val)
    while q.next != None:
        q = q.next
    q.next = tmp

def delete(val):
    global head
    if head.data == val:
        head = head.next
    else:
        q = head
        while q.next.next != None:
            if q.next.data == val:
                tmp = q.next
                q.next = tmp.next
            q = q.next
        if q.next.data == val:
            q.next = None

def reverse():
    global head
    p1 = head
    p2 = head.next
    p3 = p2.next
    p1.next = None
    p2.next = p1
    while p3 != None:
        p1 = p2
        p2 = p3
        p3 = p3.next
        p2.next = p1
    head = p2

res = Node(None)
def sortedInsert(val):
    global res
    q = res
    tmp = Node(val)
    if res.data == None or res.data > val:
        tmp.next = res
        res = tmp
    else:
        while q.next!=None and q.next.data < val:
            q = q.next
        tmp.next = q.next
        q.next = tmp

def insertSort():
    global head,res
    q = head
    while q!=None:
        sortedInsert(q.data)
        q = q.next
    head = res

def remDuplicates():
    global head
    arr = []
    q = head
    p = q.next
    arr.append(q.data)
    while q.next != None:
        if p.data in arr:
            q.next = p.next
            p = p.next
        else:
            arr.append(p.data)
            q = p;
            p = p.next;
                    
ll = [1,2,6,6,4,5]
for item in ll:
    create_list(item)

add_begin(7)
add_end(8)
delete(8)
#reverse()
insertSort()
remDuplicates()
print_list(head)
