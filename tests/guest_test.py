import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Satsuki", 10.00, "Radio Gaga")
    
    def test_guest_has_name(self):
        self.assertEqual("Satsuki", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(10, self.guest.wallet)
    

    def test_pay_fee(self):
        room_fee = 4.00
        self.guest.pay_fee(room_fee)
        self.assertEqual(6.00, self.guest.wallet)

    def test_guest_has_fave_song(self):
        self.assertEqual("Radio Gaga", self.guest.fave_song)

    # def test_guest_cheer_for_fave_song(self, song):
    #     # arrange
    #     # action
    #     # assert
    #     pass
