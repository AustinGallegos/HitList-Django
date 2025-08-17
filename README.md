# HitList - Django

## Overview
A refactored version of HitList in Python's Django framework: a full-stack web app that integrates with the **Spotify Web API**.  
Users can search for songs, submit daily entries, and view a randomly selected **Hit of the Day**.  
Authenticated users can stream the featured track directly on their active Spotify device.

## Tech Stack
- **Python** (os, sys, dotenv, urllib)
- Django
- Requests
- Celery
- **PostgreSQL**
- HTML/CSS, JavaScript

## Features
- Search for songs using Spotify's Web API  
- Submit daily entries (resets every 24 hours)  
- Randomly select and display the "Hit of the Day"  
- Playback directly on a logged-in Spotify device  

## Setup
1. Clone the repo  
2. Install dependencies (requirements.txt)
3. Run the app (main.py)
