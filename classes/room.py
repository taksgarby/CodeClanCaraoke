class Room:
    def __init__(self, name, capacity, fee):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []
        self.fee = fee
        self.total_sales = 0

    
    def check_in_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            return "Sorry, there is no more space in this room."

    def check_out_guest(self, guest_name):
        for guest in self.guests:
            if guest_name == guest:
                self.guests.remove(guest_name)
    
    def add_song(self, song):
        self.songs.append(song)

    # def add_total_sales(self):
    #     self.total_sales = self.fee * len(self.guests)
        
    def cheer_for_fave_song(self, fave_song):
        for song in self.songs:
            if fave_song == song.title:
                return "Woo Hoo"
        else:
            return "meh"
    

    