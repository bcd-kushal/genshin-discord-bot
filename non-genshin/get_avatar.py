import discord

async def get_avatar(interaction:discord.Interaction,user:discord.Member):
  name,avatar="",""
  
  if str(interaction.channel.type)=='private':
    interaction.response.send_message(content='hi')
    return
  else:
    name = user.display_name
    avatar = user.display_avatar

  
  embed=discord.Embed(
    title=f"{name}'s server avatar",
    color=discord.Color.blurple()
  )
  embed.set_image(url=avatar)
  embed.set_author(icon_url=avatar,name=f'{user.name}#{user.discriminator}')
  
  await interaction.response.send_message(embed=embed,ephemeral=True)