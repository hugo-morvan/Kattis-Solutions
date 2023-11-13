m,q = input().split()
m = int(m)
q = int(q)


class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

    def add_child(self, obj):
        self.children.append(obj)

    def countChildren(self):
        return len(self.children)

print("input")
employees = []
for i in range(m):
    id, salary, height = input().split()
    id = int(id)
    salary = int(salary)
    height = int(height)
    employee = {'id': id, 'salary': salary, 'height': height}
    employees.append(employee)

employees.sort(key=lambda x: x['salary'], reverse=True)
print(employees)

def buildTree(employees):
    root = Tree(employees[0])
    for i in range(1, len(employees)):
        employee = employees[i]
        parent = findParent(root, employee)
        parent.add_child(Tree(employee))
    return root

def findParent(root, id):
    if root.data['id'] == id:
        return None
    for child in root.children:
        if child.data['id'] == id:
            return root
        else:
            return findParent(child, id)

def findEmployee(root, id):
    if root.data['id'] == id:
        return root
    for child in root.children:
        if child.data['id'] == id:
            return child
        else:
            return findEmployee(child, id)


root = buildTree(employees)

print("Tree:")
def printTree(root):
    print(root.data['id'], end=" ")
    print("Children: ", end="")
    for child in root.children:
        printTree(child)

print("Queries:")
for i in range(q):
    id = int(input())
    #emp = findEmployee(root, id)
    boss = findParent(root, id)

    #subs = emp.countChildren()
    bossID = boss.data['id']

    print(bossID if bossID != None else 0)

