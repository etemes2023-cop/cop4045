class SocialNetwork:
    def __init__(self):
        pass

    def add_user(self, sn: dict[str, tuple[str, list[str]]], username: str, fullname: str) -> bool:
        """Checks if user is already in social network. If so, return False. Otherwise, add that user and return True."""
        try:
            friends = []
            for cur_username in sn:
                if cur_username == username:
                    return False
                
            sn[username] = (fullname, friends)
            return True
        
        except TypeError:
            print("Invalid username or full name or dictionary type.")
            raise

    def add_friend(self, sn: dict[str, tuple[str, list[str]]], user1: str, user2: str) -> bool:
        """Checks if both users exist in dictionary. If so, they are added to each other's network and true is returned.
        Otherwise, return false."""
        try:
            user1_found = False
            user2_found = False
            for user in sn:
                if user == user1:
                    user1_found = True
                if user == user2:
                    user2_found = True

            if user1_found and user2_found:
                sn[user1][1].append(user2)
                sn[user2][1].append(user1)
                return True
            else:
                return False
            
        except TypeError:
            print("Invalid username or full name or dictionary type.")
            raise    

    def get_friend(self, sn: dict[str, tuple[str, list[str]]], user1: str, distance: int)-> list[str]:
        """Gets every unique friend for one user in the social network through nested loops."""
        try:
            friends = []
            current = sn[user1][1].copy()
            friends = current.copy()
            print(f"user1: {user1}")
            print(f"current: {current}")
            print(f"friends: {friends}")
            for i in range(1, distance):
                next_link = []
                for friend in current:
                    for friend_of_friend in sn[friend][1]:
                        if (friend_of_friend in friends or friend_of_friend == user1):
                            continue
                        else:
                            friends.append(friend_of_friend)
                            next_link.append(friend_of_friend)
                current = next_link
            return friends
        
        except TypeError:
            print("Invalid username or full name or dictionary type.")
            raise   
 
    def main(self):
        sn = {}
        user_added = True
        friend_added = True
        while (user_added == True):
            keep_going = input("Do you want to add another user? ")
            if (keep_going.lower() == 'y'):
                username = input("Enter username: ")
                fullname = input("Enter full name: ")
                print(self.add_user(sn, username, fullname))
            elif (keep_going.lower() == 'n'):
                user_added = False
            else:
                print("\nInvalid message.")

        while (friend_added == True):
            keep_going = input("Do you want to add a friendship? ")
            if (keep_going.lower() == 'y'):
                user1 = input("Enter first username: ")
                user2 = input("Enter second username: ")
                print(self.add_friend(sn, user1, user2))
            elif (keep_going.lower() == 'n'):
                friend_added = False
            else:
                print("\nInvalid message.")

        user_in = input("Enter username to find friends for: ")
        distance = int(input(f"Enter link distance for {user_in}: "))
        print(self.get_friend(sn, user_in, distance))

solution = SocialNetwork()
solution.main()