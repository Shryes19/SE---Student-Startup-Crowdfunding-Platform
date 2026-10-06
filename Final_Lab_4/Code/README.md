# Missile Command — Lab 4 Final Code

Source repository: https://github.com/SETAPESU26/33_missileCommand

## Run

```bash
pip install pygame
python game.py
```

## Completed Lab Tasks

1. **Battery selection bug fixed:** `nearest_battery()` now considers only batteries that are alive and have ammunition.
2. **Explosion color implemented:** explosions transition from white-hot through yellow/orange to red as they fade.
3. **City-destruction feedback implemented:** a visible warning is shown when a city is destroyed, with a stronger warning when only two or fewer cities remain.
4. **City repair implemented:** one destroyed city is automatically restored whenever the score crosses a 2000-point threshold.

The interceptor movement was also made robust so it snaps to the target when a frame would otherwise overshoot it.
