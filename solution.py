from gym_line_follower.helper import LaRoboLigaEnv

if __name__ == "__main__":
    husky = LaRoboLigaEnv()
    velocity = 1.0  # Velocity
    while True:
        husky.set_velocity([velocity, velocity])
