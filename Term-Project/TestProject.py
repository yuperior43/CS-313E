#File:TestProject.py
#Description: Runs basic tests to ensure functionality of nervous system.

#Student Name: Primo M. Marquez
#Student UT EID: pmm2734

#Partner Name: Henry Chen
#Partner UT EID: hhc462

#Course Name: CS 313E
#Unique Number: 52590

import unittest
from term_project import * 

class TestProject(unittest.TestCase):
    def test_basic_functionality(self):
        nerve_system = NerveSystem()
        for _ in range(3):
            nerve_system.insert_neuron('A')
        self.assertEqual(nerve_system.get_num_neurons(), 3)
        self.assertEqual(nerve_system.transmit_message('Hold', -30), 'The hand is holding an object.')
    
    def test_no_nerves(self):
        nerve_system = NerveSystem()
        self.assertEqual(nerve_system.transmit_message('Hold', -30), 'No nerves to transmit message.\n')

    def test_weak_message(self):
        nerve_system = NerveSystem()
        nerve_system.insert_neuron('A')
        self.assertEqual(nerve_system.transmit_message('Hold', -60), 'Message not strong enough.')

    def test_resting_potential(self):
        nerve_system = NerveSystem(inside_ion=5, outside_ion=2)
        expected_resting_potential = 58 * math.log10(2/5)
        self.assertAlmostEqual(nerve_system.get_resting_potential(), expected_resting_potential, places=2)

    def test_queue_integration(self):
        nerve_system = NerveSystem()
        for i in range(5):
            nerve_system.insert_neuron('#')

        my_queue = Queue()
        my_queue.enqueue(('Hold', -30))

        expected_result = '[(\'Hold\', -30)]'
        self.assertEqual(str(my_queue), expected_result)

if __name__ == '__main__':
    unittest.main()
