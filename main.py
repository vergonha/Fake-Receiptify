try:
    from receiptify import FakeReceiptify
    import ctypes
    import os 
    import platform
    from colorama import Fore
    import json
except:
    raise(" [!] Error while importing modules...")

class Interface():
    def __init__(self, link, playlist):
        self.playlist = playlist
        self.link = link
        self.object = self.load_classes()
    
    def load_classes(self):
        try:
            class_instance = FakeReceiptify(self.link, self.playlist)
            class_instance.playlist_data
            return class_instance
        except:
            print (f"""{Fore.RED}[!] Critical error

Check if your Receiptify URL is updated and has "accessToken" in address
Check if your Spotify playlist link is a valid URL""")
            input() 
            exit()

    @staticmethod
    def print_help():
        print(f"""{Fore.YELLOW}
        
[Help]
Link -> URL from your session Receiptify in browser
Playlist -> Playlist with songs you want to show

        {Fore.WHITE}""")

    @staticmethod
    def print_title():
        ascii_text = f"""{Fore.MAGENTA}

  █████▒▄▄▄       ██ ▄█▀▓█████ 
▓██   ▒▒████▄     ██▄█▒ ▓█   ▀ 
▒████ ░▒██  ▀█▄  ▓███▄░ ▒███   
░▓█▒  ░░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ 
░▒█░    ▓█   ▓██▒▒██▒ █▄░▒████▒
 ▒ ░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░
 ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░
 ░ ░     ░   ▒   ░ ░░ ░    ░   
             ░  ░░  ░      ░  ░
        {Fore.WHITE}"""
        print(ascii_text)

    @staticmethod
    def update_cli_title():
        ctypes.windll.kernel32.SetConsoleTitleW(
            "Fake Receiptify >..<"
        )

    @staticmethod
    def clear():
        if platform.system() == "Windows":
            os.system('cls')
            Interface.update_cli_title()
        else:
            os.system('clear')

    @staticmethod
    def display_inputs():
        link = input(f"{Fore.YELLOW} Receiptify URL: {Fore.MAGENTA}")
        playlist = input(f"{Fore.YELLOW} Playlist URL: {Fore.MAGENTA}")
        return {
            "link": link,
            "playlist": playlist
        }

    @staticmethod
    def display_data(data):
        Interface.clear()
        print(f"{Fore.YELLOW}Paste this in your Console Browser in Receiptify Page{Fore.MAGENTA}")
        print(data.strip('"'))
        input()

    @staticmethod
    def print():
        Interface.print_title()
        Interface.print_help()


def main():
    Interface.print()
    URLs = Interface.display_inputs()
    instance = Interface(URLs['link'], URLs['playlist']).object
    Interface.display_data(instance.fake_receipt())
    exit()

if __name__ == "__main__":
    Interface.clear()
    main()