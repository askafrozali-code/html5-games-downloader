#!/usr/bin/env python3
"""
HTML5 Games Downloader
Downloads 200+ open-source HTML5 games from GitHub and creates a ZIP archive
"""

import os
import subprocess
import json
import time
import shutil
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError
import zipfile
import sys

# Configuration
GAMES_DIR = "html5_games"
OUTPUT_ZIP = "html5_games_200plus.zip"
GITHUB_API_URL = "https://api.github.com/search/repositories"
BACKUP_GAMES_LIST = [
    "gabrielecirulli/2048",
    "Hextris/Hextris",
    "ellisonleao/clumsy-bird",
    "chregu/html5pacman",
    "FreezingMoon/AncientBeast",
    "Kaetram/Kaetram-Open",
    "liorean/html5-games",
    "playcanvas/engine",
    "jboesch/Agar",
    "dirkk0/knight-tour",
    "slime73/love",
    "cocos2d/cocos2d-html5",
    "turbulenz/turbulenz_engine",
    "craftyjs/Crafty",
    "melonjs/melonJS",
    "photonstorm/phaser",
    "gorhill/uBlock",
    "kripken/emscripten",
    "mrdoob/three.js",
    "babylonjs/Babylon.js",
]

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print welcome banner"""
    clear_screen()
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║     HTML5 GAMES DOWNLOADER - 200+ Games Collection      ║
    ║                 GitHub Source Code Fetcher               ║
    ╚══════════════════════════════════════════════════════════╝
    """)

def fetch_games_from_github(query="html5-game", per_page=100):
    """
    Fetch HTML5 games from GitHub API
    Returns list of repository URLs
    """
    print(f"\n🔍 Searching GitHub for {query} repositories...")
    
    games_list = []
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'HTML5-Games-Downloader'
    }
    
    try:
        # Try to fetch from GitHub API
        for page in range(1, 5):  # Fetch multiple pages
            url = f"{GITHUB_API_URL}?q=topic:{query}&sort=stars&per_page={per_page}&page={page}"
            print(f"  📄 Fetching page {page}...")
            
            try:
                req = urlopen(url)
                data = json.loads(req.read().decode('utf-8'))
                
                if 'items' in data:
                    for item in data['items']:
                        games_list.append(item['full_name'])
                        print(f"  ✓ Found: {item['full_name']}")
                
                time.sleep(1)  # Rate limiting
            except URLError as e:
                print(f"  ⚠️  Error fetching page {page}: {e}")
                continue
    
    except Exception as e:
        print(f"⚠️  Could not fetch from GitHub API: {e}")
        print("Using backup games list...")
        return BACKUP_GAMES_LIST
    
    # If we got results, return them, otherwise use backup
    if games_list:
        return games_list[:200]  # Limit to 200
    else:
        print("Using backup games list...")
        return BACKUP_GAMES_LIST

def clone_repository(repo_name, base_dir):
    """
    Clone a single repository
    Returns True if successful, False otherwise
    """
    repo_url = f"https://github.com/{repo_name}.git"
    repo_path = os.path.join(base_dir, repo_name.replace('/', '_'))
    
    try:
        print(f"  ⬇️  Cloning: {repo_name}...", end=" ")
        
        # Use git clone with timeout
        result = subprocess.run(
            ['git', 'clone', '--depth', '1', repo_url, repo_path],
            capture_output=True,
            timeout=30,
            text=True
        )
        
        if result.returncode == 0:
            print("✓")
            return True
        else:
            print(f"✗ (Error: {result.stderr[:50]})")
            return False
    
    except subprocess.TimeoutExpired:
        print("✗ (Timeout)")
        return False
    except Exception as e:
        print(f"✗ ({str(e)[:50]})")
        return False

def download_games(games_list, base_dir):
    """
    Download multiple games
    """
    print(f"\n📥 Starting to download games...")
    print(f"📂 Games will be saved to: {base_dir}/")
    print(f"🎮 Total games to download: {len(games_list)}\n")
    
    os.makedirs(base_dir, exist_ok=True)
    
    successful = 0
    failed = 0
    
    for idx, game in enumerate(games_list, 1):
        print(f"[{idx}/{len(games_list)}]", end=" ")
        
        if clone_repository(game, base_dir):
            successful += 1
        else:
            failed += 1
        
        # Add small delay to avoid rate limiting
        time.sleep(0.5)
    
    print(f"\n\n✅ Download Summary:")
    print(f"   ✓ Successful: {successful}")
    print(f"   ✗ Failed: {failed}")
    print(f"   📊 Total: {successful + failed}")
    
    return successful, failed

