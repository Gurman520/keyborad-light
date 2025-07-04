# Keyboard Backlight Keeper  
*A simple utility to maintain keyboard backlight on Windows laptops*  

---

## 📝 Description  
Many laptops turn off keyboard backlight after a short period of inactivity. This lightweight utility keeps the backlight active by periodically emulating a key press (`F15` by default).

**Windows only** - Uses Windows-specific APIs.

---

## ⚙️ Features  
- Runs silently in system tray  
- Minimal resource usage  
- No installation required  

---

## 🚀 Quick Start  

### Download pre-built version:  
[Download EXE](https://raw.githubusercontent.com/Gurman520/keyborad-light/main/releases/Keyboard%20Backlight.exe)  

### Build from source:  
1. Install Python 3.10+  
2. Install dependencies:  
   ```powershell
   pip install pystray Pillow keyboard auto-py-to-exe
   ```
3. Build EXE:
    ```powershell
   auto-py-to-exe
   ```
4. Run as administrator (required for keyboard emulation)  

---

## 📜 License  
MIT License  

