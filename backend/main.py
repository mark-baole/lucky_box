from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from .game_logic import GameState
import os

app = FastAPI(title="Lucky Box Game", version="1.0.0")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global game state (in-memory)
game_state: Optional[GameState] = None

class GameSetupRequest(BaseModel):
    box_count: int

@app.post("/game/setup", status_code=status.HTTP_201_CREATED)
def setup_game(request: GameSetupRequest):
    global game_state
    if request.box_count < 1 or request.box_count > 50:
         raise HTTPException(status_code=400, detail="Box count must be between 1 and 50")
    
    game_state = GameState(total_boxes=request.box_count)
    return {"message": "Game initialized", "total_boxes": request.box_count}

@app.post("/box/open")
def open_box():
    global game_state
    if game_state is None:
        raise HTTPException(status_code=400, detail="Game not started. Please call /game/setup first.")
    
    result = game_state.open_box()
    if result is None:
        raise HTTPException(status_code=400, detail="No boxes left to open")
        
    return result

# Mount frontend directory
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('frontend/index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
