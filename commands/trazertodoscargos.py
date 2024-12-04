import discord
from discord.ext import commands
from discord import app_commands

@commands.has_permissions(administrator=True)
class TrazerTodosCargos(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @app_commands.command(name='puxarporcargo', description="Puxa todos os usuários pelo cargo até o seu canal.")
  @app_commands.guild_only()
  async def trazerTodosCargos(self, interaction: discord.Interaction, cargos: discord.Role):
    bot_role = interaction.guild.me.top_role 
    author_role = interaction.user.top_role

    if author_role <= bot_role: 
      await interaction.response.send_message( 
        embed=discord.Embed(description="Você não tem permissão para usar este comando.", color=discord.Color.red()), ephemeral=True ) 
      return
  
    afkChannel = interaction.guild.afk_channel
    authorChannel = interaction.user.voice.channel
    for channel in interaction.guild.voice_channels:
      if not channel == authorChannel and len(channel.members) > 0 or channel == afkChannel:
        for member in channel.members:
          for m_role in member.roles:
            if m_role.id == cargos.id:
              await member.move_to(authorChannel)
    await interaction.response.send_message(embed=discord.Embed(description="Comando executado com sucesso!", color=interaction.guild.me.color), ephemeral=True, delete_after=4)
  

@commands.has_permissions(administrator=True)
async def setup(client: commands.Bot):
  await client.add_cog(TrazerTodosCargos(client))
