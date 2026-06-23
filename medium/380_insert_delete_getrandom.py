import random 

class RandomizedSet:

    def __init__(self):
        self.items_list = []
        self.items_map = {}
        self.length = 0
        

    def insert(self, val: int) -> bool:

        if val not in self.items_map:
            # map value to first available index in list
            self.items_map[val] = self.length

            # add to list
            self.items_list.append(val)

            self.length += 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.items_map:
            
            # get the current index of val to remove
            index = self.items_map[val]

            # check if index of item to remove is already last .if it is, don't need to swap
            if index == self.length - 1:
                pass

            # otherwise, swap
            else:
                
                # get value current at last index.
                swapped_val = self.items_list[self.length - 1]

                # update map with kept value : original index of removed item
                self.items_map[swapped_val] = index
                
                # perform swap
                self.items_list[index], self.items_list[self.length - 1] = self.items_list[self.length - 1], self.items_list[index]

            # remove from map, list
            self.items_map.pop(val)
            self.items_list.pop()
            
            self.length -= 1
            return True
        
        return False

    def getRandom(self) -> int:
        index = random.randint(0, self.length - 1)
        return self.items_list[index]
        


def show(rs, action, result=None):
    if result is None:
        print(f"{action}")
    else:
        print(f"{action} -> {result}")
    print("state:", rs.__dict__)
    print("-" * 50)


rs = RandomizedSet()
show(rs, "init")

show(rs, "insert(10)", rs.insert(10))    # True
show(rs, "insert(20)", rs.insert(20))    # True
show(rs, "insert(30)", rs.insert(30))    # True
show(rs, "insert(40)", rs.insert(40))    # True
show(rs, "insert(50)", rs.insert(50))    # True

show(rs, "insert(30)", rs.insert(30))    # False, duplicate
show(rs, "insert(10)", rs.insert(10))    # False, duplicate

show(rs, "remove(30)", rs.remove(30))    # True, middle removal
show(rs, "remove(10)", rs.remove(10))    # True, first-ish removal
show(rs, "remove(99)", rs.remove(99))    # False, not present

show(rs, "insert(60)", rs.insert(60))    # True
show(rs, "insert(70)", rs.insert(70))    # True

show(rs, "remove(50)", rs.remove(50))    # True
show(rs, "remove(70)", rs.remove(70))    # True, possibly last removal

show(rs, "insert(80)", rs.insert(80))    # True
show(rs, "insert(90)", rs.insert(90))    # True
show(rs, "insert(100)", rs.insert(100))  # True

show(rs, "remove(20)", rs.remove(20))    # True
show(rs, "remove(40)", rs.remove(40))    # True
show(rs, "remove(60)", rs.remove(60))    # True

show(rs, "insert(20)", rs.insert(20))    # True again after removal
show(rs, "insert(30)", rs.insert(30))    # True again after removal

print("Random checks:")
for _ in range(20):
    val = rs.getRandom()
    print(val, val in rs.__dict__.get("nums", rs.__dict__.get("values", [])))