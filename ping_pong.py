import curses
import random
import time

# Dimensions
HEIGHT = 20
WIDTH = 60
PADDLE_HEIGHT = 4

BALL_CHAR = 'o'
PADDLE_CHAR = '|'

# AI difficulty settings
AI_FAIL_CHANCE = 0.01  # small chance AI will fail to move optimally


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(50)

    # Initial positions
    user_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    ai_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    vel_x = -1
    vel_y = random.choice([-1, 1])

    while True:
        stdscr.clear()
        # Draw borders
        for x in range(WIDTH + 1):
            stdscr.addch(0, x, '-')
            stdscr.addch(HEIGHT, x, '-')
        for y in range(HEIGHT + 1):
            stdscr.addch(y, 0, '|')
            stdscr.addch(y, WIDTH, '|')

        # Draw paddles
        for i in range(PADDLE_HEIGHT):
            stdscr.addch(user_y + i, 2, PADDLE_CHAR)
            stdscr.addch(ai_y + i, WIDTH - 3, PADDLE_CHAR)

        # Draw ball
        stdscr.addch(ball_y, ball_x, BALL_CHAR)
        stdscr.refresh()

        # Input handling
        try:
            key = stdscr.getkey()
        except Exception:
            key = None
        if key == 'a' and user_y > 1:
            user_y -= 1
        elif key == 'd' and user_y + PADDLE_HEIGHT < HEIGHT:
            user_y += 1
        elif key in ('q', 'Q'):
            break

        # AI movement
        if random.random() > AI_FAIL_CHANCE:
            if ai_y + PADDLE_HEIGHT // 2 < ball_y and ai_y + PADDLE_HEIGHT < HEIGHT:
                ai_y += 1
            elif ai_y + PADDLE_HEIGHT // 2 > ball_y and ai_y > 1:
                ai_y -= 1

        # Move ball
        ball_x += vel_x
        ball_y += vel_y

        # Collision with top/bottom
        if ball_y <= 1 or ball_y >= HEIGHT - 1:
            # Reverse vertical direction when hitting top or bottom
            vel_y = -vel_y
        
        # Collision with paddles
        if ball_x == 3:
            if user_y <= ball_y < user_y + PADDLE_HEIGHT:
                vel_x = 1
            else:
                # AI scores
                stdscr.addstr(HEIGHT // 2, WIDTH // 2 - 5, 'You Lose!')
                stdscr.refresh()
                time.sleep(2)
                break
        elif ball_x == WIDTH - 4:
            if ai_y <= ball_y < ai_y + PADDLE_HEIGHT:
                vel_x = -1
            else:
                stdscr.addstr(HEIGHT // 2, WIDTH // 2 - 5, 'AI Loses!')
                stdscr.refresh()
                time.sleep(2)
                break

        time.sleep(0.02)


if __name__ == '__main__':
    curses.wrapper(main)
