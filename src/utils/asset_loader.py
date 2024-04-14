"""
Module for loading assets using pygame and pygame.mixer.
"""
from pygame import mixer


def sprite_loader(pygame, asset: str):
    """
    Load a sprite image using pygame.

    Args:
        pygame: The pygame module.
        asset: The path to the asset file.

    Returns:
        The loaded sprite image.
    """
    return pygame.image.load(asset).convert_alpha()


def sound_loader(asset: str):
    """
    Load a sound using pygame.mixer.

    Args:
        asset: The path to the asset file.

    Returns:
        The loaded sound.
    """
    return mixer.Sound(asset)
