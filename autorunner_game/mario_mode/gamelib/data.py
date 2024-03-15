import os, pygame
from pygame.locals import *

data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, '..', 'data'))

def filepath(filename):
    """
    Returns the absolute file path for the given filename.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The absolute file path.
    """
    return os.path.join(data_dir, filename)

def load(filename, mode='rb'):
    """
    Opens and returns a file object for the given filename.

    Args:
        filename (str): The name of the file.
        mode (str, optional): The mode in which the file should be opened. Defaults to 'rb'.

    Returns:
        file: The file object.
    """
    return open(os.path.join(data_dir, filename), mode)

def load_image(filename):
    """
    Loads and returns an image from the given filename.

    Args:
        filename (str): The name of the image file.

    Returns:
        pygame.Surface: The loaded image as a pygame Surface object.
    """
    filename = filepath(filename)
    try:
        image = pygame.image.load(filename)
        image = pygame.transform.scale(image, (image.get_width()*2, image.get_height()*2))
    except pygame.error:
        raise SystemExit( "Unable to load: " + filename)
    return image.convert_alpha()

def load_sound(filename, volume=0.5):
    """
    Loads and returns a sound from the given filename.

    Args:
        filename (str): The name of the sound file.
        volume (float, optional): The volume of the sound. Defaults to 0.5.

    Returns:
        pygame.mixer.Sound: The loaded sound as a pygame Sound object.
    """
    filename = filepath(filename)
    try:
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(volume)
    except:
        raise SystemExit( "Unable to load: " + filename)
    return sound

def play_music(filename, volume=0.5, loop=-1):
    """
    Loads and plays music from the given filename.

    Args:
        filename (str): The name of the music file.
        volume (float, optional): The volume of the music. Defaults to 0.5.
        loop (int, optional): The number of times the music should loop. -1 for infinite loop. Defaults to -1.
    """
    filename = filepath(filename)
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)
    except:
        raise SystemExit( "Unable to load: " + filename)

def stop_music():
    """
    Stops the currently playing music.
    """
    pygame.mixer.music.stop()
