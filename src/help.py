class Categories:
    cb = 'cb'
    misc = 'misc'


class HelpDoc(dict):
    def __init__(self, help_txt, brief: str, description='', usage=''):
        if not description:
            description = self.descriptify(brief)
        super().__init__(
            help=help_txt,
            brief=brief,
            description=description,
            usage=usage
        )

    def descriptify(self, s):
        return s[0].upper() + s[1:] + '.'

help_doc = dict(
    battle=HelpDoc(
        help_txt=Categories.cb,
        brief='Start a Mock Scoresheet in this channel with two team names and the size of people per team. You can also ping the corresponding team role.',
        description='\nStart a Mock Scoresheet in this channel with two team names and the size of people per team. You can also ping the corresponding team role.\n`battle TeamThea @Team Aqua 5`',
        usage='battle (Team1) (Team2) (Size)'
    ),
    send=HelpDoc(
        help_txt=Categories.cb,
        brief='Sends in the mentioned/selected player for the specified team.',
        usage='send (@Player) (TeamName)',
        description='Sends in the mentioned/selected player for the specified team.\n`send @superhylia TeamCapulus`'
    ),
    replace=HelpDoc(
        help_txt=Categories.cb,
        brief='Replaces current player with the mentioned/selected player.',
        usage='replace (@Player) (TeamName)',
        description='Replaces current player with the mentioned/selected player.\n`replace Oracle TeamCapulus`'
    ),
    end=HelpDoc(
        help_txt=Categories.cb,
        brief='End the game with characters and stocks for both teams.',
        usage='end (Char1)[AltNum] (StocksTaken1) (Char2)[AltNum] (StocksTaken2)',
        description='End the game with characters and stocks for both teams.\n`end Mario4 3 DK2 1`'
    ),
    endlag=HelpDoc(
        help_txt=Categories.cb,
        brief='Prematurely end the game with characters and stocks for both teams due to lag or disconnection.',
        usage='endlag (Char1)[AltNum] (StocksTaken1) (Char2)[AltNum] (StocksTaken2)',
        description='Prematurely end the game with characters and stocks for both teams due to lag or disconnection.\n`endlag Mario4 3 DK2 1`'
    ),
    resize=HelpDoc(
        help_txt=Categories.cb,
        brief='Resize the size of players per team of the crew battle.',
        usage='resize (Size)',
        description='Resize the size of players per team of the crew battle.\n`resize 3`'
    ),
    undo=HelpDoc(
        help_txt=Categories.cb,
        brief='Undoes the last action taken by the bot.',
        usage='',
        description=''
    ),
    timerstock=HelpDoc(
        help_txt=Categories.cb,
        brief='Lose a stock on your team\'s side due to timing out if you\'ve been sent in: otherwise, if a team is specified, the last player on the selected team will lose a stock due to the timer.',
        usage='timerstock [TeamName]',
        description='Lose a stock on your team\'s side due to timing out if you\'ve been sent in: otherwise, if a team is specified, the last player on the selected team will lose a stock due to the timer.\n`timerstock TeamThea`'
    ),
    forfeit=HelpDoc(
        help_txt=Categories.cb,
        brief='Forfeit the crew battle on your team\'s behalf if you\'ve been sent in: otherwise, if a team is specified, the selected team will forfeit the crew battle.',
        usage='forfeit [TeamName]',
        description='Forfeit the crew battle on your team\'s behalf if you\'ve been sent in: otherwise, if a team is specified, the selected team will forfeit the crew battle.\n`forfeit TeamCapulus`'
    ),
    status=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the current status of the crew battle with an overview of players, stocks taken, lobby ID, and stream.',
        usage='',
        description=''
    ),
    chars=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints all characters, their compatible nicknames, and all of their emojis via your DMs.',
        usage='`',
        description=''
    ),
    clear=HelpDoc(
        help_txt=Categories.cb,
        brief='Clears the current crew battle in the channel.',
        usage='',
        description=''
    ),
    confirm=HelpDoc(
        help_txt=Categories.cb,
        brief='Confirm the final scoresheet is correct once the battle is over.',
        usage='',
        description=''
    ),
    char=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the character\'s corresponding emojis. This is a good way to test what emoji will be used on the scoresheet with the `end` command.',
        usage='char (Char1)[AltNum]',
        description='Prints the character\'s corresponding emojis. This is a good way to test what emoji will be used on the scoresheet with the `end` command.\n`char Sephiroth7`'
    ),
    arena=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the arena information: if the arena ID/pass is specified, the arena will be set.',
        usage='arena [ID/Pass]',
        description='Prints the arena information: if the arena ID/pass is specified, the arena will be set.\n`arena LFLTC/2020`'
    ),
    stream=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the stream information: if the streamlink is specified, the stream will be set.',
        usage='stream [StreamLink]',
        description='Prints the stream information: if the streamlink is specified, the stream will be set.\n`stream https://twitch.tv/LifelightCafe`'
    ),
    timer=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the time in minutes and seconds since the last match finished.',
        usage='',
        description=''
    ),
    guide=HelpDoc(
        help_txt=Categories.misc,
        brief='Provides the link to the usage guide for the bot.',
        usage='',
        description=''
    ),
    coin=HelpDoc(
        help_txt=Categories.misc,
        brief='Flips a coin: if a user is mentioned, it will ask them to choose heads or tails.',
        usage='coin [@User]',
        description='Flips a coin: if a user is mentioned, it will ask them to choose heads or tails.\n`coin @superhylia`'
    ),
    use_ext=HelpDoc(
        help_txt=Categories.cb,
        brief='Use the extension period to send in the next player on your team\'s behalf if you\'ve been sent in: otherwise, if a team is specified, the selected team will use the extension period.',
        usage='use_ext [TeamName]',
        description='Use the extension period to send in the next player on your team\'s behalf if you\'ve been sent in: otherwise, if a team is specified, the selected team will use the extension period.\n`use_ext TeamAqua`'
    ),
    ext=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints whether or not either team has used their extension period.',
        usage='',
        description=''
    ),
    countdown=HelpDoc(
        help_txt=Categories.cb,
        brief='Counts down for 3 seconds: if a time is specified, it will count down from that time in seconds.',
        usage='countdown [Time]',
        description='Prints whether or not either team has used their extension period.\n`countdown 10`'
    ),
    credits=HelpDoc(
        help_txt=Categories.misc,
        brief='Provides the credits for the bot.',
        usage='',
        description=''
    ),
    print_all_emojis=HelpDoc(
        help_txt=Categories.misc,
        brief='TEST.',
        usage='',
        description=''
    ),
    thank=HelpDoc(
        help_txt=Categories.misc,
        brief='Thanks the original bot developer, AlexJett!',
        usage='',
        description=''
    ),
    stagelist=HelpDoc(
        help_txt=Categories.misc,
        brief='Provides an image of the stagelist used in crew battles.',
        usage='',
        description=''
    ),
    invite=HelpDoc(
        help_txt=Categories.misc,
        brief='Provides an invite to the Lifelight Café and Steamy League Discord servers.',
        usage='',
        description=''
    ),
)
