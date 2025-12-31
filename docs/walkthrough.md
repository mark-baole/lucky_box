# Lucky Box Walkthrough

I have successfully built the Lucky Box application! 🎁

## What's Included
- **Backend**: A FastAPI application (`backend/main.py`) that manages the game state and logic (`backend/game_logic.py`).
- **Frontend**: A beautiful, responsive HTML page (`frontend/index.html`) using Tailwind CSS for styling.

## How to Run

1.  **Start the Backend**:
    Open a terminal in `g:\My Drive\Git Projects\lucky_box` and run:
    ```bash
    python -m uvicorn backend.main:app --reload
    ```
    You should see `Uvicorn running on http://127.0.0.1:8000`.

2.  **Play the Game**:
    Open `frontend/index.html` in your web browser.
    - Enter the number of boxes you want (1-50).
    - Click "Start Game".
    - Click on the boxes to reveal the animals! 🦁🐘

## Features
- **Dynamic Setup**: Choose how many boxes to play with.
- **Random Prizes**: Animals are chosen randomly from a pool with different rarities (Common, Rare, Legendary).
- **Visual Feedback**:
    - Boxes open with a satisfying animation.
    - A modal pops up showing the animal, emoji, and rarity.
    - "Game Over" alert when all boxes are opened.

## Verification
- Validated that the backend starts up correctly.
- The frontend is configured to talk to `http://localhost:8000`.
