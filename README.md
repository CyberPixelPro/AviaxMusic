<h1 align="center">🎵 Aviax Music Bot 🎵</h1>

<p align="center">
  <img src="https://telegra.ph/file/29808c1fd50add3b1bfc6.jpg" alt="Aviax Music Logo" width="1300" height="300">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/TeamAviax/AviaxMusic?style=for-the-badge&color=blue" alt="GitHub stars">
  <img src="https://img.shields.io/github/forks/TeamAviax/AviaxMusic?style=for-the-badge&color=blue" alt="GitHub forks">
  <img src="https://img.shields.io/github/issues/TeamAviax/AviaxMusic?style=for-the-badge&color=red" alt="GitHub issues">
  <img src="https://img.shields.io/github/license/TeamAviax/AviaxMusic?style=for-the-badge&color=green" alt="GitHub license">
</p>

<h2 align="center">Delivering Superior Music Experience to Telegram</h2>

---

### 🌟 Features

- 🎵 **Multiple Sources:** Play music from various platforms.
- 📃 **Queue System:** Line up your favorite songs.
- 🔀 **Advanced Controls:** Shuffle, repeat, and more.
- 🎛 **Customizable Settings:** From equalizer to normalization.
- 📢 **Crystal Clear Audio:** High-quality playback.
- 🎚 **Volume Mastery:** Adjust to your preferred loudness.

---

### 🔧 Quick Setup

1. **Upgrade & Update:**
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```

2. **Install Required Packages:**
   ```bash
   sudo apt-get install python3-pip ffmpeg -y
   ```
3. **Setting up PIP**
   ```bash
   sudo pip3 install -U pip
   ```
4. **Installing Node**
   ```bash
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && source ~/.bashrc && nvm install v18
   ```
5. **Clone the Repository**
   ```bash
   https://github.com/TeamAviax/AviaxMusic && cd AviaxMusic
   ```
6. **Install Requirements**
   ```bash
   pip3 install -U -r requirements.txt
   ```
7. **Create .env  with sample.env**
   ```bash
   cp sample.env .env
   ```
   - Edit .env with your vars
8. **Editing Vars:**
   ```bash
   vi .env
   ```
   - Edit .env with your values.
   - Press `I` button on keyboard to start editing.
   - Press `Ctrl + C`  once you are done with editing vars and type `:wq` to save .env or `:qa` to exit editing.
9. **Installing tmux**
    ```bash
    sudo apt install tmux -y && tmux
    ```
10. **Run the Bot**
    ```bash
    bash start
    ```

