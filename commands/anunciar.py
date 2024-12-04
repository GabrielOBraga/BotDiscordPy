import discord
from discord.ext import commands
from discord import app_commands


class Anunciar(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @app_commands.command(name='anunciar', description="Encaminha um anuncio para o canal onde foi executado o comando.")
  @app_commands.guild_only()
  async def anunciar(self, interaction: discord.Interaction, *, mensagem: str):
    bot_role = interaction.guild.me.top_role 
    author_role = interaction.user.top_role

    if author_role <= bot_role: 
      await interaction.response.send_message( 
        embed=discord.Embed(description="Você não tem permissão para usar este comando.", color=discord.Color.red()), ephemeral=True ) 
      return
  
    embed_message = discord.Embed(
        title="🚨 │ **Anuncio**",
        description=f"**{mensagem}**",
        color=0xFF0004
    )
    embed_message.set_thumbnail(
        url=interaction.guild.icon.replace(format="png").url)
    await interaction.response.send_message(embed=discord.Embed(description="Comando executado com sucesso!", color=interaction.guild.me.color), ephemeral=True, delete_after=4)
    await interaction.channel.send('||@everyone||')
    await interaction.channel.send(embed=embed_message)


async def setup(client: commands.Bot):
  await client.add_cog(Anunciar(client))
