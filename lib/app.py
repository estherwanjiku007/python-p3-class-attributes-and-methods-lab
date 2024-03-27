class Song:
    count=0
    artists=[]
    genres=[]
    artist_count={}
    genre_count={}
    def __init__(self,name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_to_song_count()
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        Song.add_to_artist_count(artist)
        Song.add_to_genre_count(genre)
    
    @classmethod
    def add_to_song_count(cls,incrementor=1):
        cls.count+=incrementor
    
    @classmethod
    def  add_to_artists(cls,an_artist):
        cls.artists.append(an_artist)
        print(cls.artists)

    @classmethod
    def add_to_genres(cls,a_genre):
        cls.genres.append(a_genre)
        print(cls.genres)

    @classmethod
    def add_to_artist_count(cls,an_artist):
        cls.artist_count[an_artist]=cls.artists.count(an_artist)
    
    @classmethod
    def add_to_genre_count(cls,a_genre):
        cls.genre_count[a_genre]=cls.genres.count(a_genre)
        
#all_artists=Song("Shusho","Gospel","Gospel")

    
