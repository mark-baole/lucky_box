# Deployment Guide for Lucky Box

To let others play your game, you can deploy it to a free cloud hosting service like **Render**.

## Prerequisites
- You have a GitHub account.
- You have pushed this code to a GitHub repository.

## Steps to Deploy on Render

1.  **Sign Up/Login**: Go to [render.com](https://render.com) and log in with your GitHub account.
2.  **New Web Service**: Click "New +" and select "Web Service".
3.  **Connect Repository**: Find your `lucky_box` repository and click "Connect".
4.  **Configure**:
    - **Name**: `lucky-box-game` (or similar)
    - **Runtime**: `Python 3`
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5.  **Deploy**: Click "Create Web Service".

Render will build your app and give you a URL (e.g., `https://lucky-box-game.onrender.com`). Share this URL with your friends!

## Alternative: Temporary Sharing with Ngrok
If you just want to show it quickly without deploying:
1.  Download [ngrok](https://ngrok.com/).
2.  Run your local server: `python -m uvicorn backend.main:app --reload`
3.  In a new terminal, run: `ngrok http 8000`
4.  Copy the `https://...ngrok-free.app` URL and share it.
