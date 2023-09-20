import discord 
from datetime import datetime
from replit import db


async def user_feedback(interaction:discord.Interaction,msg):
  await interaction.response.defer(thinking=True,ephemeral=True)
  
  username = interaction.user.name + "#" + interaction.user.discriminator
  timestamp = str(datetime.utcnow().strftime('%m-%d|%H:%M:%S'))
  
  key = timestamp+"|"+username

  if 'feedback' not in db:
    db['feedback']=dict()

  db['feedback'][key]=str(msg)

  #print(interaction.channel.type=='private')
  #print(str(interaction.channel.type)=='private')

  eph=True
  if str(interaction.channel.type)=='private':
    eph=False
  else:
    eph=True
  
  await interaction.followup.send(content=f'Thank You for your feedback soon, we will look into your feedback in the near future!\n{interaction.channel.type}',ephemeral=eph)