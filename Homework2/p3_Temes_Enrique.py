class SocialNetwork:
    def __init__(self):
        pass

    def add_user(self, sn, username, fullname):
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

    def main(self):
        sn = {}
        username = input("Enter username: ")
        fullname = input("\nEnter full name: ")
        print(self.add_user(sn, username, fullname))
        return 0

solution = SocialNetwork()
solution.main()