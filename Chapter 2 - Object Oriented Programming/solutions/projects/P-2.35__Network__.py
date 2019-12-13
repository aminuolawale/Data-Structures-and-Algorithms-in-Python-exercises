# Write a set of Python classes that can simulate an Internet application in which one party, Alice, is periodically 
# creating a set of packets that she wants to send to Bob. An Internet process is continually checking if Alice has 
# any packets to send, and if so, it delivers them to Bob’s computer, and Bob is periodically checking if his computer
# has a packet from Alice, and, if so, he reads and deletes it
from random import  randrange
import time
class NetworkEvent:
    def __init__(self, type, data ):
        self.EVENT_TYPES = ['packet_created', 'packet_sent', 'packet_recieved']
        if type not in self.EVENT_TYPES:
            raise TypeError('{} is not a valid type'.format(type))
        self._type = type
        self._data = data
    def __repr__(self):
        return 'NetworkEvent->(type:{} | data:{})'.format(self._type, self._data)

class Network:
    def __init__(self):
        self._events = []
        self._clients = []
    def add_network_event(self, event):
        self._events.append(event)
    def send_packet(self, packet):
        recipient = packet._recipient
        recipient._messages.append(packet)
        # self._events.append(NetworkEvent('packet_sent',packet))
        
    def resolve_packets(self):
        for i,event in enumerate(self._events):
            if event._type == 'packet_created':
                self.send_packet(event._data)
                self._events.pop(i)
class Packet:
    def __init__(self, data, sender, recipient):
        self._sender = sender
        self._recipient = recipient
        self._data = data
    def __repr__(self):
        return 'Packet->(data:{} | sender:{} | recipient:{})'.format(self._data, self._sender, self._recipient)
    def data(self):
        return self._data
    def recipient(self):
        return self._recipient

class Client:
    def __init__(self, name):
        self._name = name
        self._packets = []
        self._messages = []
        self._network = None
    def __repr__(self):
        return 'Client->({})'.format(self._name)
    def join_network(self, network: Network):
        self._network = network
        network._clients.append(self)
    #methods
    def create_packet(self, data, recipient):
        packet = Packet(data, self, recipient)
        self._packets.append(packet)
        self._network.add_network_event(NetworkEvent('packet_created',packet))



    def periodically_generate_packets(self,period, cycles):
        data = ''
        recipient = ''
        for _ in range(cycles):
            count = randrange(2,10)
            for _ in range(count):
                self.create_packet(data, recipient)
            print('packet generated')
            time.sleep(period)
    @staticmethod
    def read_message(message):
        print('oh, I have a message')
        time.sleep(1)
        print("I'm done!")

    def check_messages(self):
        if len(self._packets) ==  0:
            print('Aww, No Messages. No one cares about me')
        else:
            for message in self._messages:
                self.read_message(message)


def server():
    alice = Client('Alice')
    bob = Client('Bob')
    network = Network()
    alice.join_network(network)
    bob.join_network(network)
    bob.create_packet('wqeqedwvwvwc', alice)
    alice.create_packet('wqeqedwc', bob)
    bob.create_packet('wqeqedwvwvwc', alice)
    alice.create_packet('wqeqedwc', bob)
    network.resolve_packets()
    print (network._events)
    print(alice._messages, bob._messages)
    print (network._events)



server()




            
        