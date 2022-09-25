
class Guest:
    def __init__(self, name, wallet, fave_song):
        self.name = name
        self.wallet = wallet
        self.fave_song = fave_song


    def pay_fee(self, room_fee):

        self.wallet -= room_fee
