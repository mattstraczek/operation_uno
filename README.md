# Operation UNO
## by Adnan Noorullah​, Alex Kwandou​, Matt Straczek, Jacob Stolker​
### adnann2, kwandou2, mstrac4, stolker2
---
## Overview 
### Users can play UNO with
- Single Player mode ​
- AI with three difficulty modes​
- Player accounts
- Different rulesets/new cards​
- Real-life Sound effects​
- Theme music
- Custom graphics ​

---
## Why UNO?
- We wanted to create a recognizable game we all enjoy playing​
- We wanted to put our own spin on the game​
    - Custom rulesets, cards, mechanics are possible

### Roles
- Adnan Noorullah​ -> Graphics/Win Condition/UX
- Alex Kwandou​    -> Animations/Backend/Logic
- Matt Straczek   -> Graphics/Accounts/UX
- Jacob Stolker​   -> Mechanics/Logic/Testing

---

## How to Install
- The program requires python3 and the Pygame library to run.
- You can find directions to install at https://www.pygame.org/wiki/GettingStarted
- To run the actual game, type "python3 OperationUNO.py" or "python OperationUNO.py"

---

## Technical Architecture

- ### Libraries
    - Pygame     -> game functionality
    - numpy      -> data handling, game logic
    - unit-tests -> testing

- ### Components

    - Card    –> basic UNO card that contains color and value attributes​
    - Deck    –> contains multiple Card objects​
    - Player  –> represents a player of the game (both human and AI), contains information of their hand, handles placing a card​
    - AI      –> contains logic for different difficulties (governs the ai player's next move)​
    - Game    –> manages the Player objects, the Deck, and the current state of the game​
    - Ruleset –> tells Deck and Game how to initialize and run, and determines what is considered a valid move

- ### Menus
    - Main Menu          –> The home screen of the game​
    - Play Menu          –> Asks the user to choose between single player and multiplayer​
    - Settings Menu      –> Registration and login profiles​
    - Single player Menu –> User chooses how many bots and the difficulty​
    - Game Window        –> The game screen with all the animations and gameplay​
    - End Menu           –> Displays the winner and allows user to play again or quit game
 
 ![image](https://user-images.githubusercontent.com/82806112/166127080-0448a3a9-6747-40ee-8e61-fd999bcb1769.png)
