#File: term_project.py
#Description: This is a basic representation of a nervous system. 

#Student Name: Primo M. Marquez
#Student UT EID: pmm2734

#Partner Name: Henry Chen
#Partner UT EID: hhc462

#Course Name: CS 313E
#Unique Number: 52590

import random
import math
import time

# universal constants for the program to use
list_of_actions = {
    'Move': 'The hand moved.',
    'Snap': 'The hand used its fingers to snap.',
    'Hold': 'The hand is holding an object.',
    'Clench': 'The hand clenched into a fist.',
    'Grab': 'The hand grabbed an object'
}

refractory_period = 0.01

class Neuron():
    '''A simple representation of a neuron'''
    def __init__ (self, dendrite, axon = None, threshold = -55):
        self.dendrite = dendrite
        self.axon = axon
        self.threshold = threshold
        self.refractory = False

    def stimulate_neuron(self):
        '''Illustrates the flow of ions through the neuronal membrane and sets it to its
        refractory period'''
        if self.refractory:
            print('The nerve cannot be stimulated. It is still within it\'s refractory period.')
            return
        num_sodium_ions = random.randint(100, 1000)
        num_potassium_ions = random.randint(100, 1000)
        print(num_sodium_ions, 'sodium ions entered.', num_potassium_ions,
              'potassium ions were released.')

        self.refractory = True
        time.sleep(refractory_period)
        self.reset_neuron()
    
    def reset_neuron(self):
        '''Resets neuron'''
        self.refractory = False

class NerveSystem():
    '''A simple representation of a nervous system'''
    def __init__ (self, inside_ion = 10, outside_ion = 1):
        self.first = None
        self.organ = 'Hand'
        self.inside_ion = inside_ion
        self.outside_ion = outside_ion

    def get_resting_potential(self):
        '''Calculates the resting potential of the system using inside_ion and 
        outside_ion'''
        resting_potential = 58 * math.log10(self.outside_ion/self.inside_ion)
        return resting_potential

    def get_num_neurons(self):
        '''Returns the number of neurons in the system; returns -1 if there
        are no neurons'''
        curr = self.first
        res = 0
        if curr is None:
            return -1
        while curr != self.organ:
            res += 1
            curr = curr.axon
        return res

    def insert_neuron(self, data):
        '''Inserts a neuron into the system'''
        new_nerve = Neuron(data)
        current = self.first

        if current is None:
            self.first = new_nerve
            self.first.axon = self.organ
            return
        
        while current.axon != self.organ:
            current = current.axon
        
        current.axon = new_nerve
        new_nerve.axon = self.organ
        return
    
    def transmit_message(self, message, voltage):
        '''Sends a message from one neuron to another, eventually reaching
        the hand'''
        current = self.first

        # will only pass a message if there are neurons to transmit the message
        if current is None:
            return 'No nerves to transmit message.\n'

        # will only create an action potential if the voltage is greater than the 
        # threshold
        if voltage < current.threshold:
            return 'Message not strong enough.'

        print('Signal was strong enough. Propagating signal...\n')
        self._transmit_message(current)
        try:
            print(f'Message \"{message.lower()}\" successfully passed to hand.\n')
        except TypeError:
            print('Error! Your message must be a string.')
        except AttributeError:
            print('Error! Your message must be a string.')
        return self.hand_action(message)
    
    def _transmit_message(self, current):
        '''Helper function - responsible for passing message from one neuron
        to the next'''
        if current == self.organ:
            return
        current.stimulate_neuron()
        print('Passing message to next nerve...\n')
        self._transmit_message(current.axon)

    def hand_action(self, message):
        '''Returns a response of the hand once the message is received'''
        try:
            if message in list_of_actions:
                return list_of_actions[message]
        except TypeError:
            return 'The hand didn\'t do anything...'
        return 'The hand didn\'t do anything...'

    def __str__ (self):
        '''Returns a string implementation of the nerve system'''
        string = 'No system to display.'
        count = 0
        curr = self.first

        if curr == None:
            return string

        string = ''
        while curr.axon != self.organ:
            string += str(curr.dendrite)
            count += 1
            string += "-->"
            curr = curr.axon

        string += str(curr.dendrite)
        string += "-->"
        string += str(self.organ)
        return string
    
class Queue():
    '''Queue implements the FIFO principle'''  
    def __init__ (self):
        self.queue = []

    def enqueue(self, item):
        '''Takes in an item and adds it to the end of the queue'''
        self.queue.append(item)

    def dequeue(self):
        '''Removes an item from the end of the queue'''
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        '''Checks if the queue is empty'''
        return len(self.queue) == 0

    def __str__(self):
        '''Returns a string representation of the queue'''
        return str(self.queue)

def main():
    my_queue = Queue()
    my_queue.enqueue(('Grab', -60))
    my_queue.enqueue(('Grab', -20))
    my_queue.enqueue(('Hold', -40))
    my_queue.enqueue(('Move', -30))


    nerve_system = NerveSystem()
    print(nerve_system, '\n')
    print(nerve_system.transmit_message('Hold', 10))
    print('#########################################\n')

    for _ in range(3):
        nerve_system.insert_neuron(('#'))
    print(nerve_system.transmit_message('()', 10))
        
    print('Number of neurons in system:', nerve_system.get_num_neurons())

    print(nerve_system, '\n')
    print('Resting Potential:', nerve_system.get_resting_potential(), '\n')

    print('#########################################\n')

    while not my_queue.is_empty():
        item = my_queue.dequeue()
        print(nerve_system.transmit_message(item[0], item[1]))
        print('\n#########################################\n')

if __name__ == "__main__":
    main()
