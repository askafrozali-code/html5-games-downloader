# 🎮 HTML5 Games Downloader - Complete Repository

**Download 390+ Popular HTML5 Games in One Click!**

A comprehensive Python project to automatically download and organize 390+ popular HTML5 games from GitHub, complete with organized categorization and ZIP compression.

---

## 📊 Repository Contents

### Main Files

| File | Purpose |
|------|---------|
| `download_500plus_games.py` | **Main Script** - Downloads all 390+ games |
| `download_games.py` | Alternative script for 200+ games |
| `README.md` | General documentation |
| `GAMES_DOWNLOADER_GUIDE.md` | Detailed guide for 500+ games downloader |
| `INSTALLATION_GUIDE.md` | Step-by-step installation instructions |
| `GAMES_LIST.txt` | Complete list of all 390+ games |
| `.gitignore` | Git ignore rules |
| `BANNER.txt` | ASCII art banner |

---

## 🎯 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/askafrozali-code/html5-games-downloader.git
cd html5-games-downloader

# 2. Run the main script
python download_500plus_games.py

# 3. Wait 1-2 hours
# 4. Get html5_games_500plus.zip (3-8 GB)
```

---

## 🎮 Games Included (390+)

### Main/Home Games (100+)
Racing, Sports, Action, Platformers, Simulators, Puzzle, Horror, Music, IO Games, and more!

**Popular games:** Friday Night Funkin, Soccer 2026, Basketball Stars, Ultrakill, Granny, Only Up!, Drift Hunters, Diep.io, Paper.io 2, and 90+ more!

### Driving Games (50+)
Racing, Trucks, Motorcycles, GTA series, Simulators, Parking, Stunts, and more!

**Popular games:** GTA 1/Mods, Drag Racer v3, Big Truck series, Moto X3M Winter, Monster Truck, and 45+ more!

### Flash Games (240+)
Action, Strategy, Puzzle, Classics, Sports, Casual, and more!

**Popular games:** Happy Wheels, Super Mario 63, Pacman, Tetris, Age of War, Stick War, BTD5, Alien Hominid, and 230+ more!

---

## 📋 Features

✅ **390+ Pre-configured Games**
- Organized by category (Main, Driving, Flash)
- All from popular GitHub repositories
- Ready to download and play

✅ **Automatic Processing**
- Downloads all games automatically
- Creates organized folder structure
- Compresses to single ZIP file
- Shows progress tracking

✅ **Smart Organization**
- Categorized by game type
- Games index included
- Easy navigation
- Well-documented

✅ **No External Dependencies**
- Uses Python standard library only
- Just needs Git installed
- Works on Windows, Mac, Linux

✅ **Comprehensive Documentation**
- Installation guide
- Usage guide
- Troubleshooting tips
- Games list reference

---

## 📁 Output Structure

```
html5_games_500plus/
├── Race/
├── Dune_Dash/
├── Friday_Night_Funkin/
├── Soccer_2026/
├── GTA_Mods/
├── Happy_Wheels/
├── Super_Mario_63/
├── Pacman/
├── ... (380+ more games)
└── GAMES_INDEX.md

html5_games_500plus.zip (3-8 GB compressed)
```

---

## ⏱️ Timeline

| Stage | Time |
|-------|------|
| Download games | 1-2 hours |
| Create ZIP | 10-20 minutes |
| **Total** | **~2-3 hours** |

---

## 💾 Storage Requirements

| Type | Size |
|------|------|
| Uncompressed | 5-10 GB |
| ZIP Archive | 3-8 GB |
| Total Space Needed | 15-20 GB |

---

## 🛠️ System Requirements

- ✓ Python 3.7+
- ✓ Git (any version)
- ✓ 15-20 GB free disk space
- ✓ Internet connection
- ✓ Windows, macOS, or Linux

---

## 📖 Documentation

| Document | Content |
|----------|---------|
| `INSTALLATION_GUIDE.md` | How to install dependencies and run script |
| `GAMES_DOWNLOADER_GUIDE.md` | Detailed guide for 500+ games downloader |
| `GAMES_LIST.txt` | Complete organized list of all 390+ games |
| `README.md` | General info and features |
| `BANNER.txt` | ASCII art banner |

---

## 🎯 Game Categories

### By Type
- **Racing**: 40+ games (Drift, Formula, Street, etc.)
- **Sports**: 30+ games (Soccer, Basketball, Pool, etc.)
- **Action**: 50+ games (Shooting, Fighting, etc.)
- **Puzzle**: 25+ games (Blocks, Brain teasers, etc.)
- **Platformer**: 20+ games (Jumping, Climbing, etc.)
- **Simulator**: 15+ games (Driving, Business, etc.)
- **Strategy**: 15+ games (Tower Defense, War, etc.)
- **Others**: 95+ games (Casual, Horror, Adventure, etc.)

---

## 🚀 Usage Examples

### Download All Games
```bash
python download_500plus_games.py
```

### Customize - Only Flash Games
Edit script and modify `compile_games_list()`:
```python
return GAMES_DATABASE["Flash Games"]
```

### Customize - Only 100 Games
```python
games_list = compile_games_list()
games_list = games_list[:100]
```

### Different Output Name
```python
GAMES_DIR = "my_games"
OUTPUT_ZIP = "my_games.zip"
```

---

## 🛠️ Troubleshooting

### Git not installed?
👉 Download from: https://git-scm.com/

### Python not found?
👉 Download from: https://www.python.org/downloads/
👉 Make sure to check "Add Python to PATH"

### Some games fail to download?
👉 Script continues with others
👉 Failed games are reported at the end
👉 Retry with better internet

### Slow download?
👉 Check internet connection
👉 GitHub rate limiting possible
👉 Try during off-peak hours

### Disk space error?
👉 Free up 15+ GB
👉 Use external drive
👉 Modify games list to download fewer

---

## 📊 Statistics

```
Repository: html5-games-downloader
Total Games: 390+
├── Main/Home: 100+ games
├── Driving: 50+ games
└── Flash: 240+ games

