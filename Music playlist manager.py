playlist = []

def add_song(song):
    playlist.append(song)
    print(f"\n'{song}' song was Added to Playlist Successfully")
    
def remove_song(song):
    if song in playlist:
        playlist.remove(song)
        print(f"\n'{song}' song was removed successfully from playlist")
    else:
        print("\nSong was not found in playlist")
        
def view_playlist():
    print("\nYour Music Playlist")
    if len(playlist) == 0:
        print("\nThe Playlist was Empty!")
    else:
        for index, song in enumerate(playlist,1):
            print(f"\n{index}.{song}")

def menu():
    print("\n..............Mini Music Palylist Manager.............. ")
    
    while True:
        print("\nOptions : [1] Add Song  [2] Remove song  [3] View Playlist  [4] Exit ")
        user_option = input("\nEnter your option : ")
        
        if user_option == '1':
            song = input("Enter The song name:")
            add_song(song)
            
        elif user_option == '2':
            song = input("Enter the song name:")
            remove_song(song)
            
        elif user_option == '3':
            view_playlist()
            
        elif user_option == '4':
            print("\nThanks for using Mini Music Playlist....")
            break
        
        else:
            print('\nInvalid Option number!')
menu()