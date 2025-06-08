class Categories:
    cb = 'cb'
    misc = 'misc'


class HelpDoc(dict):
    def __init__(self, help_txt, brief: str, description='', usage='', example=''):
        if not description:
            description = self.descriptify(brief)
        super().__init__(
            help=help_txt,
            brief=brief,
            description=description,
            usage=usage,
            example=example
        )

    def descriptify(self, s):
        return s[0].upper() + s[1:] + '.'

help_doc = dict(
    battle=HelpDoc(
        help_txt=Categories.cb,
        brief='Start a Mock Scoresheet in this channel with two team names and the size of people per team. You can also ping the corresponding team role.',
        description='',
        usage='```battle (Team1) (Team2) (Size)```',
        example='**Example:** `battle TeamThea @Team Aqua 5`'
    ),
    send=HelpDoc(
        help_txt=Categories.cb,
        brief='Sends in the mentioned/selected player for the specified team.',
        usage='**Usage:** `send (@Player) (TeamName)`',
        example='**Example:** `send @superhylia TeamCapulus`'
    ),
    replace=HelpDoc(
        help_txt=Categories.cb,
        brief='Replaces current player with the mentioned/selected player.',
        usage='**Usage:** `replace (@Player) (TeamName)`',
        example='**Example:** `replace Oracle TeamCapulus`'
    ),
    end=HelpDoc(
        help_txt=Categories.cb,
        brief='End the game with characters and stocks for both teams.',
        usage='**Usage:** `end (Char1)[AltNum] (StocksTaken1) (Char2)[AltNum] (StocksTaken2)`',
        example='**Example:** `end Mario4 3 DK2 1`'
    ),
    endlag=HelpDoc(
        help_txt=Categories.cb,
        brief='Prematurely end the game with characters and stocks for both teams due to lag or disconnection.',
        usage='**Usage:** `endlag (Char1)[AltNum] (StocksTaken1) (Char2)[AltNum] (StocksTaken2)`',
        example='**Example:** `endlag Mario4 3 DK2 1`'
    ),
    resize=HelpDoc(
        help_txt=Categories.cb,
        brief='Resize the size of players per team of the crew battle.',
        usage='**Usage:** `resize (Size)`',
        example='**Example:** `resize 3`'
    ),
    undo=HelpDoc(
        help_txt=Categories.cb,
        brief='Undoes the last action taken by the bot.',
        usage='**Usage:** `undo`',
        example='**Example:** `undo`'
    ),
    timerstock=HelpDoc(
        help_txt=Categories.cb,
        brief='Lose a stock on your team\'s side due to timing out if you\'ve been sent in: otherwise, if a team is specified, the last player on the selected team will lose a stock due to the timer.',
        usage='**Usage:** `timerstock [TeamName]`',
        example='**Example:** `timerstock TeamThea`'
    ),
    forfeit=HelpDoc(
        help_txt=Categories.cb,
        brief='Forfeit the crew battle on your team\'s behalf if you\'ve been sent in: otherwise, if a team is specified, the selected team will forfeit the crew battle.',
        usage='**Usage:** `forfeit [TeamName]`',
        example='**Example:** `forfeit TeamCapulus`'
    ),
    status=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the current status of the crew battle with an overview of players, stocks taken, lobby ID, and stream.',
        usage='**Usage:** `status`',
        example='**Example:** `status`'
    ),
    chars=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints all characters, their compatible nicknames, and all of their emojis via your DMs.',
        usage='**Usage:** `chars`',
        example='**Example:** `chars`'
    ),
    clear=HelpDoc(
        help_txt=Categories.cb,
        brief='Clears the current crew battle in the channel.',
        usage='**Usage:** `clear`',
        example='**Example:** `clear`'
    ),
    confirm=HelpDoc(
        help_txt=Categories.cb,
        brief='Confirm the final scoresheet is correct once the battle is over.',
        usage='**Usage:** `confirm`',
        example='**Example:** `confirm`'
    ),
    char=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the character\'s corresponding emojis. This is a good way to test what emoji will be used on the scoresheet with the `end` command.',
        usage='**Usage:** `char (Char1)[AltNum]`',
        example='**Example:** `char Sephiroth7`'
    ),
    arena=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the arena information: if the arena ID/pass is specified, the arena will be set.',
        usage='**Usage:** `arena [ID/Pass]`',
        example='**Example:** `arena LFLTC/2020`'
    ),
    stream=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the stream information: if the streamlink is specified, the stream will be set.',
        usage='**Usage:** `stream [StreamLink]`',
        example='**Example:** `stream https://twitch.tv/LifelightCafe`'
    ),
    timer=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints the time in minutes and seconds since the last match finished.',
        usage='**Usage:** `timer`',
        example='**Example:** `timer`'
    ),
    guide=HelpDoc(
        help_txt=Categories.misc,
        brief='Provides the link to the usage guide for the bot.',
        usage='**Usage:** `guide`',
        example='**Example:** `guide`'
    ),
    coin=HelpDoc(
        help_txt=Categories.misc,
        brief='Flips a coin: if a user is mentioned, it will ask them to choose heads or tails.',
        usage='**Usage:** `coin [@User]`',
        example='**Example:** `coin @superhylia`'
    ),
    use_ext=HelpDoc(
        help_txt=Categories.cb,
        brief='Use the extension period to send in the next player on your team\'s behalf if you\'ve been sent in: otherwise, if a team is specified, the selected team will use the extension period.',
        usage='**Usage:** `use_ext [TeamName]`',
        example='**Example:** `use_ext TeamAqua`'
    ),
    ext=HelpDoc(
        help_txt=Categories.cb,
        brief='Prints whether or not either team has used their extension period.',
        usage='**Usage:** `ext`',
        example='**Example:** `ext`'
    ),
    countdown=HelpDoc(
        help_txt=Categories.cb,
        brief='Counts down for 3 seconds: if a time is specified, it will count down from that time in seconds.',
        usage='**Usage:** `countdown [Time]`',
        example='**Example:** `countdown 10`'
    ),
    credits=HelpDoc(
        help_txt=Categories.misc,
        brief='Provides the credits for the bot.',
        usage='**Usage:** `credits`',
        example='**Example:** `credits`'
    ),
    print_all_emojis=HelpDoc(
        help_txt=Categories.misc,
        brief='TEST.',
        usage='**Usage:** `print_all_emojis`',
        example='**Example:** `print_all_emojis`'
    ),
    thank=HelpDoc(
        help_txt=Categories.misc,
        brief='Thanks the original bot developer, AlexJett!',
        usage='**Usage:** `thank`',
        example='**Example:** `thank`'
    ),
    stagelist=HelpDoc(
        help_txt=Categories.misc,
        brief='Provides an image of the stagelist used in crew battles.',
        usage='**Usage:** `stagelist`',
        example='**Example:** `stagelist`'
    ),
    invite=HelpDoc(
        help_txt=Categories.misc,
        brief='Provides an invite to the Lifelight Café and Steamy League Discord servers.',
        usage='**Usage:** `invite`',
        example='**Example:** `invite`'
    ),
)
