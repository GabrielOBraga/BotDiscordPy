import discord
from discord import ui
from .selectInterfaces import createEssentialChannels
from .btnInterfaces import *
import asyncio


class ViewActionConfirm(ui.View):
    def __init__(self, channels):
        super().__init__()
        self.future = asyncio.Future()
        self.add_item(createEssentialChannels(channels, self.future))

class ViewBtnInterface(ui.View):
    def __init__(self,userCallCommand ,channelWaiting: discord.VoiceChannel, channelHome: discord.VoiceChannel, channelBlue: discord.VoiceChannel, channelRed: discord.VoiceChannel,confirmedUsers: list, embedMessage, embedMessageTeam):
        super().__init__()

        self.amountBtn = BtnAmountCustomMatch()
        self.startBtn = BtnStartCustomMatch(
          userCallCommand, channelBlue, channelRed, confirmedUsers, embedMessageTeam, self
        )
        self.joinBtn = BtnJoinCustomMatch(
          channelWaiting, confirmedUsers, embedMessage, self
        )
        self.exitBtn = BtnExitCustomMatch(
          channelHome, confirmedUsers, embedMessage, self
        )
        self.add_item(self.joinBtn)
        self.add_item(self.exitBtn)
        self.add_item(self.amountBtn)
        self.add_item(self.startBtn)
    

        