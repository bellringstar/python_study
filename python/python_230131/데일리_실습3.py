class PublicTransport:
    number_of_passenger = 0

    def __init__(self, name, fare):
        self.name = name
        self.fare = fare


    def get_in(self, passenger):
        PublicTransport.number_of_passenger += passenger

    def get_off(self, passenger):
        PublicTransport.number_of_passenger -= passenger

    def profit(self):
        return PublicTransport.number_of_passenger * self.fare
        

class Bus(PublicTransport):

    def __init__(self, name, fare, max_num):
        super().__init__(name, fare)
        self.max_num = max_num

    def get_in(self, passenger):
        if passenger > self.max_num:
            print('더이상 탑승할 수 없습니다.')
        else:
            PublicTransport.number_of_passenger += passenger

bus = Bus('bus',1450, 10)
bus.get_in