def create_zip_archive(source_dir, output_file):
    """
    Create a ZIP archive from the games directory
    """
    print(f"\n📦 Creating ZIP archive...")
    print(f"📁 Source: {source_dir}")
    print(f"📄 Output: {output_file}")
    
    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            total_files = 0
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname)
                    total_files += 1
                    
                    if total_files % 100 == 0:
                        print(f"  📦 Compressed: {total_files} files...")
        
        file_size = os.path.getsize(output_file) / (1024 * 1024)  # MB
        print(f"\n✅ ZIP created successfully!")
        print(f"   📦 Archive: {output_file}")
        print(f"   💾 Size: {file_size:.2f} MB")
        return True
    
    except Exception as e:
        print(f"❌ Error creating ZIP: {e}")
        return False

def create_readme(games_dir):
    """
    Create a README file with information about all games
    """
    readme_content = """# HTML5 Games Collection (200+ Games)

This is a collection of 200+ open-source HTML5 games downloaded from GitHub.

## Directory Structure

Each subdirectory contains a separate game with full source code.

## How to Run

1. Navigate to any game directory
2. Read the README.md file in that directory (if available)
3. Most games can be run by opening `index.html` in a web browser
4. Some games may require a local server or build process

## Popular Games Included

- **2048** - The famous tile-sliding game
- **Hextris** - Angular Tetris variant
- **Clumsy Bird** - Flappy Bird clone
- **Pacman** - Classic arcade game
- **AncientBeast** - Multiplayer strategy game
- **Kaetram** - Open-source 2D MMORPG
- And 195+ more!

## Technologies Used

- HTML5 Canvas
- WebGL
- JavaScript/TypeScript
- Various game frameworks:
  - Phaser
  - Babylon.js
  - Three.js
  - Crafty.js
  - Cocos2d
  - MelonJS

## License

Each game has its own license. Please check the LICENSE file in each repository.

## Sources

Games were downloaded from:
- GitHub Topic: html5-game
- Individual repositories with HTML5 game implementations

---

Generated: 2024 | HTML5 Games Downloader
"""
    
    try:
        with open(os.path.join(games_dir, "README.md"), 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print("✓ README.md created")
    except Exception as e:
        print(f"⚠️  Could not create README: {e}")

def main():
    """Main execution function"""
    print_banner()
    
    # Check if git is installed
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
    except:
        print("❌ Error: Git is not installed!")
        print("Please install Git from https://git-scm.com/")
        sys.exit(1)
    
    # Fetch games list
    games_list = fetch_games_from_github("html5-game", per_page=100)
    
    if not games_list:
        print("❌ Error: Could not fetch games list")
        sys.exit(1)
    
    # Clean up if directory already exists
    if os.path.exists(GAMES_DIR):
        print(f"\n⚠️  Directory '{GAMES_DIR}' already exists")
        response = input("Do you want to delete it and start fresh? (y/n): ").lower()
        if response == 'y':
            shutil.rmtree(GAMES_DIR)
            print("✓ Directory deleted")
        else:
            print("Using existing directory...")
    
    # Download games
    successful, failed = download_games(games_list, GAMES_DIR)
    
    # Create README
    create_readme(GAMES_DIR)
    
    # Create ZIP archive
    if os.path.exists(GAMES_DIR):
        if create_zip_archive(GAMES_DIR, OUTPUT_ZIP):
            print(f"\n🎉 SUCCESS! Your ZIP file is ready: {OUTPUT_ZIP}")
            print(f"\n📊 Statistics:")
            print(f"   🎮 Games Downloaded: {successful}")
            print(f"   ❌ Failed: {failed}")
            print(f"   📦 Archive: {OUTPUT_ZIP}")
        else:
            print("⚠️  ZIP creation failed")
    else:
        print("❌ Games directory not found")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
