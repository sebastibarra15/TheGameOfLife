Conway's Game of Life - README
==============================

Overview
--------
This project is an implementation of Conway's Game of Life using Python and Tkinter on 2020. 
The program simulates a cellular automaton system, where simple rules give rise 
to complex behaviors. Users can interact with the grid, set initial conditions, 
and observe how cells evolve over time. The project is a tribute to 
John Horton Conway and includes his image in the main interface.

Features
--------
- Interactive grid to manually select live or dead cells.
- Predefined patterns for automatic demonstrations of interesting behaviors.
- Adjustable speed controls: Slower, Normal, and Faster.
- Buttons for starting, pausing, resetting, and accessing instructions.
- Tribute to John Horton Conway with his image in the interface.
- Spanish version of the game without the tribute image.
- Spanish project report detailing the functionality and concepts.

Requirements
------------
1. Python 3.6+ installed on your system.
2. Pillow library for handling images:
   Install Pillow using the following command:
   pip install Pillow
3. Place the image file `Conwayy.JPG` in the same directory as the Python script 
   for the program to display the tribute.

How to Run the Program
----------------------
1. Ensure all required dependencies are installed.
2. Place the file `Conwayy.JPG` in the same folder as the Python script.
3. Run the script:
   python gameoflife.py

Details of the Interface
------------------------
Main Window:
  - Title: "THE GAME OF LIFE"
  - Includes an introduction to the Game of Life, its rules, and its dedication 
    to John Horton Conway.
  - Displays Conway's image with a brief description of his contributions.

Buttons:
  1. START GAME:
     - Opens the interactive grid.
     - Allows users to create or explore cellular patterns.
  2. INSTRUCTIONS:
     - Opens a detailed instruction window explaining the rules, buttons, 
       and patterns.
  3. HELP (available in the interactive grid):
     - Reopens the instructions window anytime during the game.

Interactive Grid
----------------
1. Grid:
   - A 20x40 grid where users can toggle cells between alive (white) and dead (black).
   - Click a cell to change its state.
2. Buttons:
   - START: Begins the simulation based on the current grid.
   - PAUSE: Temporarily stops the simulation.
   - RESET: Clears the grid to its initial state.
3. Speed Controls:
   - Slower: 1000ms per update.
   - Normal: 500ms per update.
   - Faster: 100ms per update.

Predefined Patterns
-------------------
The game includes the following predefined patterns:
  - SpaceShip
  - 10 Cell Row
  - Gosper Glider Gun
  - Butterfly
  - R-Pentomino
  - More options available in the dropdown menu.
Users can select a pattern, click START, and watch the simulation.

Spanish Version
---------------
- A version of the game is available entirely in Spanish, without the tribute 
  image to John Horton Conway.
- Includes a Spanish-language project report detailing the concepts, rules, 
  and implementation of the Game of Life.

Acknowledgment
--------------
This project is dedicated to the memory of John Horton Conway (1937-2020), 
whose contributions to mathematics and computer science have inspired generations. 
His Game of Life remains a cornerstone of cellular automaton research and a source 
of fascination for programmers and scientists worldwide.

Feel free to use and modify this project to explore Conway's Game of Life and learn 
about cellular automata!
