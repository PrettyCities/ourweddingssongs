import sys

from websitemaker.aws_services import AwsServices
from websitemaker.utils.spotify_song_finder import SpotifySongFinder

TIMES = {
    "c": "cocktail",
    "d": "dinner",
    "p": "party"
}

PROMPT = "Enter 'y' for yes, or anything else for no."

def input_loop():
    print("What would you like to do?")
    print("\ta: Add a song")
    print("\tu: Update the website")

    action = input()

    if action == "a":
        print("What is the song title?")
        title = input()
        print("What is the song's artist?")
        artist = input()

        spotify_uri = SpotifySongFinder.interactive_find(artist, title)

        print("When should the song play?")
        print("\tc: Cocktail hour(s)")
        print("\td: Dinner")
        print("\tp: Party time")
        time = input()

        if not TIMES.get(time, None):
            print("You didn't enter c, d, or p!")
            raise Exception

        print("Adding your song...")
        AwsServices.add(title=title, artist=artist, time=time, spotify_uri=spotify_uri)

    if action == "u":
        print("Updating...")
        from websitemaker.website_maker import WebsiteMaker
        WebsiteMaker.render()
        AwsServices.upload_website()

    print("Would you like to quit? {}".format(PROMPT))
    user_wants_to_quit = input()

    if user_wants_to_quit == "y":
        sys.exit(0)


def get_uris():
    is_spotify = input("Is this a Spotify song? {}".format(PROMPT))
    if is_spotify == "y":
        spotify_uri = input("Enter the uri")
        return spotify_uri, None

    is_soundcloud = input("Is this a Soundcloud song? {}".format(PROMPT))
    if is_soundcloud:
        soundcloud_uri = input("Enter the uri")
        return None, soundcloud_uri

    return None, None


if __name__ == "__main__":
    print("Hello! Welcome to the interface for ourweddingssongs")
    while True:
        input_loop()
