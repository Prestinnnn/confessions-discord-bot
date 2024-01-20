import discord
from discord import app_commands 

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            guild_id = SERVER ID HERE 

            try:
                await tree.sync(guild=discord.Object(id=guild_id))
                print('Commands synced successfully.')
                self.synced = True
            except discord.errors.Forbidden:
                print('Missing permissions to manage application commands.')
            except Exception as e:
                print(f'Error during command syncing: {e}')

        print(f"We have logged in as {self.user}.")

    @staticmethod
    async def log_confession(author, confession_text):
                                # channel id
        log_channel = client.get_channel(CHANNEL ID HERE)
        if log_channel:
            await log_channel.send(f"**Confession by {author.name}#{author.discriminator}:**\n{confession_text}")

client = aclient()
tree = app_commands.CommandTree(client)
                                      # server id
@tree.command(guild=discord.Object(id=SERVER ID HERE), name='confess', description='Send an anonymous confession')
async def confess(interaction, confession_text: str):
    author = interaction.user
    confession_text = interaction.data['options'][0]['value'] if 'options' in interaction.data else 'No confession provided'
    
    
    await interaction.response.send_message(content=f"Confession received: {confession_text}", ephemeral=True)

    
    await client.log_confession(author, confession_text)

   
    em = discord.Embed(color=0xa6756b)
    em.title = 'Anonymous Confession'
    em.description = confession_text
    em.set_footer(text='Confession by an anonymous user')

    
    await interaction.followup.send(embed=em)

client.run('BOT TOKEN HERE')

# code by Prestin






