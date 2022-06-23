todo = []

with open(r'todo.txt', 'r') as fp:
    for line in fp:
        x = line[:-1]
        todo.append(x)
    print(todo)

def add(txt):
    todo.append(txt)
    with open(r'todo.txt', 'w') as fp:
        for item in todo:
            fp.write("%s\n" % item)

def remove(txt):
    try:
        todo.remove(txt)
        with open(r'todo.txt', 'w') as fp:
            for item in todo:
                fp.write("%s\n" % item)
        return "OK"
    except ValueError:
        return "Lista nie zawiera %s" % txt

def delall():
    with open(r'todo.txt', 'w') as fp:
        todo = []
        for item in todo:
            fp.write("%s\n" % item)
    return "Gotowe"
        
def list():
    temp = ''''''
    for x in todo:
        temp += str(x)
        temp += '''
'''
    if temp == "":
        return "Lista jest pusta."
    else:
        return temp
