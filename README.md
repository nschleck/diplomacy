# diplomacy in Python

This code base allows the game Diplomacy to be run and adjudicated in Python

The code is *almost* completely runable at the moment. Future updates will fix the following issues:
1. Convoy orders don't totally work yet - specifically, input is not handled in moveFunctions properly
2. Path function needs to be expanded to handle edge cases of multiple paths -- I need to look up the rules on this one.
3. Multiple Coasts haven't been implemented to bulgaria, spain, etc. This will affect fleet movement and maybe convoying?
4. Add easier input for initial unit conditions for testing (sandbox)


Future big updates, after getting the code watertight:
1. Create a graphical gamestate that shows unit positions, and maybe moves as well.
2. Modify the order input structure to allow multiple players to realistically play a game (i.e. simultaneous hidden orders)
