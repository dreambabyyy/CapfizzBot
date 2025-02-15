# CAPFIZZ NODE BOT

## Features

- Multi-account parallel mining
- Automatic ping every 60 seconds per account
- Auto retry with rate limit handling
- Real-time statistics dashboard
- Activity logging for each account
- Easy configuration management
- Modular and maintainable structure

## Prerequisites

Before running the bot, you need to:

1. Register an account at https://mainnet.capfizz.com/register?ref=JDIMF4
2. Install the [Capfizz Sentry Node Extension](https://chromewebstore.google.com/detail/capfizz-sentry-node/agollninopbkafedoijcnbdopajjjmfa) in your Chrome browser

## Installation

1. Clone this repository:

```bash
git clone https://github.com/dreambabyyy/CapfizzBot.git && cd CapfizzBot
```

2. Install dependencies:

```bash
pip3 install -r requirements.txt 
```

## Configuration

### Getting Your Account Cookie

1. Right-click on the Capfizz Sentry Dashboard
2. Click "Inspect Popup"
3. Go to the "Network" tab
4. Copy the cookie from the request headers
5. Add the cookie to `cookie.txt` (one cookie per line for multiple accounts)

![image](https://github.com/user-attachments/assets/a0900738-f484-4243-a5d0-1b980c634c8b)


## Usage

1. Add your account cookie(s) to `nano cookie.txt`:

```
cookie_string_here
another_cookie_string_here
```
2. Add your proxy to `nano proxy.txt`:

```
http://ip:port
http://user:pass@ip:port
socks5://ip:port
socks4://ip:port
```

3. Run the bot:

```bash
python bot.py or python3 bot.py
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
