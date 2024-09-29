import pygame

from dataclasses import dataclass


@dataclass
class Colors:
    """A class to hold color constants for the Pygame application."""

    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)


class PygameApplication:
    """A class to represent the main Pygame application."""

    def __init__(
        self, window_width: int, window_height: int, window_title: str, fps: int
    ) -> None:
        """Initialize the Pygame application.

        Args:
            window_width (int): The width of the application window.
            window_height (int): The height of the application window.
            window_title (str): The title of the application window.
            fps (int): The frames per second for the application.
        """
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(window_title)

        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        self.running = False
        self.fps = fps

    def process_pygame_events(self):
        """Process Pygame events and update the application state.

        This method checks for events like quitting the application.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        """Run the main loop of the Pygame application.

        This method handles event processing, updating game logic,
        and rendering frames to the display.
        """
        self.running = True

        while self.running:
            self.process_pygame_events()

            delta_time: float = self.clock.tick(self.fps) / 1000

            # Call the update method with the delta time
            self.on_tick(delta_time)

            # Clear the screen with the background color
            self.screen.fill(Colors.Black)

            # Call the draw method to render game elements
            self.on_draw()

            # Update the display with the drawn frame
            pygame.display.flip()

    def on_tick(self, dt: float):
        """Update game logic based on the time elapsed.

        Args:
            dt (float): The time elapsed since the last frame, in seconds.
        """
        # TODO: Implement your game logic here.
        print(f"Delta time: {dt}")

    def on_draw(self):
        """Draw game elements on the screen.

        This method is where you should put your drawing code.
        """
        # TODO: Add the elements you want to draw here.
        # For exemple : draw a red square in the center of the screen
        pygame.draw.rect(
            self.screen, Colors.Red, pygame.Rect(300 - 30, 300 - 30, 60, 60)
        )


if __name__ == "__main__":
    app = PygameApplication(
        window_width=600, window_height=600, window_title="Application Name", fps=60
    )
    app.run()
