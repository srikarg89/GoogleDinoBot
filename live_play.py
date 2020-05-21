#https://dino-chrome.com/

import pyautogui
import cv2
import numpy as np
import time

def choose_action(nearest_x, nearest_w, nearest_h):
    x = 510
    width = 68
    jump_v = 50.2
    g = 9.1
    speed = 1000 / 20

    dist = nearest_x - x - width
    print(dist)
    if dist < 10:
        # Panic jump
        return 1

    dist_end = nearest_x + nearest_w - x
    # Kinematics to figure out how far dino will travel during jump
    t_apex = jump_v / g
    h_apex = (jump_v ** 2) / (2 * g)
    h_obs = nearest_h
    h_diff = h_apex - h_obs
    t_obs = (2 * h_diff / g) ** (1/2)
    #        print(t_apex, t_obs)
    t = t_apex + t_obs
    travel_dist = speed * t
    print(speed, t)
    print(travel_dist)
    # Buffer so u don't keep it toooo close
    buffer = 10

    if travel_dist + buffer > dist_end:
        return 1
    return 0

#im = pyautogui.screenshot(region=(300,400,1200,500))
time.sleep(1)
#dino_loc = pyautogui.locateOnScreen('images/dino.PNG', confidence=.60)
def get_obstacles():
    obs_locs = pyautogui.locateAllOnScreen('images/cactus1.PNG', confidence=.6)
    obs_locs2 = pyautogui.locateAllOnScreen('images/cactus4.PNG', confidence=.6)
    obs_locs = [i for i in obs_locs] + [i for i in obs_locs2]
    if len(obs_locs) == 0:
        return []
    obs_locs = sorted(obs_locs, key = lambda obs: obs.left)
    merged = []
    last = obs_locs[0]
    merged.append([last.left, last.left + last.width, last.height])
    for i in obs_locs[1:]:
        if i.left - last.left < 50:
            merged[-1][1] = i.left + i.width
            merged[-1][1] = max(merged[-1][1], i.height)
        else:
            merged.append([i.left, i.left + i.width, i.height])
        last = i
    print("NUMBER OF OBSTACLES", len(merged))
    return merged

is_jumping = False
jump_time = 0
for i in range(100):
    if is_jumping:
        while time.time() - jump_time < .4:
            pass
#            print("JUMPING")
        is_jumping = False
    obstacles = get_obstacles()
    obstacles = sorted(obstacles, key = lambda obs: obs[0])
    if len(obstacles) > 0:
        nearest = obstacles[0]
        action = choose_action(nearest[0], nearest[1]-nearest[0], nearest[2])
        print(action)
        if action == 1:
            pyautogui.press('space')
            is_jumping = True
            jump_time = time.time()
    else:
        print(0)
#    time.sleep(.01)

#for i in range(100):
#    print(len(get_obstacles()))