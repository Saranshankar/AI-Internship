import cv2
import numpy as np
import random

# Window size
WIDTH = 800
HEIGHT = 500

# Bow position
bow_x = 70
bow_y = HEIGHT // 2

# Arrow
arrow_x = bow_x
arrow_y = bow_y
arrow_speed = 20
shoot =False

# Fruit
fruit_radius = 25
fruit_x = random.randint(500, WIDTH - 50)
fruit_y = 0
fruit_speed = 4

score = 0

while True:
    frame = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)

    # Move fruit downward
    fruit_y += fruit_speed

    # New fruit if missed
    if fruit_y > HEIGHT:
        fruit_x = random.randint(500, WIDTH - 50)
        fruit_y = 0

    # Draw fruit
    cv2.circle(frame, (fruit_x, fruit_y), fruit_radius, (0, 0, 255), -1)

    # Draw bow
    cv2.ellipse(frame, (bow_x, bow_y), (15, 40), 0, -90, 90, (0, 255, 255), 3)
    cv2.line(frame, (bow_x, bow_y - 40), (bow_x, bow_y + 40), (255, 255, 255), 2)

    # Shoot arrow
    if shoot:
        arrow_x += arrow_speed

    # Draw arrow
    cv2.arrowedLine(frame,
                    (arrow_x, arrow_y),
                    (arrow_x + 40, arrow_y),
                    (0, 255, 0), 4)

    # Collision detection
    tip_x = arrow_x + 40
    tip_y = arrow_y

    distance = np.sqrt((tip_x - fruit_x) ** 2 + (tip_y - fruit_y) ** 2)

    if distance < fruit_radius:
        score += 1

        # New fruit
        fruit_x = random.randint(500, WIDTH - 50)
        fruit_y = 0

        # Reset arrow
        arrow_x = bow_x
        shoot = False

    # Arrow leaves screen
    if arrow_x > WIDTH:
        arrow_x = bow_x
        shoot = False

    # Show score
    cv2.putText(frame, f"Score : {score}",
                (600, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2)

    cv2.imshow("Fruit Archery Game", frame)

    key = cv2.waitKey(20) & 0xFF

    # SPACE to shoot
    if key == 32 and not shoot:
        shoot = True

    # q to quit
    if key == ord('q'):
        break


cv2.destroyAllWindows()