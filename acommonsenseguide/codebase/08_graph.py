from collections import deque

class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.visited = False

    def add_friend(self, friend):
        self.friends.append(friend)

    # breadth-first search
    def display_network(self):
        to_reset = []
        queue = deque([self])
        self.visited = True

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex.name)

            for friend in current_vertex.friends:
                if not friend.visited:
                    to_reset.append(friend)
                    queue.append(friend)
                    friend.visited = True

        for person in to_reset:
            person.visited = False


mary = Person('Mary')
bob = Person('Bob')
jay = Person('Jay')
mary.add_friend(bob)
bob.add_friend(jay)
mary.add_friend(jay)
print(mary.friends[0].name)

mary.display_network()
#breadth-first search
#depth-first search
