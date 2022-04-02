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
- [ ] Implement test steps of legal move illegal move
    - [ ] square [1,1] is occupied
    - [ ] game notifies player the square is occupied
    - [ ] the game does not break
    - [ ] state of game does not change
