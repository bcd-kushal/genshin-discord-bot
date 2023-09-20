import discord
from discord import app_commands
from discord.ext import commands

import os
import threading
import asyncio

from ng_ping import bot_ping
from ng_feedback import user_feedback
from ng_avatar import get_avatar

from pr_shutdown import shut_command
from pr_feedback import give_feedback
from pr_db_monitor import monitor_db

from gen_summary import player_summ
from gen_claim_daily import user_claim_daily
from gen_redeem import user_redeem_code
from gen_resources import show_resources
from gen_registration import user_registration
from gen_exploration import user_explore
from gen_diary_log import user_diary

from zz_keep_alive import keeping_alive



class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('.'),intents=discord.Intents.all())
    
    async def on_ready(self):
        print(f'Logged in as {self.user.name}') # ----------------------- add timestamp later 
        synced = await self.tree.sync()
        custom_status = discord.Game(name="with herself")
        await client.change_presence(activity=custom_status,status=discord.Status.idle)
        print(f'Slash commands synced: {len(synced)}')

client = Client()
# till here the request arrives; then its required to bifocate the traffic based on the 
# type of command that was generated - (at root lvl view: isGenshinCommand or notGenshinCommand)
##########################################################################################

# ===> what we would also like to do is distribute it over diff folders to maintain structuring


#============================================
#--------- THE NON GENSHIN COMMANDS ---------

                #PING
@client.tree.command(name='ping',description='Check the bot\'s present latency')
async def ping_check(interaction:discord.Interaction):
    await bot_ping(interaction,client)
    return

                #ABOUT THE BOT


                #VIEW USER PFP
@client.tree.command(name='profile-pic',description="Lets you view an account's pfp")
async def show_pfp(interaction:discord.Interaction,member:discord.Member):
    await get_avatar(interaction,member)
    return
  


                #FEEDBACK
@client.tree.command(name='feedback',description="Send your feedback to us")
async def get_feedback(interaction:discord.Interaction,feedback:str):
    await user_feedback(interaction,feedback)
    return




                #HELP DOCUMENTATION



                #INVITE ---- ????



                #MATH



#============================================





#============================================
#--------- THE GENSHIN COMMANDS ---------

                #USER SUMMARY             .... ephemeral false
@client.tree.command(name="my-summary", description="Summarized statistics of your account")
async def player_summary(interaction:discord.Interaction): #later add user list to chose from
  await player_summ(interaction)



                #CLAIM DAILY             .... ephemeral true
@client.tree.command(name="checkin-hoyolab", description="Claim your hoyolab daily check-in reward")
async def claim_daily(interaction:discord.Interaction):
  await user_claim_daily(interaction)



                #REDEEM CODE             .... ephemeral true
@client.tree.command(name="redeem", description="Redeem code for your account")
async def redeem_code(interaction:discord.Interaction,code1:str,code2:str=None,code3:str=None):
  await user_redeem_code(interaction,code1,code2,code3)



                #EXPLORATION             .... ephemeral false
@client.tree.command(name="my-exploration", description="Check your Teyvat's exploration progress")
async def exploration(interaction:discord.Interaction):
  await user_explore(interaction)




                #IN-GAME RESOURCES             .... ephemeral true
@client.tree.command(name="my-resource", description="Check your in-game resource replenishments (resin,commissions and more)")
async def resource_fetch(interaction:discord.Interaction):
  await show_resources(interaction)


                #PRIMO MORA LOG             .... ephemeral true
@client.tree.command(name="my-diary", description="Check your recent primogem and mora acquisition method")
async def player_diary(interaction:discord.Interaction,primo_log:int=None,mora_log:int=None):
  await user_diary(interaction,primo_log,mora_log)


                #REGISTER             .... ephemeral true
@client.tree.command(name="register", description="Register your Genshin account with us")
async def register(interaction:discord.Interaction):
  await user_registration(interaction)



#============================================





#============================================
#--------- DEVS COMMANDS --------------------

                #GET FEEDBACK LIST
@client.command(aliases=['feedbacks'])
async def feedback(msg):
  await give_feedback(msg,client)


                #SHUTDOWN BOT
@client.command(aliases=['shutoff','sleep_bot','shut_bot'])
async def shutdown(msg):
  await shut_command(msg,client)


                #TEST DB INSERTION
@client.command()
async def showdb(msg):
  await monitor_db(msg,str(client.user))

#============================================


keeping_alive()
client.run(str(os.environ['BOT_TOKEN']))