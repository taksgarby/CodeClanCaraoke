import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("One", 5, 4.50)

    def test_room_has_name(self):
        self.assertEqual("One", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)
    
    def test_room_has_song_list(self):
        self.assertEqual([], self.room.songs)

    
    def test_room_has_guests(self):
        self.assertEqual([], self.room.guests)

    def test_room_has_guests_num(self):
        self.assertEqual(0, len(self.room.guests))
    
    def test_room_has_fee(self):
        self.assertEqual(4.50, self.room.fee)

    def test_room_has_total_sales(self):
        self.assertEqual(0, self.room.total_sales)

    def test_check_in_guest(self):
        # arrange
        guest = Guest("Mei", 15.00, "River")
        # act
        self.room.check_in_guest(guest)
        # assert
        self.assertEqual([guest], self.room.guests)

    def test_check_out_guest(self):
        guest = Guest("Totoro", 100.00, "Shima Uta")
        self.room.check_in_guest(guest)
        self.room.check_out_guest(guest)
        self.assertEqual([], self.room.guests)

    def test_add_song_to_room(self):
        song = Song("Shima Uta", "The Boom")
        self.room.add_song(song)
        self.assertEqual([song], self.room.songs)
    
    
    def test_cannot_check_out_guest_(self):
        guest_1 = Guest("April", 5.00, "Doraemon Theme")
        guest_2 = Guest("Beth", 10.00, "Praise You")
        guest_3 = Guest("Callum", 7.00, "Little Lion Man")
        guest_4 = Guest("Dawn", 10.00, "We Are The Champions")
        guest_5 = Guest("Ether", 4.00, "A Case Of You")
        guest_6 = Guest("Fukase", 10.00, "Cactus Tree")
        self.room.check_in_guest(guest_1)
        self.room.check_in_guest(guest_2)
        self.room.check_in_guest(guest_3)
        self.room.check_in_guest(guest_4)
        self.room.check_in_guest(guest_5)

        result = self.room.check_in_guest(guest_6)

        self.assertEqual("Sorry, there is no more space in this room.", result)


    def test_cheer_for_fave_song(self):
        # arrange
        guest = Guest("Totoro", 100.00, "Shima Uta")
        self.room.check_in_guest(guest)
        song = Song("Shima Uta", "The Boom")
        self.room.add_song(song)
        result = self.room.cheer_for_fave_song(guest.fave_song)
        self.assertEqual("Woo Hoo", result )
        

        

    # def test_add_to_total_sales(self):
    #     # arrange
    #     guest_1 = Guest("April", 5.00)
    #     guest_2 = Guest("Beth", 10.00)
    #     guest_3 = Guest("Callum", 7.00)
    #     guest_4 = Guest("Dawn", 10.00)
    #     guest_5 = Guest("Ether", 4.00)
    #     self.room.check_in_guest(guest_1)
    #     self.room.check_in_guest(guest_2)
    #     self.room.check_in_guest(guest_3)
    #     self.room.check_in_guest(guest_4)
    #     self.room.check_in_guest(guest_5)

    #     # act
    #     result = self.room.add_total_sales()
    #     # assert
    #     self.assertEqual(22.50, result)
    #     # self.room.total_sales