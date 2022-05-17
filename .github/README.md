<img src="https://telegra.ph/file/7f06a0170136896d8bf46.jpg" align="right" width="200" height="200"/>

<h3>⚠️ This repo is just a clone of <a href="https://github.com/TechShreyash/SiestaXMusic">SiestaXMusic</a>. All credits goes to devs of <a href="https://github.com/TechShreyash/SiestaXMusic/graphs/contributors">SiestaXMusic</a>.</h3>


# AviaxMusic

[AviaxMusic](https://github.com/TeamAviax/AviaxMusic) is a Powerful Telegram Music+Video Bot written in Python using Pyrogram and Py-Tgcalls by which you can stream songs, video and even live streams in your group calls via various sources.

* Youtube, Soundcloud, Apple Music, Spotify, Resso and Telegram Audios & Videos support.
* Written from scratch, making it stable and less crashes.
* Attractive thumbnails, fonts and images,  making experience more user-friendly and interactive.
* Loop, Shuffle, Specific Skip, Playlists etc support
* Global, Users, Chats Top 10 played tracks stats
* Multi-Language support


# 🔗 An Overview

Here's a brief high-level overview of the AviaxMusic:

This project is based on [Pyrogram](https://github.com/pyrogram) and [Py-Tgcalls](https://github.com/pytgcalls/pytgcalls) . Pyrogram is a modern, elegant and asynchronous MTProto API framework.

* For database, AviaxMusic uses the MongoDB to store data and keys. [MongoDB](https://www.mongodb.com/) is a document database with the scalability and flexibility that you want with the querying and indexing that you need.
* Project uses the bs4 web scrapping for getting many platform details. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a Python library for pulling data out of HTML and XML files.
* The project uses the font [`Poppins`](../assets/font.ttf) as its main font for the thumbnails.
* The projects uses attractive images and icons which you can get in [assets](../assets/) directory.

For more information on the technologies that power the AviaxMusic, check out the [Docs](https://notreallyshikhar.gitbook.io/yukkimusicbot/).



# ⚡️ Getting Started

### Before deploying AviaxMusic , please have a look towards [all available config vars](../config/README.md) , also please check [all available commands](../strings/command.yml) of the project.

> If you want to start working with AviaxMusic you can either fork or import repo .
> The official [documentation site](https://notreallyshikhar.gitbook.io/yukkimusicbot/) contains a lot of information. The best place to start is from the deployment section.
> If you'd like to talk to us, join us on our [Telegram Group](https://telegram.me/AviaxSupport)


## 🖇 Prerequisites

> In order to avoid conflicts in your project, you must have/installed

- [Python3.9](https://www.python.org/downloads/release/python-390/)
- [Telegram API Key](https://docs.pyrogram.org/intro/setup#api-keys)
- [Telegram Bot Token](https://t.me/botfather)
- [MongoDB URI](https://telegra.ph/How-To-get-Mongodb-URI-04-06)
- [Pyrogram String Session](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/string-session)


## 🖇 Generating Pyrogram String Session

- Generate a Pyrogram String Session via [Replit](https://replit.com/@NotReallyShikhar/Yukki-Music-String-Gen)

- Generate a Pyrogram String Session via [Telegram String Generation Bot](https://t.me/YukkiStringBot)


## 🖇 Heroku Deployment

<h4>Click the button below to deploy AviaxMusic on Heroku!</h4>    
<a href="https://dashboard.heroku.com/new?template=https://github.com/TeamAviax/AviaxMusic"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a>

> How to Deploy To Heroku? [Watch Tutorial](https://www.youtube.com/embed/NPTk-awGalY)

> Click on buttons below to expand and  detailed explanation process. !
    
<details>
    <summary><b> Detailed Heroku Depoyment Process » </b></summary>

<img src="https://telegra.ph/file/672efa7b8160ed39c6e86.jpg" align="right" width="350" height="700"/>

### 🚀 Deploy Process
- Click on the deploy button above and login to your [heroku account](https://heroku.com/login) .
- Fill your values there.
- If you don't know how to get config vars : [Please refer here](../config/README.md)
- Make sure you fill correct values.
- Click on **Deploy** button.
- Please wait till the app gets deployed on heroku. Deploying can take upto **2-3 mins**..
- When your app is successfully deployed, click on **Manage App** button.


### 🚀 Booting Process
- Search for **Resources** Tab inside your app. ( Check Image for more details)
- Click on the **Pencil Icon** under resources section.
- Turn **on** the **switch** present there near pencil icon.
- Congrats your Music Bot is now **Booting**.


### 🚀 Checking Logs
- After Turning on your booting .
- Click on the **More Button** present at top right corner .
- Click on the **View Logs** button from the drop down menu.
- You check your logs there!
- Click on save button there at bottom to save your logs and forward it to us on [@AviaxSupport](https://telegram.me/AviaxSupport) if you face any problem

</details>

## 🖇 VPS Deployment

> Checkout [Docs](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/local-hosting-or-vps) for Detailed Explanation on VPS Deploy


```console
shikhar@MacBook~ $ git clone https://github.com/TeamAviax/AviaxMusic
shikhar@MacBook~ $ cd AviaxMusic
shikhar@MacBook~ $ sudo bash setup
```
> Setup will install each and every requirement, nodejs and pip packages automatically. After successfull installation of requirements , setup will ask you to input your vars.
> Please input your vars correctly.

```console
shikhar@MacBook~ $ bash start
```

> Not Getting VPS Method? [Watch Tutorial](https://telegram.me/TheYukki/2275)


<img src="https://telegra.ph/file/6b75b57da50ef1183fcdc.jpg" align="center">


## 🏷 Support

Reach out to the maintainer at one of the following places:

- [Updates Channel](https://telegram.me/AviaxOfficial)
- [Support Group](https://telegram.me/AviaxSupport)

## 🎗 Project assistance

If you want to say **thank you** or/and support active development of AviaxMusic:

- Add a [GitHub Star](https://github.com/TeamAviax/AviaxMusic) to the project.
- Fork the Repo :)

## 👨🏻‍💻 Authors & contributors

The original setup of this repository is by [Team Yukki](https://github.com/TeamYukki).

For a full list of all authors and contributors, see [the contributors page](https://github.com/TeamYukki/YukkiMusicBot/contributors).
