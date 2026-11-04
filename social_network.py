class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Only add the friend if they aren't already in the list
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        # Prevent duplicate people
        if name in self.people:
            print(f"{name} is already in the network!")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        # Make sure both people exist before connecting them
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Friendships go both ways, so add each person to the other's list
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friend_names)}")


# Test your code here

# Test the Person class on its own
alex = Person("Alex")
jordan = Person("Jordan")
print(alex.friends)  # []
alex.add_friend(jordan)
print(alex.friends[0].name)  # Jordan

print()

network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
print(network.people)
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Edge case: adding a duplicate person
network.add_person("Alex")  # Alex is already in the network!

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")  # Friendship not created. Johnny doesn't exist!
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Edge case: adding the same friendship twice shouldn't create duplicates
network.add_friendship("Alex", "Jordan")

print()
network.print_network()


'''
Design Memo

A graph is the right structure for a social network because a social network
is really just people and the connections between them. In a graph, each
person is a node and each friendship is an edge. Friendships go both ways, so
the graph is undirected: when Alex is friends with Jordan, Jordan is also
friends with Alex. A graph also lets every person connect to any number of
other people, which is exactly how real friend groups work.

A list would not work as well because it only stores items in order. It can
hold all the people, but it has no natural way to show who is connected to
whom. A tree is closer, but trees are hierarchical: each node has exactly one
parent and there are no cycles. Social networks are full of cycles. For
example, Morgan, Casey and Riley are all friends with each other, so they
form a loop that a tree is not allowed to have.

I used an adjacency list, where each Person keeps a list of their friends,
and the network keeps a dictionary of names to Person objects. Looking up a
person by name in the dictionary is fast (O(1)), so adding a friendship is
quick. The trade-off is that checking for a duplicate friend means scanning
the friends list, which is O(k) where k is the number of friends. Printing
the network visits every person and every friendship, so it is O(V + E). An
adjacency matrix would make checking a friendship O(1), but it would use
V x V space, and most of it would be empty because each person is only
friends with a small part of the network. For a sparse network like this,
the adjacency list uses much less memory.
'''