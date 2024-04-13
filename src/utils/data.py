from utils.json_reader import File_reader

class Data():
    def __init__(self):
        file_reader_game = File_reader()
        game_data = file_reader_game.read_json("game.json")
        player_data = file_reader_game.read_json("player.json")
        enemy_data = file_reader_game.read_json("enemy.json")
        spawner_data = file_reader_game.read_json("spawner.json")
        asset_data = file_reader_game.read_json("assets.json")

        global game_data_instance, player_data_instance, enemy_data_instance, spawner_data_instance, asset_data_instance
        game_data_instance = GameData(game_data)
        player_data_instance = PlayerData(player_data)
        enemy_data_instance = EnemyData(enemy_data)
        spawner_data_instance = SpawnerData(spawner_data)
        asset_data_instance = AssetData(asset_data)


    def get_game_data(self):
        return game_data_instance

    def get_player_data(self):
        return player_data_instance

    def get_enemy_data(self):
        return enemy_data_instance

    def get_spawner_data(self):
        return spawner_data_instance

    def get_asset_data(self):
        return asset_data_instance


class GameData():
    def __init__(self, game_data):
        self.screen_width = game_data['screen_width']
        self.screen_height = game_data['screen_height']
        self.fps = game_data['fps']
        self.score = 0
        self.lazers = []
        self.enemies = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)


class PlayerData():
    def __init__(self, player_data):
        self.width = player_data['width']
        self.height = player_data['height']
        self.current_shoot_cooldown = 0
        self.x = player_data['start_x']
        self.y = player_data['start_y']
        self.max_hp = player_data['max_hp']
        self.current_hp = self.max_hp

        self.velocity = player_data['velocity']  # Initial velocity
        self.acceleration = player_data['acceleration']  # Acceleration factor
        self.max_speed = player_data['max_speed']  # Maximum speed
        self.friction = player_data['friction']  # Friction factor
        self.shoot_cooldown = player_data['shoot_cooldown']  # Shoot cooldown timer


class EnemyData():
    def __init__(self, enemy_data):
        self.spawn_rate = enemy_data['spawn_rate']
        #self.spawn_rate = 0


class SpawnerData():
    def __init__(self, spawner_data):
        self.spawn_rate = spawner_data['spawn_cooldown']
        self.enemy_ships = spawner_data['enemy_ships']


class AssetData():
    def __init__(self, asset_data):
        self.sounds = SoundsData(asset_data['sounds'])
        self.images = ImageData(asset_data['images'])


class SoundsData():
    def __init__(self, sounds_data):
        self.player_death = sounds_data['player_death']
        self.lazer = sounds_data['lazer']
        self.enemy_death = sounds_data['enemy_death']

        self.menu_select = sounds_data['menu_select']
        self.menu_hover = sounds_data['menu_hover']


class ImageData():
    def __init__(self, image_data):
        # self.player = image_data['player']
        # self.enemy = image_data['enemy']
        # self.lazer = image_data['lazer']
        # self.background = image_data['background']

        self.menu_btn = image_data['menu_btn']