<h1 align="center">🎵 Aviax Music Bot 🎵</h1>

<p align="center">
  <img src="https://telegra.ph/file/29808c1fd50add3b1bfc6.jpg" alt="Aviax Music Logo" width="600" height="150">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/TeamAviax/AviaxMusic?style=for-the-badge&color=blue" alt="GitHub stars">
  <img src="https://img.shields.io/github/forks/TeamAviax/AviaxMusic?style=for-the-badge&color=blue" alt="GitHub forks">
  <img src="https://img.shields.io/github/issues/TeamAviax/AviaxMusic?style=for-the-badge&color=red" alt="GitHub issues">
  <img src="https://img.shields.io/github/license/TeamAviax/AviaxMusic?style=for-the-badge&color=green" alt="GitHub license">
</p>

<h2 align="center">Delivering Superior Music Experience to Telegram</h2>

---

### 🛠 Fix for YouTube Blocking VPS IPs

Due to YouTube blocking VPS IPs drastically, we have implemented a fix. Follow the steps below:

1. **Join our Support Group**: Type `#script` in our [support group](https://t.me/NexGenSpam) to get the necessary script.
2. **Run the Script**: Run the downloaded script on your Windows Desktop Through VS Code or any other Software to generate cookies.
3. **Fork the Repository**: Fork this repository to your GitHub account.
4. **Add Cookies**: Paste the generated cookies into the `cookies` folder in your forked repository.
5. **Deploy the Bot**: Continue with the setup instructions as outlined above.

This process will allow you to bypass the YouTube restrictions and ensure smooth operation of the bot.

---

## 🎵 Using the API for Audio Streaming
If you do not want to deal with YouTube restrictions, you can rely on our API for audio streaming. The API allows you to fetch audio directly without needing cookies, making the process simpler and more reliable.

### How to Get an API Key
To use the API, you need an API key. Follow these steps to obtain one:

1. **DM on Telegram**: Contact the bot admin on Telegram at [Rahul](https://t.me/RahulTC) to request an API key.
2. **Free Trial**: New users can request a **5-day free trial** with a 1,000 song request limit to test the API. Simply mention "I want a free trial" in your DM, and I will provide a trial API key.
3. **Choose a Plan**: After the trial (or if you want a higher limit), select a plan based on your song request limit needs (all prices are in INR, on a **monthly basis**):
   - **5,000 Song Requests Daily**: ₹49/month
   - **10,000 Song Requests Daily**: ₹99/month
   - **15,000 Song Requests Daily**: ₹149/month
   - **20,000 Song Requests Daily**: ₹199/month
4. **Payment**: After selecting a plan, You will be provided payment details. Once the payment is confirmed, you will receive your API key via Telegram DM.
5. **Integrate the API Key**: Add the API key to your bot's configuration (refer to the setup instructions for details on where to add the key).

### Important Notes About API Usage
- **Daily Reset**: The song request limit resets daily at midnight (IST). For example, if you have a 5,000 song request limit, you can request up to 5,000 songs each day.
- **Audio Only**: The API provides audio streaming only. If you need video play support, you must add cookies as described in the section above.
- **Support**: If you face any issues with the API or need help with integration, join our [support group](https://t.me/NexGenSpam) and ask for assistance.

---

### 🌟 Features

- 🎵 **Multiple Sources:** Play music from various platforms.
- 📃 **Queue System:** Line up your favorite songs.
- 🔀 **Advanced Controls:** Shuffle, repeat, and more.
- 🎛 **Customizable Settings:** From equalizer to normalization.
- 📢 **Crystal Clear Audio:** High-quality playback.
- 🎚 **Volume Mastery:** Adjust to your preferred loudness.

---

## 🚀 Deploy on Heroku 
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/CyberPixelPro/AviaxMusic)

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
   git clone https://github.com/CyberPixelPro/AviaxMusic && cd AviaxMusic
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

---

### 🛠 Commands & Usage

The Aviax Music Bot offers a range of commands to enhance your music listening experience on Telegram:

| Command                 | Description                                 |
|-------------------------|---------------------------------------------|
| `/play <song name>`     | Play the requested song.                    |
| `/pause`                | Pause the currently playing song.           |
| `/resume`               | Resume the paused song.                     |
| `/skip`                 | Move to the next song in the queue.         |
| `/stop`                 | Stop the bot and clear the queue.           |
| `/queue`                | Display the list of songs in the queue.     |

For a full list of commands, use `/help` in [telegram](https://t.me/AviaxBeatzBot).

---

### 🔄 Updates & Support

Stay updated with the latest features and improvements to Aviax Music Bot:

<p align="center">
  <a href="https://telegram.me/NexGenSpam">
    <img src="https://img.shields.io/badge/Join-Support%20Group-blue?style=for-the-badge&logo=telegram">
  </a>
  <a href="https://telegram.me/NexGenSpam">
    <img src="https://img.shields.io/badge/Join-Update%20Channel-blue?style=for-the-badge&logo=telegram">
  </a>
</p>

---

### 🤝 Contributing

We welcome contributions to the Aviax Music Bot project. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with a meaningful name.
3. Make your changes and commit them with a descriptive commit message.
4. Open a pull request against our `main` branch.
5. Our team will review your changes and provide feedback.

For more details, reach out us on telegram.

---

### 📜 License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

### 🙏 Acknowledgements

Thanks to all the contributors, supporters, and users of the Aviax Music Bot. Your feedback and support keep us going!
- [Yukki Music](https://github.com/TeamYukki/YukkiMusicBot) and [AnonXMusic](https://github.com/AnonymousX1025/AnonXMusic) For their Source Codes.
- **Special Thanks** to [SPiDER 🇮🇳](https://github.com/Surendra9123) for invaluable assistance in resolving the IP ban issue.
