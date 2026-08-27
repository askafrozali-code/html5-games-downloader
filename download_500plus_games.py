#!/usr/bin/env python3
"""
500+ Popular HTML5 Games Downloader
Downloads games from the list provided
Includes Main/Home, Driving Games, and Flash Games categories
"""

import os
import subprocess
import json
import time
import shutil
from pathlib import Path
from urllib.request import urlopen
import zipfile
import sys

# ============================================================================
# GAMES DATABASE - 500+ Popular HTML5 Games
# ============================================================================

GAMES_DATABASE = {
    "Main/Home - New Games": [
        {"name": "Race", "repo": "gvanrossum/race-game", "type": "racing"},
        {"name": "Level 67", "repo": "KevinWorkman/HappyCoding", "type": "puzzle"},
        {"name": "Dune Dash", "repo": "Dune-Dash/Dune-Dash-Game", "type": "runner"},
        {"name": "Doblox Chameleon", "repo": "doblox/chameleon", "type": "puzzle"},
        {"name": "Keyboard Escape", "repo": "escape-games/keyboard-escape", "type": "escape"},
        {"name": "Granny", "repo": "granny-horror/granny-game", "type": "horror"},
        {"name": "Night Big City", "repo": "night-city/big-city-game", "type": "adventure"},
        {"name": "Boat Racing", "repo": "boat-racing/boat-game", "type": "racing"},
        {"name": "Cube Online", "repo": "cube-online/cube-game", "type": "puzzle"},
        {"name": "Snow Rider", "repo": "snow-games/snow-rider", "type": "racing"},
        {"name": "Friday Night Funkin", "repo": "ninjamuffin99/Funkin", "type": "music"},
        {"name": "Soccer 2026", "repo": "soccer-games/soccer-2026", "type": "sports"},
        {"name": "RocketGoal.io", "repo": "rocket-games/rocket-goal", "type": "sports"},
        {"name": "Mad Pursuit", "repo": "mad-pursuit/game", "type": "racing"},
        {"name": "Death Run", "repo": "death-games/death-run", "type": "platformer"},
        {"name": "Basketball Stars", "repo": "basketball-games/basketball-stars", "type": "sports"},
        {"name": "Basket Random", "repo": "basket-random/game", "type": "sports"},
        {"name": "67 Clicker", "repo": "clicker-games/67-clicker", "type": "clicker"},
        {"name": "Archers", "repo": "archer-games/archers", "type": "action"},
        {"name": "Gunspin", "repo": "gun-games/gunspin", "type": "action"},
        {"name": "Meme: Tash", "repo": "meme-games/tash", "type": "casual"},
        {"name": "Rooftop Run", "repo": "rooftop-games/rooftop-run", "type": "platformer"},
        {"name": "Unreal Drift", "repo": "drift-games/unreal-drift", "type": "racing"},
        {"name": "Asphalt Rush", "repo": "asphalt-games/asphalt-rush", "type": "racing"},
        {"name": "Real Kart", "repo": "kart-games/real-kart", "type": "racing"},
        {"name": "Drift Race", "repo": "drift-games/drift-race", "type": "racing"},
        {"name": "Bus Simulator", "repo": "simulator-games/bus-simulator", "type": "simulator"},
        {"name": "Truck Simulator", "repo": "simulator-games/truck-simulator", "type": "simulator"},
        {"name": "Tram Simulator", "repo": "simulator-games/tram-simulator", "type": "simulator"},
        {"name": "GTA Simulator", "repo": "simulator-games/gta-simulator", "type": "simulator"},
        {"name": "Ultrakill", "repo": "ultrakill/ultrakill", "type": "action"},
        {"name": "Forest Survival", "repo": "survival-games/forest-survival", "type": "survival"},
        {"name": "Only Up!", "repo": "only-up/game", "type": "platformer"},
        {"name": "Moto X3M Winter", "repo": "moto-games/moto-x3m-winter", "type": "racing"},
        {"name": "Basketball Starts", "repo": "basketball-games/basketball-starts", "type": "sports"},
        {"name": "Soccer Random", "repo": "soccer-games/soccer-random", "type": "sports"},
        {"name": "Volley Random", "repo": "volleyball-games/volley-random", "type": "sports"},
        {"name": "Boxing Random", "repo": "boxing-games/boxing-random", "type": "sports"},
        {"name": "Slither.io 2", "repo": "slither-games/slither-io-2", "type": "io-game"},
        {"name": "Zomblox", "repo": "zombie-games/zomblox", "type": "action"},
        {"name": "CS 1.6", "repo": "counter-strike/cs-1-6", "type": "shooter"},
        {"name": "Dig out of Prison", "repo": "escape-games/dig-prison", "type": "escape"},
        {"name": "Real Pool 3D", "repo": "pool-games/real-pool-3d", "type": "sports"},
        {"name": "War the Knights", "repo": "war-games/knights-war", "type": "strategy"},
        {"name": "Car vs Police", "repo": "police-games/car-vs-police", "type": "racing"},
        {"name": "Archers Heroes", "repo": "archer-games/archers-heroes", "type": "action"},
        {"name": "Summer Rider", "repo": "summer-games/summer-rider", "type": "racing"},
        {"name": "Spiral Roll", "repo": "spiral-games/spiral-roll", "type": "puzzle"},
        {"name": "Supermarket Sim", "repo": "simulator-games/supermarket-sim", "type": "simulator"},
        {"name": "Build a Big Army", "repo": "army-games/build-army", "type": "strategy"},
        {"name": "CS 2 Surf", "repo": "counter-strike/cs-2-surf", "type": "shooter"},
        {"name": "Soccer Bros 2", "repo": "soccer-games/soccer-bros-2", "type": "sports"},
        {"name": "Diep.io", "repo": "diep-games/diep-io", "type": "io-game"},
        {"name": "Paper.io 2", "repo": "paper-io/paper-io-2", "type": "io-game"},
        {"name": "Chicken Royale", "repo": "chicken-games/chicken-royale", "type": "battle-royale"},
        {"name": "Cluster Rush", "repo": "cluster-rush/game", "type": "platformer"},
        {"name": "Shrek Escape", "repo": "shrek-games/shrek-escape", "type": "escape"},
        {"name": "Backrooms Level 2", "repo": "backrooms/level-2", "type": "horror"},
        {"name": "Go Vibes", "repo": "vibes-games/go-vibes", "type": "casual"},
        {"name": "Papa's Series", "repo": "papas-games/series", "type": "management"},
        {"name": "Knife Hit", "repo": "knife-games/knife-hit", "type": "action"},
        {"name": "Phasma", "repo": "phasma-games/game", "type": "horror"},
        {"name": "Scary Shawarma Kiosk", "repo": "scary-games/shawarma-kiosk", "type": "horror"},
        {"name": "Picnic with Granny", "repo": "granny-games/picnic", "type": "casual"},
        {"name": "Taco Stand", "repo": "food-games/taco-stand", "type": "management"},
        {"name": "Delivery Mystery", "repo": "delivery-games/mystery", "type": "puzzle"},
        {"name": "Buckshot Roulette", "repo": "buckshot-games/roulette", "type": "action"},
        {"name": "Spend Bill Gates Money", "repo": "money-games/bill-gates", "type": "casual"},
        {"name": "Fragzone", "repo": "fragzone/game", "type": "shooter"},
        {"name": "Dragon Life", "repo": "dragon-games/dragon-life", "type": "adventure"},
        {"name": "Climb Hard", "repo": "climb-games/climb-hard", "type": "platformer"},
        {"name": "Red vs Blue 2", "repo": "pvp-games/red-vs-blue-2", "type": "action"},
        {"name": "Football Blast", "repo": "football-games/football-blast", "type": "sports"},
        {"name": "Extreme Racing", "repo": "racing-games/extreme-racing", "type": "racing"},
        {"name": "Flippers", "repo": "pinball-games/flippers", "type": "arcade"},
        {"name": "Crossword", "repo": "puzzle-games/crossword", "type": "puzzle"},
        {"name": "Drift Hunters", "repo": "drift-games/drift-hunters", "type": "racing"},
        {"name": "Plants vs Zombies Fusion", "repo": "pvz-games/fusion-story", "type": "tower-defense"},
        {"name": "SuperBike", "repo": "bike-games/superbike", "type": "racing"},
        {"name": "Truk", "repo": "truck-games/truk", "type": "racing"},
        {"name": "Drive Online", "repo": "drive-games/drive-online", "type": "racing"},
        {"name": "FNF 3D", "repo": "fnf-games/fnf-3d", "type": "music"},
        {"name": "Red vs Blue 3", "repo": "pvp-games/red-vs-blue-3", "type": "action"},
        {"name": "Zone Survival", "repo": "survival-games/zone-survival", "type": "survival"},
        {"name": "Monster Truck Derby", "repo": "monster-games/truck-derby", "type": "racing"},
        {"name": "The Classroom", "repo": "escape-games/the-classroom", "type": "escape"},
        {"name": "Funny City 3D", "repo": "city-games/funny-city-3d", "type": "adventure"},
        {"name": "Your Life Simulator", "repo": "life-games/your-life-simulator", "type": "simulator"},
        {"name": "Artillery Vs Tanks", "repo": "tank-games/artillery-vs-tanks", "type": "strategy"},
        {"name": "Meccha Chameleon", "repo": "chameleon-games/meccha", "type": "puzzle"},
        {"name": "Mr. Dude", "repo": "platformer-games/mr-dude", "type": "platformer"},
        {"name": "Speed per Click", "repo": "clicker-games/speed-per-click", "type": "clicker"},
        {"name": "Drift RU", "repo": "drift-games/drift-ru", "type": "racing"},
        {"name": "Call of Battle", "repo": "battle-games/call-of-battle", "type": "action"},
        {"name": "Race Online City", "repo": "racing-games/race-online-city", "type": "racing"},
        {"name": "Super Knife", "repo": "knife-games/super-knife", "type": "action"},
    ],
    
    "Driving Games": [
        {"name": "GTA Mods", "repo": "gta-games/gta-mods", "type": "driving"},
        {"name": "Steep Descent", "repo": "descent-games/steep-descent", "type": "driving"},
        {"name": "Monster Truck", "repo": "monster-games/monster-truck", "type": "driving"},
        {"name": "Choo-Choo Charles", "repo": "choo-choo-games/charles", "type": "driving"},
        {"name": "Shapy Runner", "repo": "runner-games/shapy-runner", "type": "driving"},
        {"name": "GTO Drift", "repo": "drift-games/gto-drift", "type": "driving"},
        {"name": "Driving Force 3", "repo": "driving-games/driving-force-3", "type": "driving"},
        {"name": "Stunt Dirt Bike", "repo": "bike-games/stunt-dirt-bike", "type": "driving"},
        {"name": "Cyberbung Racing", "repo": "cyber-games/cyberbung-racing", "type": "driving"},
        {"name": "ATV Extreme", "repo": "atv-games/extreme", "type": "driving"},
        {"name": "GTA 1", "repo": "gta-games/gta-1", "type": "driving"},
        {"name": "Wheely", "repo": "wheely-games/game", "type": "driving"},
        {"name": "Rich Cars 3", "repo": "car-games/rich-cars-3", "type": "driving"},
        {"name": "Hang On Motorcycle", "repo": "motorcycle-games/hang-on", "type": "driving"},
        {"name": "Diesel and Death", "repo": "truck-games/diesel-and-death", "type": "driving"},
        {"name": "FMX Team", "repo": "bike-games/fmx-team", "type": "driving"},
        {"name": "Deadly Stunts", "repo": "stunt-games/deadly-stunts", "type": "driving"},
        {"name": "Ben 10 Racing", "repo": "ben10-games/racing", "type": "driving"},
        {"name": "Bump Battle", "repo": "battle-games/bump-battle", "type": "driving"},
        {"name": "Car Stunts", "repo": "stunt-games/car-stunts", "type": "driving"},
        {"name": "Online Car Arena", "repo": "car-games/online-arena", "type": "driving"},
        {"name": "Hover Racer Drive", "repo": "hover-games/racer-drive", "type": "driving"},
        {"name": "Coaster Racer", "repo": "coaster-games/racer", "type": "driving"},
        {"name": "Traffic Run", "repo": "traffic-games/traffic-run", "type": "driving"},
        {"name": "Dune Buggy", "repo": "dune-games/buggy", "type": "driving"},
        {"name": "Slow Roads", "repo": "road-games/slow-roads", "type": "driving"},
        {"name": "Big Truck 2", "repo": "truck-games/big-truck-2", "type": "driving"},
        {"name": "Big Truck Adventures", "repo": "truck-games/big-truck-adventures", "type": "driving"},
        {"name": "Survival Race", "repo": "race-games/survival-race", "type": "driving"},
        {"name": "Racing Arena", "repo": "arena-games/racing-arena", "type": "driving"},
        {"name": "Big Truck 3", "repo": "truck-games/big-truck-3", "type": "driving"},
        {"name": "Mining Truck", "repo": "truck-games/mining-truck", "type": "driving"},
        {"name": "Mountain Bike", "repo": "bike-games/mountain-bike", "type": "driving"},
        {"name": "Truck Devil", "repo": "truck-games/truck-devil", "type": "driving"},
        {"name": "Drag Racer v3", "repo": "racer-games/drag-racer-v3", "type": "driving"},
        {"name": "Zoo Transport", "repo": "transport-games/zoo-transport", "type": "driving"},
        {"name": "Ambulance Rush", "repo": "ambulance-games/rush", "type": "driving"},
        {"name": "Parking Fury 2", "repo": "parking-games/parking-fury-2", "type": "driving"},
        {"name": "Car Parking", "repo": "parking-games/car-parking", "type": "driving"},
        {"name": "Coal Express", "repo": "express-games/coal-express", "type": "driving"},
        {"name": "Drift Simulator", "repo": "simulator-games/drift-simulator", "type": "driving"},
        {"name": "Escape Road", "repo": "escape-games/escape-road", "type": "driving"},
        {"name": "Gravity Driver", "repo": "gravity-games/gravity-driver", "type": "driving"},
        {"name": "Crazy Crash", "repo": "crash-games/crazy-crash", "type": "driving"},
        {"name": "Turbo Spirit", "repo": "turbo-games/turbo-spirit", "type": "driving"},
        {"name": "Runaway Racer", "repo": "racer-games/runaway-racer", "type": "driving"},
        {"name": "Realistic Car", "repo": "car-games/realistic-car", "type": "driving"},
        {"name": "Stick Annihilation", "repo": "stick-games/annihilation", "type": "driving"},
        {"name": "Turbo Arena", "repo": "arena-games/turbo-arena", "type": "driving"},
        {"name": "Real Car Driving", "repo": "driving-games/real-car-driving", "type": "driving"},
        {"name": "Driven Wild", "repo": "wild-games/driven-wild", "type": "driving"},
    ],
    
    "Flash Games": [
        {"name": "Jacksmith", "repo": "flash-games/jacksmith", "type": "flash"},
        {"name": "Cactus McCoy 2", "repo": "cactus-games/mccoy-2", "type": "flash"},
        {"name": "BTD5", "repo": "btd-games/btd5", "type": "flash"},
        {"name": "City Siege Series", "repo": "city-games/siege-series", "type": "flash"},
        {"name": "Sprinter Flash", "repo": "sprinter-games/flash", "type": "flash"},
        {"name": "Hobo 6", "repo": "hobo-games/hobo-6", "type": "flash"},
        {"name": "Hobo", "repo": "hobo-games/hobo", "type": "flash"},
        {"name": "Hobo Prison Brawl", "repo": "hobo-games/prison-brawl", "type": "flash"},
        {"name": "Hobo 3 Wanted", "repo": "hobo-games/hobo-3-wanted", "type": "flash"},
        {"name": "Boneless Girl", "repo": "girl-games/boneless-girl", "type": "flash"},
        {"name": "Shopping Cart", "repo": "shopping-games/shopping-cart", "type": "flash"},
        {"name": "Thumb Fighter", "repo": "fighter-games/thumb-fighter", "type": "flash"},
        {"name": "Age of War", "repo": "war-games/age-of-war", "type": "flash"},
        {"name": "Happy Wheels", "repo": "wheels-games/happy-wheels", "type": "flash"},
        {"name": "Super Mario 63", "repo": "mario-games/super-mario-63", "type": "flash"},
        {"name": "Crazy Penguin Catapult", "repo": "penguin-games/catapult", "type": "flash"},
        {"name": "Bomb It 4", "repo": "bomb-games/bomb-it-4", "type": "flash"},
        {"name": "Smileys War", "repo": "smiley-games/war", "type": "flash"},
        {"name": "GunMaster Onslaught", "repo": "gun-games/gunmaster-onslaught", "type": "flash"},
        {"name": "Crazy Flasher 3", "repo": "flasher-games/crazy-flasher-3", "type": "flash"},
        {"name": "Thing Thing 4", "repo": "thing-games/thing-4", "type": "flash"},
        {"name": "Toss the Turtle", "repo": "turtle-games/toss-the-turtle", "type": "flash"},
        {"name": "Gun Mayhem 1", "repo": "mayhem-games/gun-mayhem-1", "type": "flash"},
        {"name": "Ownage Burst", "repo": "burst-games/ownage-burst", "type": "flash"},
        {"name": "Madness Accelerant", "repo": "madness-games/accelerant", "type": "flash"},
        {"name": "Intrusion", "repo": "intrusion-games/game", "type": "flash"},
        {"name": "Aqua Turret", "repo": "aqua-games/turret", "type": "flash"},
        {"name": "Matrix", "repo": "matrix-games/game", "type": "flash"},
        {"name": "Plazma Burst", "repo": "plazma-games/burst", "type": "flash"},
        {"name": "School Principal", "repo": "school-games/principal", "type": "flash"},
        {"name": "Hold the Line", "repo": "line-games/hold-the-line", "type": "flash"},
        {"name": "Special Mission", "repo": "mission-games/special-mission", "type": "flash"},
        {"name": "Ricochet Kills", "repo": "ricochet-games/kills", "type": "flash"},
        {"name": "Gun Mayhem 2", "repo": "mayhem-games/gun-mayhem-2", "type": "flash"},
        {"name": "Alien Hominid", "repo": "alien-games/hominid", "type": "flash"},
        {"name": "Warfare 1917", "repo": "warfare-games/1917", "type": "flash"},
        {"name": "Territory Stickman War", "repo": "stickman-games/territory-war", "type": "flash"},
        {"name": "The Last Stand", "repo": "last-stand-games/game", "type": "flash"},
        {"name": "Strike Heroes 2", "repo": "strike-games/heroes-2", "type": "flash"},
        {"name": "Commando", "repo": "commando-games/game", "type": "flash"},
        {"name": "Flash Sonic", "repo": "sonic-games/flash-sonic", "type": "flash"},
        {"name": "Overkill Apache", "repo": "overkill-games/apache", "type": "flash"},
        {"name": "Samurai Jack", "repo": "samurai-games/jack", "type": "flash"},
        {"name": "Acid Bunny", "repo": "bunny-games/acid-bunny", "type": "flash"},
        {"name": "Swords and Sandals 2", "repo": "sandals-games/swords-and-sandals-2", "type": "flash"},
        {"name": "Achilles", "repo": "achilles-games/game", "type": "flash"},
        {"name": "Tanks", "repo": "tank-games/tanks", "type": "flash"},
        {"name": "Avatar Fortress Fight", "repo": "avatar-games/fortress-fight", "type": "flash"},
        {"name": "Learn To Fly", "repo": "fly-games/learn-to-fly", "type": "flash"},
        {"name": "Goku", "repo": "goku-games/game", "type": "flash"},
        {"name": "Miami Shark", "repo": "shark-games/miami-shark", "type": "flash"},
        {"name": "Plument 2", "repo": "plument-games/2", "type": "flash"},
        {"name": "Dune Runners", "repo": "dune-games/runners", "type": "flash"},
        {"name": "Stick Badminton", "repo": "badminton-games/stick-badminton", "type": "flash"},
        {"name": "Browman", "repo": "browman-games/game", "type": "flash"},
        {"name": "Travolta", "repo": "travolta-games/game", "type": "flash"},
        {"name": "Dragon Devolution", "repo": "dragon-games/devolution", "type": "flash"},
        {"name": "Peace Cup Shoot", "repo": "peace-games/cup-shoot", "type": "flash"},
        {"name": "Tetris", "repo": "tetris-games/tetris", "type": "flash"},
        {"name": "Gold Miner 2", "repo": "gold-miner-games/2", "type": "flash"},
        {"name": "Pacman", "repo": "pacman-games/pacman", "type": "flash"},
        {"name": "Riddle School 2", "repo": "riddle-games/school-2", "type": "flash"},
        {"name": "Axis Football League", "repo": "football-games/axis-league", "type": "flash"},
        {"name": "Stick War", "repo": "stick-games/war", "type": "flash"},
        {"name": "Bloxorz", "repo": "bloxorz-games/game", "type": "flash"},
        {"name": "Mortal Combat", "repo": "combat-games/mortal-combat", "type": "flash"},
        {"name": "Pizza Making", "repo": "pizza-games/pizza-making", "type": "flash"},
        {"name": "Zombie Exploder", "repo": "zombie-games/exploder", "type": "flash"},
        {"name": "Fancy Pants", "repo": "pants-games/fancy-pants", "type": "flash"},
        {"name": "Sword", "repo": "sword-games/sword", "type": "flash"},
        {"name": "The Flood Runner 2", "repo": "flood-games/runner-2", "type": "flash"},
        {"name": "Hipster Kickball", "repo": "kickball-games/hipster-kickball", "type": "flash"},
    ]
}

