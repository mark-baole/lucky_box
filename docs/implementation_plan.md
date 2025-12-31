# Lucky Box Implementation Plan

## Goal
Build a web application "Lucky Box" where a child can open virtual boxes to reveal animal prizes.

## User Review Required
> [!NOTE]
> The current design uses in-memory storage for simplicity. Game state will be lost if the server restarts.

## Proposed Changes

### Backend (Python/FastAPI)
- **Framework**: FastAPI
- **API Definition**: Use existing `openapi.yaml` as the contract.
- **State Management**: Simple in-memory class `GameManager`.
- **Data**: A hardcoded list of animals (Lion 🦁, Elephant 🐘, etc.) with rarity weights.

#### [NEW] [main.py](file:///g:/My%20Drive/Git%20Projects/lucky_box/backend/main.py)
- FastAPI app entry point.
- Implementation of `/game/setup` and `/box/open` endpoints.
- CORS middleware configuration.

#### [NEW] [game_logic.py](file:///g:/My%20Drive/Git%20Projects/lucky_box/backend/game_logic.py)
- `Game` class to hold state (total boxes, opened count).
- Logic to pick a random animal from the pool.

### Frontend (HTML/JS/Tailwind)
- **Tech**: Single HTML file with embedded script and Tailwind via CDN (for simplicity/speed) or a basic Vite setup if preferred. Given the "simple" requirement, a standalone HTML file or a simple static structure served by FastAPI is efficient.
- **Design**:
    - **Setup Screen**: Input for number of boxes, "Start Game" button.
    - **Game Screen**: Grid of closed boxes.
    - **Interaction**: Clicking a box triggers the API.
    - **Reveal**: Modal or overlay showing the animal emoji and name.

#### [NEW] [index.html](file:///g:/My%20Drive/Git%20Projects/lucky_box/frontend/index.html)
- Main UI structure.
- Tailwind CSS classes for styling.
- JavaScript for API communication and DOM manipulation.

## Verification Plan

### Automated Tests
- Run `pytest` for backend logic (game setup, opening boxes, game over state).

### Manual Verification
1.  Start the backend server.
2.  Open `index.html` in a browser.
3.  Enter a number of boxes (e.g., 5) and start.
4.  Click boxes and verify animals are revealed.
5.  Verify "Game Over" or empty state when all boxes are opened.
