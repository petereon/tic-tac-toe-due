## Refactoring strategy
- Make game state reflected in dictionary structure
- Move visualizations out of domain logic
- Make API that can be requested for game-state
- Make API that can be requested for player action

---


### Pomodoro 0:
- __April 2nd 2022__

__Focus: Setup__
- [x] Precommit hook for conventional commits
- [x] Precommit hook for formatting ~~& linting~~

---

### Pomodoro 1:
- __April 2nd 2022__

__Focus: Domain logic__
- [x] BDD feature descriptions for basic moves
    - [x] Legal move
    - [x] Illegal move

---

### Pomodoro 2:
- __April 2nd 2022__

__Focus: Domain logic__
- [X] Implement test steps of legal move
    - [X] a game is in progress
    - [X] the player is "X"
    - [X] square [0,1] is unoccupied
    - [X] player makes a move at [0,1]
    - [X] square [0,1] is occupied by "X"
    - [X] the player is "O"
- [X] Outline refactoring strategy

---


### Pomodoro 3:
- __April 3rd 2022__

__Focus: Domain logic__
- [x] Implement test steps of legal move illegal move
    - [x] square [1,1] is occupied
- [x] Implement test steps for out of board move
    - [x] player makes a move at [3,3]
    - [x] the game breaks

### Pomodoro 4:
- __April 3rd 2022__

__Focus: Domain logic__
- [x] Implement features for endgame
    - [x] the game is a draw
    - [x] player "X" wins
    - [x] player "O" wins

Seems like all the desired logic in the game is now sufficiently described in the BDD tests, moving on to the unit tests to cover the remaining logic.

### Pomodoro 5:
- __April 3rd 2022__

__Focus: Domain logic__
- [ ] Unit test functions
    - [x] `generate_board`
    - [x] `generate_board_repr`
    - [ ] `player_sign`
    - [ ] `assess_game`
    - [ ] `process_round`
    - [ ] `play_game`

### Pomodoro 6:
- __April 3rd 2022__

__Focus: Domain logic__
- [ ] Unit test functions
    - [x] ~~`generate_board`~~
    - [x] ~~`generate_board_repr`~~
    - [ ] `player_sign`
    - [ ] `assess_game`
    - [ ] `process_round`
    - [ ] `play_game`