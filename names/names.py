import time

class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        # self.value_listed = list(self.value)
        # self.numeric_value = ord(self.value_listed[0].lower())


    def insert(self, value):
        #case 1: value is less than self.value
        #compare first letters
        if value < self.value:
            #if no left child, insert here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        #case 2: value is greater than or equal to self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else: 
                self.right.insert(value)
    
    def contains(self, target):
        #case 1: self.value is = target
        if self.value == target:
            return True
        #case 2: if target is < self.value
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        #case 3: if target is >= self.value
        else:
            if self.right is None:
                return False
            else: 
                return self.right.contains(target)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#insert the values into our tree
my_tree = BSTNode('Hallie Vazquez')
for name in names_1:
    my_tree.insert(name)

#if we resolve to true we append to duplicates list:
for name in names_2:
    if my_tree.contains(name) is True:
        duplicates.append(name)
        
#code to be replaced:
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
