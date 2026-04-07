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

YouTube blocks many VPS IPs. We now provide **two ways** to keep playback smooth:

1. **API (Recommended):**  
   Stream **audio & video** via our API with built-in vPlay support. No cookie hassle.

2. **Custom Cookies (Fallback / No-API mode):**  
   Generate cookies on your local machine and place them in the `cookies/` folder to bypass YouTube restrictions.

---

## 🎵 Using the API for Audio & Video (vPlay)

The API now supports **both audio and video**.  
Use API for reliability; switch to **custom cookies** if you prefer not to rely on the API.

---

### 🔑 Get an API Key

Manage keys from our official dashboard (no Telegram DMs needed):

[![API Dashboard](https://img.shields.io/badge/Visit-Dashboard-black?style=for-the-badge&logo=vercel)](https://console.nexgenbots.xyz)  
[![API Community](https://img.shields.io/badge/Join-API%20Community-green?style=for-the-badge&logo=telegram)](https://t.me/+oH1cVV8YSsdhMWU5)  
[![Contact Rahul](https://img.shields.io/badge/DM-@RahulTC-blueviolet?style=for-the-badge&logo=telegram)](https://t.me/ItzRahul)  

---

#### 🛠️ Steps to Get Started

1. **Sign up** at [console.nexgenbots.xyz](https://console.nexgenbots.xyz) and create an account.  
2. **Generate Key**: After logging in, click **“Generate Key”** on the dashboard to activate the **Free Plan**.  
3. **Upgrade anytime** via the dashboard for higher limits.  

---

### 📦 Plans & Pricing (₹/month)

| Plan          | Daily API Requests | Daily Video Requests | Price   |
|---------------|--------------------|----------------------|---------|
| **Free**      | 500                | 25                   | ₹0      |
| **Basic**     | 3,000              | 150                  | ₹150    |
| **Starter**   | 5,000              | 250                  | ₹250    |
| **Standard**  | 15,000             | 750                  | ₹450    |
| **Pro**       | 25,000             | 1,250                | ₹900    |
| **Business**  | 50,000             | 2,500                | ₹1700   |
| **Enterprise**| 100,000            | 5,000                | ₹3200   |
| **Ultra**     | 150,000            | 7,500                | ₹4500   |

---

### 📌 Important Notes About API Usage

- 🔄 **Daily Reset**: All limits reset at midnight (IST).  
- 🎧🎬 **Audio + Video**: Fully supported via API (vPlay).  
- 🍪 **Fallback**: Add local **custom cookies** if you prefer not to use the API (works for both audio & video).  
- 💬 **Support**: Join the [API Community Group](https://t.me/+oH1cVV8YSsdhMWU5).  

---

### ⚙️ Integration

Add your API key to `.env`:


API_KEY=your-api-key-here

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

<h3>✔️ Prerequisites</h3>

- <a href="https://www.python.org">Python 3.10+</a> installed  
- <a href="https://deno.com/">deno</a> & <a href="https://ffmpeg.org//">ffmpeg</a> installed on your system  
- Required variables mentioned in <a href="https://github.com/CyberPixelPro/AviaxMusic/blob/master/sample.env">sample.env</a>

1. **Upgrade & Update:**
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```

2. **Install Required Packages:**
   ```bash
   sudo apt-get install python3-pip ffmpeg -y
   ```

3. **Install Deno:**
   ```bash
   apt-get install unzip && curl -fsSL https://deno.land/install.sh | sh
   ```

3. **Setting up PIP**
   ```bash
   sudo pip3 install -U pip
   ```
4. **Clone the Repository**
   ```bash
   git clone https://github.com/CyberPixelPro/AviaxMusic && cd AviaxMusic
   ```
5. **Install Requirements**
   ```bash
   pip3 install -U -r requirements.txt
   ```
6. **Create .env  with sample.env**
   ```bash
   cp sample.env .env
   ```
   - Edit .env with your vars
7. **Editing Vars:**
   ```bash
   vi .env
   ```
   - Edit .env with your values.
   - Press `I` button on keyboard to start editing.
   - Press `Ctrl + C`  once you are done with editing vars and type `:wq` to save .env or `:qa` to exit editing.
8. **Installing tmux**
    ```bash
    sudo apt install tmux -y && tmux
    ```
9. **Run the Bot**
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
  <a href="https://telegram.me/NexGenBotsIndia">
    <img src="https://img.shields.io/badge/Join-Support%20Group-blue?style=for-the-badge&logo=telegram">
  </a>
  <a href="https://telegram.me/NexGenBots">
    <img src="https://img.shields.io/badge/Join-Update%20Channel-blue?style=for-the-badge&logo=telegram">
  </a>
</p>

---

### 🤝 Contributing

We welcome contributions to the Aviax Music Bot project. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with a meaningful name.
3. Make your changes and commit them with a descriptive commit message.
4. Open a pull request against our `master` branch.
5. Our team will review your changes and provide feedback.

For more details, reach out us on telegram.

---

### 📜 License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

### 🙏 Acknowledgements

Thanks to all the contributors, supporters, and users of the Aviax Music Bot. Your feedback and support keep us going!
- AnonX Music – Base inspiration
- All contributors & community members
  
---

⭐ If you like this project, don’t forget to star the repo!

