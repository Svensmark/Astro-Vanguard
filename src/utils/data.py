"""
Module for Data and related classes
"""
import dataclasses
from utils.json_reader import FileReader

@dataclasses.dataclass
class Data:
    """
    Class for Data
    """
    game_data: 'GameData'
    player_data: 'PlayerData'
    enemy_data: 'EnemyData'
    spawner_data: 'SpawnerData'
    asset_data: 'AssetData'

    def __init__(self):
        file_reader = FileReader()
        assets = file_reader.read_json("assets.json")
        self.game_data = GameData(**file_reader.read_json("game.json"))
        self.player_data = PlayerData(**file_reader.read_json("player.json"))
        self.enemy_data = EnemyData(**file_reader.read_json("enemy.json"))
        self.spawner_data = SpawnerData(**file_reader.read_json("spawner.json"))
        self.asset_data = AssetData(
            sounds=SoundsData(**assets['sounds']),
            images=ImageData(**assets['images'])
        )

@dataclasses.dataclass
class GameData:
    """
    Class for GameData
    """
    screen_width: int
    screen_height: int
    fps: int
    score: int = 0
    lazers: list = dataclasses.field(default_factory=list)
    enemies: list = dataclasses.field(default_factory=list)
    
    def reset(self):
        self.score = 0
        self.lazers.clear()
        self.enemies.clear()

@dataclasses.dataclass
class PlayerData:
    """
    Class for PlayerData
    """
    width: int
    height: int
    start_x: int
    start_y: int
    max_hp: int
    velocity: int  # Initial velocity
    acceleration: int  # Acceleration factor
    max_speed: int  # Maximum speed
    friction: int  # Friction factor
    shoot_cooldown: int  # Shoot cooldown timer
    current_shoot_cooldown: int = 0
    current_hp: int = dataclasses.field(init=False)

    def __post_init__(self):
        self.current_hp = self.max_hp
        
    def reset(self):
        self.current_hp = self.max_hp
        self.current_shoot_cooldown = 0

@dataclasses.dataclass
class EnemyData:
    """
    Class for EnemyData
    """
    width: int
    height: int
    spawn_rate: int
    

@dataclasses.dataclass
class SpawnerData:
    """
    Class for SpawnerData
    """
    spawn_cooldown: int
    enemy_ships: list

@dataclasses.dataclass
class AssetData:
    """
    Class for AssetData
    """
    sounds: 'SoundsData'
    images: 'ImageData'

@dataclasses.dataclass
class SoundsData:
    """
    Class for SoundsData
    """
    player_death: str
    lazer: str
    enemy_death: str
    menu_select: str
    menu_hover: str

@dataclasses.dataclass
class ImageData:
    """
    Class for ImageData
    """
    menu_btn: str
