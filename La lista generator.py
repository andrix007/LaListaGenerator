import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials


def pause():
    input("Press the <ENTER> key to continue...")


def connectToSpotify(client_id="95ecfeec533b482eb92f25a9c0303836", client_secret="5435383558a140779bf084386bc5f390"):
    return spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))


def WrtitePlaylistSongsToList(file="List.txt", user_link = "https://open.spotify.com/user/2s744jpq2tiwuofn79mnla2cx?si=fd13de4be51943ca",
 playlist_link = "https://open.spotify.com/playlist/0rLkhpdhuTJORKiIZUMLbG?si=04bd229fa6da4792", isNumbered = 'no'):

    songs = {}

    results = get_playlist_tracks(user_link, playlist_link)
    lineCounter = 0

    with open(file, "w", encoding="utf-8") as playlist_list:

        for item in results:

            artists = ""

            for artist in item["track"]["artists"]:
                artists = artists + str(artist['name']) + ','
            artists = artists[:-1]

            track = item["track"]["name"]

            if isNumbered == 'yes':
                lineCounter = lineCounter+1
                line = str(lineCounter) + ". " + artists + " - " + track + '\n'
            else:
                line = artists + " - " + track + "\n"

            playlist_list.write(line)


def get_playlist_tracks(username,playlist_id):
    results = spotify.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks


def getJsonConfig():
    with open('config.json') as conf:
        config = json.load(conf)
        return config


if __name__ == "__main__":

    try:
        print("Connecting to Spotify API...")
        spotify = connectToSpotify()

        print("Retrieving configuration...")
        config = getJsonConfig()

        user_link = config['user_link']
        playlist_link = config['playlist_link']
        isNumbered = config['numbered']
        ImSureYouPutYes = config['put_yes_if_you_are_cool']

        if ImSureYouPutYes == 'yes':
            print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        else:
            print("Writing playlist songs in list...")
            WrtitePlaylistSongsToList("./List.txt", user_link, playlist_link, isNumbered)

            print("Done! Check your list and be mesmerized!")

        pause()
    except Exception as e:
        print(e)







