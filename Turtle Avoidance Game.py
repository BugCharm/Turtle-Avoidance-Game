import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Avoidance Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(0, -250)
player.speed(0)
player.shapesize(stretch_wid=2, stretch_len=2)  # Enlarged player

# Create the score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Create obstacles
obstacles = []
colors = ["red", "green", "blue", "orange", "purple", "pink"]
max_obstacles = 15  # Maximum number of obstacles on screen

# Player movement
def go_left():
    x = player.xcor()
    x -= 40
    if x < -280:
        x = -280
    player.setx(x)

def go_right():
    x = player.xcor()
    x += 40
    if x > 280:
        x = 280
    player.setx(x)

screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Game mechanics
score = 0
obstacle_speed = 5

def update_score():
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

def create_obstacle():
    if len(obstacles) < max_obstacles:
        obstacle = turtle.Turtle()
        obstacle.shape("circle")
        obstacle.color(random.choice(colors))
        obstacle.penup()
        obstacle.speed(0)
        obstacle.shapesize(stretch_wid=2, stretch_len=2)
        x = random.randint(-290, 290)
        y = random.randint(300, 400)
        obstacle.goto(x, y)
        obstacles.append(obstacle)

try:
    while True:
        screen.update()
        time.sleep(0.02)

        # Gradually increase speed
        obstacle_speed += 0.005

        # Randomly create obstacles
        if random.randint(1, 20) == 1:  # Random chance to create a new obstacle
            create_obstacle()

        for obstacle in obstacles:
            y = obstacle.ycor()
            y -= obstacle_speed
            obstacle.sety(y)

            # Reset the obstacle
            if y < -300:
                obstacles.remove(obstacle)
                obstacle.clear()
                score += 10
                update_score()

            # Collision check
            if player.distance(obstacle) < 30:
                print("Game over! Final Score:", score)
                time.sleep(2)
                screen.bye()
                break
except turtle.Terminator:
    print("Game closed.")
