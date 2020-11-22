import random
import math
from collections import deque

class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}


    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)


    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()


    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user_id in range(num_users):
            self.add_user(f'User {user_id}')

        # Create friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)

        num_friendships = math.floor((len(self.users) * avg_friendships) / 2)

        for i in range(num_friendships):
            friendship = possible_friendships[i]
            user_id, friend_id = friendship[0], friendship[1]
            self.add_friendship(user_id, friend_id)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        visited = {}
        queue = deque()
        queue.append([user_id])
        while len(queue) > 0:
            currPath = queue.popleft()
            currUser = currPath[-1]
            if currUser not in visited:
                visited[currUser] = currPath
                for friend_id in self.friendships[currUser]:
                    newPath = list(currPath)  # Copy
                    newPath.append(friend_id)
                    queue.append(newPath)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

# 3. Questions

# To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why?
# The equation is num_friends = (avg_friends * num_users) / 2
# So, num_friends = (10 * 100) / 2 = 500

# If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network
    # sg = SocialGraph()
    # sg.populate_graph(1000, 5)
    # # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # # print(connections)
