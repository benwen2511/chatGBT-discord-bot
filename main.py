import discord
from discord.ext import commands
import response
import re
import logging
from get_token import get_token

imageKWS = ['img','imgs','image','images','pic','pics','pictures','picture']

class botName(commands.Bot):
  intents = discord.Intents.default()
  def __init__(self):
      super().__init__(command_prefix='-', intents=self.intents)
      self.intents.message_content = True

  async def close(self):
      await super().close()
    
async def send_message(message, userMsg, aiMsgContent, isPrivate=False):
  try:
    res = await response.get_response(userMsg, aiMsgContent)
  except Exception as e:
    await message.channel.send('Something went wrong, please try again later')

  else:
    if isPrivate:
      await message.author.send(res)
    else:
      await message.channel.send(res)
 

async def generate_img(message, userMsg):
  try:
      res = await response.get_img(userMsg)
  except Exception as e:
    await message.channel.send('https://media.makeameme.org/created/bad-word-dont.jpg')
  else:
    await message.channel.send(res)

async def show_help(message):
  helpMsg = """
  `@MentionBot yourmessage` : chat with AI\n`@MentionBot /h` : show help\n`@MentionBot /p yourmessage` : send private response\n`@MentionBot /i` : generate random image
  """
  await message.channel.send(helpMsg)

def run_discord_bot():
  bot = botName()

  @bot.event
  async def on_ready():
    print('Bot is running')

  @bot.listen('on_message')
  async def message_monitor(message):

    for x in message.mentions:
      if x==bot.user:
        userMsg = re.sub(f" *<@{x.id}> *", '', message.content)

        if message.reference:
          aiMsg = await message.channel.fetch_message(message.reference.message_id)
          aiMsgContent = aiMsg.content
        else:
          aiMsgContent = ''

        if userMsg.startswith('/h'):
          await show_help(message)
        elif userMsg.startswith('/p'):
          await message.delete()
          private=True
          await send_message(message,userMsg,aiMsgContent,private)
        elif userMsg.startswith('/i') or any(word in userMsg for word in imageKWS):
          await generate_img(message, userMsg)
        else:
          await send_message(message,userMsg,aiMsgContent)


  bot.run(get_token("discord_token"))

run_discord_bot()