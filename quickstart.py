#!/usr/bin/env python3
"""
Quick start guide for HTML5 Games Downloader
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if all requirements are met"""
    print("🔍 Checking requirements...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ required")
        return False
    print("✓ Python version OK")
    
    # Check Git
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        print("✓ Git installed")
    except:
        print("❌ Git not found. Install from https://git-scm.com/")
        return False
    
    # Check disk space
    import shutil
    total, used, free = shutil.disk_usage("/")
    free_gb = free / (1024 ** 3)
    
    if free_gb < 3:
        print(f"⚠️  Warning: Only {free_gb:.1f} GB free (3 GB recommended)")
    else:
        print(f"✓ Disk space OK ({free_gb:.1f} GB free)")
    
    return True

def main():
    print("""
    ╔════════════════════════════════════════════════════════╗
    ║    HTML5 GAMES DOWNLOADER - Quick Start Guide         ║
    ╚════════════════════════════════════════════════════════╝
    """)
    
    if not check_requirements():
        print("\n❌ Please install missing requirements first")
        return False
    
    print("\n✅ All requirements met!")
    print("\n📝 To start downloading games, run:")
    print("   python download_games.py")
    print("\n⏱️  Estimated time: 30-60 minutes")
    print("💾 Estimated size: 2-5 GB")
    
    return True

if __name__ == "__main__":
    main()
