from PyQt6.QtCore import QDir

from ..basic_game import BasicGame

class ReadyOrNotGame(BasicGame):
	Name = "Ready or Not Support Plugin"
	Author = "Aidan Maskelyne"
	Version = "0.0.1"

	GameName = "Ready or Not"
	GameShortName = "readyornot"
	GameNexusName = "readyornot"
	GameNexusId = 4205
	GameSteamId = 1144200
	GameBinary = "ReadyOrNot.exe"
	GameDataPath = "ReadyOrNot/Content/Paks"
