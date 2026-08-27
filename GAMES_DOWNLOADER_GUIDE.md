# 500+ Games Downloader - Complete Guide

## 🎮 What's Included

**Total Games: 390+ from your website**

### Categories:

1. **Main/Home - New Games** (100+ games)
   - Racing: Race, Dune Dash, Drift Race, Asphalt Rush, etc.
   - Sports: Soccer 2026, Basketball Stars, Basket Random, etc.
   - Action: Ultrakill, Zomblox, Knife Hit, Archers, etc.
   - Platformers: Rooftop Run, Only Up!, Cluster Rush, etc.
   - Simulators: Bus, Truck, Tram, GTA, Supermarket simulators
   - And many more: Granny, Friday Night Funkin, Diep.io, Paper.io 2, etc.

2. **Driving Games** (50+ games)
   - GTA series (GTA Mods, GTA 1)
   - Racing: Drag Racer v3, Extreme Racing, Drift Hunters, etc.
   - Trucks: Big Truck 2/3, Mining Truck, Monster Truck, etc.
   - Motorcycles: Moto X3M Winter, Mountain Bike, etc.
   - Parking: Parking Fury 2, Car Parking
   - Special: Ambulance Rush, Zoo Transport, Coal Express, etc.

3. **Flash Games** (240+ games)
   - Action: Alien Hominid, Commando, Strike Heroes 2, etc.
   - Strategy: Age of War, Warfare 1917, Stick War, etc.
   - Classics: Happy Wheels, Super Mario 63, Pacman, Tetris, etc.
   - Puzzle: Bloxorz, Gold Miner 2, Riddle School 2, etc.
   - Sports: Axis Football League, Stick Badminton, etc.
   - And more: BTD5, Hobo series, Gun Mayhem series, etc.

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/askafrozali-code/html5-games-downloader.git
cd html5-games-downloader

# Run the 500+ games downloader
python download_500plus_games.py

# Or with Python 3
python3 download_500plus_games.py
```

---

## 📊 Script Features

✅ **390+ Pre-configured Games**
- All games from your website list
- Organized by category
- Ready to download

✅ **Automatic Processing**
- Searches GitHub for repositories
- Downloads all games
- Creates organized folders
- Compresses to ZIP

✅ **Progress Tracking**
- Shows download progress
- Statistics at the end
- Error handling

✅ **Smart Organization**
- Categorized structure
- Games index file
- Easy navigation

---

## 📁 Output Structure

After running the script:

```
html5_games_500plus/
├── Race/
├── Dune_Dash/
├── Friday_Night_Funkin/
├── Soccer_2026/
├── GTA_Mods/
├── Monster_Truck/
├── Jacksmith/
├── Happy_Wheels/
├── ... (390+ more games)
└── GAMES_INDEX.md (complete list)

html5_games_500plus.zip (3-8 GB)
```

---

## ⏱️ Execution Time

- **Download Time**: 1-2 hours (depends on internet)
- **ZIP Creation**: 10-20 minutes
- **Total**: ~2-3 hours

---

## 💾 Disk Space Required

- **Uncompressed**: 5-10 GB
- **Compressed ZIP**: 3-8 GB
- **Total Needed**: ~15-20 GB free space

---

## 🛠️ Customization

### Download Specific Categories Only

Edit the script and modify the `compile_games_list()` function:

```python
# Only download Flash Games
def compile_games_list():
    return GAMES_DATABASE["Flash Games"]

# Only download Driving Games
def compile_games_list():
    return GAMES_DATABASE["Driving Games"]

# Only download Main Games
def compile_games_list():
    return GAMES_DATABASE["Main/Home - New Games"]
```

### Change Output Names

```python
GAMES_DIR = "my_games_collection"
OUTPUT_ZIP = "my_games.zip"
```

### Limit Number of Games

```python
games_list = compile_games_list()
games_list = games_list[:100]  # Only download first 100
```

---

## 🎮 Popular Games Included

### Must-Play Games:

**Racing:**
- Moto X3M Winter
- Drift Hunters
- Real Kart
- Asphalt Rush
- Drag Racer v3

**Sports:**
- Basketball Stars
- Soccer Random
- Basket Random
- Real Pool 3D
- Volley Random

**Action:**
- Ultrakill
- Friday Night Funkin
- Knife Hit
- Archers
- Zomblox

**Classic Flash:**
- Happy Wheels
- Super Mario 63
- Pacman
- Tetris
- Age of War

**Puzzle:**
- Bloxorz
- Spiral Roll
- Cluster Rush
- Only Up!
- Gold Miner 2

**Simulators:**
- Bus Simulator
- Truck Simulator
- GTA Simulator
- Your Life Simulator
- Supermarket Sim

---

## 📝 Games Index

After download, open `GAMES_INDEX.md` to see:
- All 390+ games listed
- Categorized by type
- Type classification (racing, puzzle, action, etc.)

---

## 🛠️ Troubleshooting

### Problem: Some games fail to download

**Reason**: Repository might have moved or been deleted
**Solution**: Script continues downloading others, failed games are reported

### Problem: Slow download

**Reason**: GitHub rate limiting or slow internet
**Solution**: 
- Wait and retry
- Reduce games list
- Try during off-peak hours

### Problem: Disk space error

**Solution**:
- Clear 15+ GB space
- Use external drive
- Download in batches (modify games_list)

### Problem: Git timeout

**Solution**:
- Check internet connection
- Increase timeout in script (change `timeout=30` to `timeout=60`)

---

## 🎯 Next Steps After Download

1. **Extract the ZIP file**
   ```bash
   unzip html5_games_500plus.zip
   ```

2. **Explore the games**
   ```bash
   cd html5_games_500plus
   ls  # View all games
   ```

3. **Play a game**
   - Open any game folder
   - Find `index.html`
   - Open in web browser

4. **Check the index**
   - Open `GAMES_INDEX.md`
   - See all available games
   - Get game types

---

## 💡 Tips & Tricks

✅ **Better Organization**
- Organize games by type in subfolders
- Create shortcuts to favorites
- Use a media player for video games

✅ **Backup**
- Keep the ZIP file safe
- Create a backup copy
- Store on cloud

✅ **Playing Games**
- Most work in any modern browser
- Some may need local server
- Check README in each game folder

✅ **Updating**
- Re-run script periodically
- New games may be added
- Some games get updated

---

## 📊 Statistics

```
Total Games: 390+
├── Main/Home: 100+ games
├── Driving: 50+ games
└── Flash: 240+ games

Estimated Size: 5-8 GB (uncompressed)
Compressed Size: 3-5 GB (ZIP)
Download Time: 1-2 hours
```

---

## 📧 Support & Issues

If you encounter any problems:

1. Check `INSTALLATION_GUIDE.md`
2. Review error messages carefully
3. Ensure Git is installed
4. Check disk space
5. Try again with better internet

---

## 🎉 Enjoy!

You now have access to **390+ popular HTML5 games** in one collection!

**Happy Gaming!** 🎮🎮🎮

---

**Last Updated**: 2024
**Script Version**: 2.0
**Total Games**: 390+
