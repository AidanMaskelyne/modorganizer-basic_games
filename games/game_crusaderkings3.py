from ..basic_game import BasicGame


class CrusaderKings3Game(BasicGame):
    Name = "Crusader Kings III Support Plugin"
    Author = "AidanMaskelyne"
    Version = "0.1.0"

    GameName = "Crusader Kings III"
    GameShortName = "crusaderkings3"
    GameNexusName = "crusaderkings3"
    GameNexusId = 3486
    GameSteamId = 1158310
    GameBinary = "ck3.exe"

    GameDocumentsDirectory = r"%DOCUMENTS%/Paradox Interactive\Crusader Kings III"
    GameDatapath = r"%GAME_DOCUMENTS%\mod"
    GameSavesDirectory = r"%GAME_DOCUMENTS%\save games"
    GameSaveExtension = "ck3"
