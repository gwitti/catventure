# Catventure Game - Final Project for CS50P
Catventure is a simple and family-friendly game built with Pygame, where players control a cat navigating through a magical forest while avoiding drops of water. The game is designed to be easy to play and understand, making it suitable for both young kids and inexperienced adults.
#### Video Demo: <https://youtu.be/7Ohl4djzLTE>

## instructions
+ #### Press "Space" key to start/restart the game
The game begins with an opening screen, and to initiate or restart the game, simply press the "Space" key when ready. This simplicity in controls makes the game accessible for players of all ages.
+ #### Avoid colliding with mooving objects
Controlling the cat's movement is as straightforward as pressing the "Space" key. The game's sole control mechanism simplifies the gaming experience, especially for younger players or those new to gaming.
+ #### Your score is displayed on the screen
The game revolves around a scoring system that is continually displayed on the screen. The score resets to zero each time the player chooses to restart the game, providing a fresh start for every attempt.


## Gameplay
In this magical forest adventure, the obstacle is a drop of water that jumps through the forest. Cats typically dislike water, adding a whimsical and non-violent element to the game. This intentional design choice ensures that the game is suitable for players of all ages, including children.

## Features
+ #### Responsive cat animation
 Pressing the "Space" key triggers a jumping cat animation, while the cat walks on the ground when the key is not pressed. This feature enhances the user's understanding of basic physics within the game and contributes to an enjoyable gaming experience.
+ #### Score Tracking
Catventures scoring system tracks time units instead of counting passed obstacles. This approach encourages less experienced players to feel positive about their scores and motivates them to improve their skills further, it can be also very rewarding for kids.

## Credits
game assets: OpenGameArt.org
Font: PixelPowerline
Cat and Drop assets: Natalia Mostova

## Architechture of the programm
+ #### Game Loop and Clock
The `main` game loop `while True` continuously runs, handling events and updating the game state.
`clock = pygame.time.Clock():` Creates a Pygame clock object to control the frame rate.
+ #### Fonts and Graphics
`test_font:` Loads the PixelPowerline font with a size of 50 for displaying text on the screen.
`woods_surface:` Loads the background image for the magical forest.
`cat_stand, game_name, and game_message:` Initialize images and text surfaces for the introduction screen.
+ #### Player Cat - Cat Class
The `Cat` class encapsulates the cat's properties and behavior.
`cat_animation():` Manages the cat's animation based on its position and state.
`cat_surface` and `cat_rect:` Represent the cat's current image and position on the screen.
`cat_gravity:` Controls the vertical movement of the cat.
+ #### Obstacles - Drop Class
The `Drop` class represents the water drops, acting as obstacles.
`drop_animation():` Manages the animation of the water drops as they move across the screen.
`drop_surface` and `drop_rect:` Represent the current image and position of the water drops.
+ #### Main Game Logic
The `main()` function orchestrates the overall flow of the game.
Handles user input, updates the game state, and renders the graphics accordingly.
Uses instances of the Cat and Drop classes for managing player and obstacle interactions.
Implements collision detection between the cat and water drops.
+ #### Game State Management
`game_active:` A flag indicating whether the game is currently active or not.
`start_time and score:` Keep track of the game's start time and the player's score.
+ #### Event Handling
Pygame events, such as key presses and window closures, are processed within the main game loop.
Game starts or restarts on the press of the "Space" key.
+ #### Screen Rendering
Screens are rendered using Pygame's `blit` function, displaying background images, text, and game elements.
+ #### Scoring System
The game uses a time-based scoring system, calculating the `score` as the elapsed time in seconds.