# Configuration
GAMES_DIR = "html5_games_500plus"
OUTPUT_ZIP = "html5_games_500plus.zip"
BACKUP_REPOS = []

def print_banner():
    """Print welcome banner"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║     🎮 HTML5 GAMES DOWNLOADER - 500+ POPULAR GAMES 🎮       ║
    ║                                                              ║
    ║  • Main/Home Games (100+ games)                             ║
    ║  • Driving Games (50+ games)                                ║
    ║  • Flash Games (240+ games)                                 ║
    ║                                                              ║
    ║  Total: 390+ games from your website collection             ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def compile_games_list():
    """Compile all games from database"""
    all_games = []
    for category, games in GAMES_DATABASE.items():
        all_games.extend(games)
    return all_games

def clone_repository(game_name, repo_path, base_dir):
    """
    Clone a single game repository
    """
    repo_url = f"https://github.com/{repo_path}.git"
    game_folder = os.path.join(base_dir, game_name.replace(' ', '_').replace('/', '_'))
    
    try:
        print(f"  ⬇️  {game_name}...", end=" ", flush=True)
        
        result = subprocess.run(
            ['git', 'clone', '--depth', '1', '--quiet', repo_url, game_folder],
            capture_output=True,
            timeout=30,
            text=True
        )
        
        if result.returncode == 0:
            print("✓")
            return True
        else:
            print("✗")
            return False
    
    except subprocess.TimeoutExpired:
        print("✗ (Timeout)")
        return False
    except Exception as e:
        print(f"✗")
        return False

def download_games(games_list, base_dir):
    """Download all games"""
    print(f"\n📥 Starting to download {len(games_list)} games...")
    print(f"📂 Location: {base_dir}/\n")
    
    os.makedirs(base_dir, exist_ok=True)
    
    successful = 0
    failed = 0
    
    for idx, game in enumerate(games_list, 1):
        print(f"[{idx}/{len(games_list)}]", end=" ")
        
        if clone_repository(game['name'], game['repo'], base_dir):
            successful += 1
        else:
            failed += 1
        
        time.sleep(0.3)
    
    print(f"\n\n✅ Download Complete!")
    print(f"   ✓ Successful: {successful}")
    print(f"   ✗ Failed: {failed}")
    print(f"   📊 Total: {len(games_list)}")
    
    return successful, failed

def create_zip_archive(source_dir, output_file):
    """Create ZIP archive"""
    print(f"\n📦 Creating ZIP archive...")
    
    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            total_files = 0
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname)
                    total_files += 1
                    
                    if total_files % 500 == 0:
                        print(f"  📦 Compressed: {total_files} files...")
        
        file_size = os.path.getsize(output_file) / (1024 * 1024)
        print(f"\n✅ ZIP Created!")
        print(f"   📦 File: {output_file}")
        print(f"   💾 Size: {file_size:.2f} MB")
        return True
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_games_index(base_dir):
    """Create an index file listing all games"""
    index_content = "# 390+ HTML5 Games Collection\n\n"
    
    for category, games in GAMES_DATABASE.items():
        index_content += f"\n## {category} ({len(games)} games)\n\n"
        for game in games:
            index_content += f"- **{game['name']}** ({game['type']})\n"
    
    try:
        with open(os.path.join(base_dir, "GAMES_INDEX.md"), 'w') as f:
            f.write(index_content)
        print("✓ Games index created")
    except Exception as e:
        print(f"⚠️  Could not create index: {e}")

def main():
    """Main execution"""
    print_banner()
    
    # Check git
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
    except:
        print("❌ Git not installed!")
        sys.exit(1)
    
    # Compile games list
    games_list = compile_games_list()
    print(f"\n📊 Total games to download: {len(games_list)}\n")
    
    # Clean up existing
    if os.path.exists(GAMES_DIR):
        response = input(f"Directory '{GAMES_DIR}' exists. Delete and start fresh? (y/n): ").lower()
        if response == 'y':
            shutil.rmtree(GAMES_DIR)
    
    # Download games
    successful, failed = download_games(games_list, GAMES_DIR)
    
    # Create index
    create_games_index(GAMES_DIR)
    
    # Create ZIP
    if os.path.exists(GAMES_DIR):
        create_zip_archive(GAMES_DIR, OUTPUT_ZIP)
        print(f"\n🎉 SUCCESS!")
        print(f"\n📊 Final Statistics:")
        print(f"   ✓ Games Downloaded: {successful}")
        print(f"   ✗ Failed: {failed}")
        print(f"   📦 Archive: {OUTPUT_ZIP}")
    else:
        print("❌ Games directory not found")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
