"""
    A finite state machine (FSM) is a mathematical model of computation with states, transitions, inputs and outputs.
    This machine is always in a one state at the time and can move to other states using transitions. A transition
    changes the state of the machine to another state.

    A large number of problems can be modeled using finite state machines. Simple examples of state machines used in
    modern life are vending machines, elevators and traffic lights.  Advanced usage are artificial intelligence,
    language parsing and communication protocol design.
"""

from fysom import *

fsm = Fysom({'initial' : 'awake',
             'final' : 'red',
             'events' : [
                 {'name': 'wakeup', 'src': 'sleeping', 'dst': 'awake'},
                 {'name':'sleep', 'src':'awake', 'dst':'sleeping'}
             ]})

print(fsm.current)
fsm.sleep()
print(fsm.current)
fsm.wakeup()
print(fsm.current)