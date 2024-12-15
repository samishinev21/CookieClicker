import pygame
import asyncio
import os

TITLE = "Cookie Clicker"
HEIGHT = 720
WIDTH = 1280

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

clicks = 0

cookie_image = pygame.image.load("images/cookie.png")
cookie = pygame.Rect(CENTER_X - cookie_image.get_width() // 2,
                     CENTER_Y - cookie_image.get_height() // 2,
                     cookie_image.get_width(),
                     cookie_image.get_height())

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

font = pygame.font.Font(None, 100)


def draw():
    screen.fill("cyan")
    screen.blit(cookie_image, (cookie.x, cookie.y))
    text = font.render(str(clicks), True, "black")
    screen.blit(text, (CENTER_X - text.get_width() // 2, CENTER_Y - 350))


async def main():
    global clicks

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if cookie.collidepoint(event.pos):
                    clicks += 1

        draw()
        pygame.display.flip()

        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())