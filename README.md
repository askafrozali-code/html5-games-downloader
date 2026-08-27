# HTML5 Games Downloader

एक powerful Python script जो GitHub से **200+ open-source HTML5 games** को download करके एक single ZIP file में compress करता है।

## ✨ Features

- 🎮 **200+ HTML5 Games** - GitHub से automatically fetch करता है
- 📦 **Single ZIP Archive** - सभी games को एक file में pack करता है
- 🔍 **Smart Search** - GitHub API से latest games को find करता है
- ⚡ **Fast Cloning** - `--depth 1` से quick cloning
- 📊 **Progress Tracking** - Download progress दिखाता है
- 💾 **Organized Structure** - हर game अपने folder में

## 📋 Requirements

- Python 3.7+
- Git installed on your system
- Internet connection
- ~2-5 GB disk space (सभी 200+ games के लिए)

## 🚀 Installation & Usage

### Option 1: Windows/Mac/Linux (Terminal)

```bash
# Repository को clone करें
git clone https://github.com/askafrozali-code/html5-games-downloader.git
cd html5-games-downloader

# Python script को run करें
python download_games.py

# या Python 3 explicitly specify करें
python3 download_games.py
```

### Option 2: Direct Download

1. `download_games.py` को download करें
2. Terminal खोलें और script वाली directory में जाएं
3. चलाएं: `python download_games.py`

## 📝 Script क्या करता है?

1. **Search** - GitHub API से HTML5 games को search करता है
2. **Download** - हर game की repository को clone करता है
3. **Organize** - `html5_games/` folder में organize करता है
4. **Compress** - सभी को `html5_games_200plus.zip` में pack करता है
5. **Report** - Download summary दिखाता है

## 📊 Output

```
html5_games_200plus.zip (2-5 GB)
├── gabrielecirulli_2048/
│   ├── index.html
│   ├── README.md
│   └── ... (source files)
├── Hextris_Hextris/
│   ├── index.html
│   └── ... (source files)
├── ... 198+ more games
└── README.md (सभी games की list)
```

## 🎮 Popular Games शामिल हैं:

- **2048** - Tile sliding game
- **Hextris** - Angular Tetris variant  
- **Clumsy Bird** - Flappy Bird clone
- **Pacman** - Classic arcade
- **AncientBeast** - Multiplayer strategy
- **Kaetram** - 2D MMORPG
- और 195+ और games!

## 🕐 Execution Time

- **Full Download** - 30-60 minutes (internet speed पर depend करता है)
- **ZIP Creation** - 5-10 minutes
- **Total** - ~1-1.5 hours

## 📦 ZIP File Size

- Individual games: 100 KB - 500 MB each
- Total ZIP: 2-5 GB (approximately)

## ⚙️ Customization

Script को edit करके customize कर सकते हैं:

```python
# games की संख्या बदलें
games_list = games_list[:150]  # सिर्फ 150 games

# Output folder का नाम बदलें
GAMES_DIR = "my_games"

# ZIP file का नाम बदलें
OUTPUT_ZIP = "my_games_archive.zip"
```

## 🛠️ Troubleshooting

### Error: "Git is not installed"
**Solution:** Git को install करें: https://git-scm.com/

### Slow download?
- Internet connection check करें
- GitHub rate limiting के कारण slow हो सकता है
- Script automatically retry करेगा

### Disk space insufficient?
- कुछ games को manually remove करें
- या backup से restore करें

## 📝 License

यह script MIT License के under है।
सभी downloaded games के अपने-अपने licenses हैं।

## 🤝 Contributing

Improvements के लिए issues/PRs welcome हैं!

## 📧 Support

किसी भी प्रश्न के लिए GitHub issues खोलें।

---

**Made with ❤️ for HTML5 Game Developers**
