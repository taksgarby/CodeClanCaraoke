import unittest
from classes.song import Song
from classes.room import Room

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Little Lion Man", "Mumford & Sons")
    
    def test_song_has_title(self):
        self.assertEqual("Little Lion Man", self.song.title)
    
    def test_song_has_artist(self):
        self.assertEqual("Mumford & Sons", self.song.artist)