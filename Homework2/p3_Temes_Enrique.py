import csv
import ast
class SocialNetwork:
    def __init__(self):
        pass

    #Part A
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

    #Part B
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

    #Part C
    def get_friend(self, sn: dict[str, tuple[str, list[str]]], user1: str, distance: int)-> list[str]:
        """Gets every unique friend for one user in the social network through nested loops."""
        try:
            current = sn[user1][1].copy()
            friends = current.copy()
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

    #Part D
    def save_network(self, filename: str, sn: dict[str, tuple[str, list[str]]]) -> None:
        """Loops through the social network and adds each user's username, fullname, and friends list to a csv file."""
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["username", "fullname", "friends"])
                for user in sn:
                    writer.writerow([user, sn[user][0], sn[user][1]])
        except FileNotFoundError:
            print(f"File {filename} does not exist.")
            raise

    #Part E
    def load_network(self, filename: str) -> dict[str, tuple[str, list[str]]]:
        """Reads csv file, skips header, and converts each row back into a dictionary to be returned and printed."""
        try:
            sn = {}
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    username = row[0]
                    fullname = row[1]
                    friends = ast.literal_eval(row[2])
                    sn[username] = (fullname, friends)
                return sn
                    
        except FileNotFoundError:
            print(f"File {filename} does not exist.")
            raise

    #Part F
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

        filename = input("Enter filename to save social network: ")
        self.save_network(filename, sn)
        sn = self.load_network(filename)
        print(sn)

solution = SocialNetwork()
solution.main()