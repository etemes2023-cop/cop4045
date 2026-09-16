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
        """"""
        try:
            user1_found = False
            user2_found = False
            for user in sn:
                if user == user1:
                    user1_found = True
                if user == user2:
                    user2_found = True
            sn[user1][1].append(user2)
            sn[user2][1].append(user1)

            if user1_found and user2_found:
                return True
            else:
                return False
            
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
                fullname = input("\nEnter full name: ")
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

solution = SocialNetwork()
solution.main()