Categories: 8+ types
Estimated Download: 5-10 GB
Compressed Size: 3-8 GB
Download Time: 1-2 hours
```

---

## 🎮 Popular Must-Play Games

### Racing
- Moto X3M Winter
- Drift Hunters
- Drag Racer v3
- Real Kart
- Asphalt Rush

### Sports
- Basketball Stars
- Soccer Random
- Basket Random
- Real Pool 3D
- Volley Random

### Action
- Friday Night Funkin
- Ultrakill
- Knife Hit
- Archers
- Zomblox

### Puzzle
- Bloxorz
- Cluster Rush
- Spiral Roll
- Gold Miner 2
- Only Up!

### Classic
- Happy Wheels
- Super Mario 63
- Pacman
- Tetris
- Age of War

### IO Games
- Diep.io
- Paper.io 2
- Slither.io 2
- Chicken Royale

---

## 📝 Files Reference

### Python Scripts
- `download_500plus_games.py` - Main 390+ games downloader (4000+ lines)
- `download_games.py` - Original 200+ games downloader

### Documentation
- `README.md` - Main readme with features
- `INSTALLATION_GUIDE.md` - Installation steps
- `GAMES_DOWNLOADER_GUIDE.md` - Detailed usage guide
- `GAMES_LIST.txt` - Complete games reference

### Config
- `.gitignore` - Git ignore patterns
- `BANNER.txt` - ASCII banner

---

## 🎁 What You Get

After running the script, you'll have:

✅ **390+ Organized Games**
- Each in separate folder
- Original source files included
- Ready to play
- Well-categorized

✅ **Single ZIP Archive**
- All games compressed
- 3-8 GB file
- Easy to backup
- Easy to share

✅ **Complete Documentation**
- Games index
- Setup guides
- Troubleshooting help
- Games list

✅ **Ready to Play**
- Open any game folder
- Find index.html
- Open in browser
- Start playing!

---

## 🌟 Key Features

🎯 **Easy to Use**
- Single command to download all
- Automatic organization
- Progress tracking

⚡ **Fast**
- Batch downloading
- Parallel processing capability
- Optimized for speed

📦 **Complete**
- 390+ games included
- All popular classics
- Latest games

🔒 **Safe**
- Open-source repositories
- No malware
- Verified sources

---

## 📧 Support

For help:
1. Read `INSTALLATION_GUIDE.md`
2. Check `GAMES_DOWNLOADER_GUIDE.md`
3. Review `GAMES_LIST.txt`
4. Open GitHub issues

---

## 📄 License

MIT License - Feel free to use, modify, and distribute!

All games have their own licenses - check individual game folders.

---

## 🎉 Ready to Start?

```bash
git clone https://github.com/askafrozali-code/html5-games-downloader.git
cd html5-games-downloader
python download_500plus_games.py
```

**Happy Gaming!** 🎮🎮🎮

---

**Repository**: https://github.com/askafrozali-code/html5-games-downloader
**Last Updated**: August 2024
**Version**: 2.0
**Total Games**: 390+
**Status**: ✅ Active & Maintained

Made with ❤️ for HTML5 Game Lovers
