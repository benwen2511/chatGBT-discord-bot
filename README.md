# 🤖 chatGBT Discord Bot
ChatGBT discord bot is a project that provide you a great way to interact with chatGBT-OpenAI in your own discord servers.

## Features
- `@MentionBot yourmessage` : chat with chatGBT discord bot

![gif](https://user-images.githubusercontent.com/112210000/210421037-e5827723-7ad1-48a2-a807-74d45b75c5f3.gif)

- `@MentionBot /h` : show all command lines
- `@MentionBot /p yourmessage` : send private response into your DM
- `@MentionBot /i yourmessage` : generate random image based on user input
- `@MentionBot yourmessage` : alternative way to generate image. `yourmessage` has to contain one of the following words in this list `['img','imgs','image','images','pic','pics','picture','pictures']`


![gif](https://user-images.githubusercontent.com/112210000/211229790-4da0c145-9c2c-4096-8392-2577f8885399.gif)





## Installation

### Step 1:
- Create a `config.json` file in the current working directory
- Cope and paste the following template into the `config.json` file:
```
{
  "discord_token":"",
  "openai_api_key": ""
}
```
### Step 2: 
- Create a discord bot.
- Store the bot token in `config.json` file under `discord_token`.
### Step 3:
- Create an OpenAI account in case you do not have one.
- Generate an OpenAI API on this page `https://beta.openai.com/account/api-keys` .
- Store the OpenAI key token in `config.json` file under `openai_api_key`
### Step 4:
- Run the bot with command `py main.py`


