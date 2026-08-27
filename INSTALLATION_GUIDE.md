# HTML5 Games Downloader - Installation Guide

## 🖥️ System Requirements

- **Operating System**: Windows, macOS, या Linux
- **Python**: 3.7 या उससे ऊपर
- **Git**: Latest version
- **Disk Space**: कम से कम 3-5 GB
- **RAM**: 2 GB या अधिक
- **Internet**: High-speed connection recommended

## 📥 Installation Steps

### Step 1: Git Install करें

#### Windows
1. https://git-scm.com/ पर जाएं
2. Windows के लिए installer download करें
3. Double-click करके install करें
4. सभी default settings के साथ Next दबाएं

#### macOS
```bash
brew install git
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install git
```

#### Linux (Fedora/CentOS)
```bash
sudo yum install git
```

### Step 2: Python Install करें

#### Windows
1. https://www.python.org/downloads/ पर जाएं
2. Python 3.9+ download करें
3. **Important**: "Add Python to PATH" checkbox को check करें
4. Install करें

#### macOS
```bash
brew install python3
```

#### Linux
```bash
sudo apt-get install python3 python3-pip
```

### Step 3: Repository Clone करें

```bash
git clone https://github.com/askafrozali-code/html5-games-downloader.git
cd html5-games-downloader
```

## 🚀 Script चलाना

### Windows
```bash
python download_games.py
```

### macOS / Linux
```bash
python3 download_games.py
```

## ✅ Verification

Script सही तरीके से काम कर रहा है इसके लिए:

1. ✓ Banner display होना चाहिए
2. ✓ Requirements check करनी चाहिए
3. ✓ GitHub search करना चाहिए
4. ✓ Games download होने शुरू होने चाहिए

## 📊 Progress Tracking

Script निम्नलिखित दिखाएगा:
```
[1/200] ⬇️ Cloning: gabrielecirulli/2048... ✓
[2/200] ⬇️ Cloning: Hextris/Hextris... ✓
[3/200] ⬇️ Cloning: ellisonleao/clumsy-bird... ✓
```

## 💾 Output Files

Download complete होने के बाद:

```
html5_games/              (Directory with all games)
html5_games_200plus.zip   (Compressed archive)
```

## 🛠️ Troubleshooting

### Problem: "Python is not recognized"
**Solution**: 
- Windows में Python को PATH में add करें
- Or use `py` instead of `python`

### Problem: "Git is not recognized"
**Solution**:
- Git को फिर से install करें
- Computer restart करें

### Problem: "Permission denied"
**Solution (Linux/Mac)**:
```bash
chmod +x download_games.py
python3 download_games.py
```

### Problem: Slow Download
**Solution**:
- Internet connection check करें
- GitHub rate limiting हो सकती है
- Script automatically retry करेगा

### Problem: Disk Space Error
**Solution**:
- कम से कम 5GB space खाली करें
- किसी अन्य drive में try करें

## 📝 Advanced Usage

### केवल 100 games download करें:
```python
# download_games.py में यह line edit करें:
games_list = games_list[:100]  # Default 200
```

### Custom output folder:
```python
GAMES_DIR = "my_custom_folder"
```

### Custom ZIP name:
```python
OUTPUT_ZIP = "my_games.zip"
```

## 🔍 Verification के बाद

ZIP file extract करने के बाए:
```bash
unzip html5_games_200plus.zip
cd html5_games
ls  # सभी games देखने के लिए
```

## 📧 Support

किसी भी समस्या के लिए:
1. GitHub Issues खोलें
2. Error message के साथ details provide करें
3. Screenshot attach करें

---

**Happy Gaming! 🎮**
