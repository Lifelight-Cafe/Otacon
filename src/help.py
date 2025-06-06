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
    battle=HelpDoc(Categories.cb, 'Start a Mock Scoresheet in this channel with two team names and the size of people per team. You can also ping the corresponding team role.',
                   '**Usage:** battle Team1 Team2 Size', '**Example:** battle TeamThea @Team Aqua 5'),
    send=HelpDoc(Categories.cb, 'Sends in the mentioned/selected player for the specified team.', '',
                 '**Usage:** send @Player (TeamName)', '', '**Example:** send @superhylia TeamCapulus'),
    replace=HelpDoc(Categories.cb, 'Replaces current player with the tagged player', '', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    end=HelpDoc(Categories.cb, 'End the game with characters and stocks for both teams',
                '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    endlag=HelpDoc(Categories.cb,
                   'End the game with characters and stocks for both teams. '
                   'Same as end, but does not need to result in one player winning'
                   '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    resize=HelpDoc(Categories.cb, 'Resize the crew battle', '', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    undo=HelpDoc(Categories.cb, 'Undo the last match',
                '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    timerstock=HelpDoc(Categories.cb, 'Your current player will lose a stock to the timer', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    forfeit=HelpDoc(Categories.cb, 'Forfeits a crew battle', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    status=HelpDoc(Categories.cb, 'Current status of the battle', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    chars=HelpDoc(Categories.cb, 'Prints all characters names and their corresponding emojis', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    clear=HelpDoc(Categories.cb, 'Clears the current cb in the channel', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    confirm=HelpDoc(Categories.cb, 'Confirms the final score sheet is correct', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    char=HelpDoc(Categories.cb, 'Prints the character emoji (you can use this to test before entering in the sheet)',
                 '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    arena=HelpDoc(Categories.cb, 'Sets the stream if you are a streamer or leader, or prints it if you are not', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    stream=HelpDoc(Categories.cb, 'Sets the stream if you are a streamer or leader, or prints it if you are not', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    timer=HelpDoc(Categories.cb, 'Prints the time since the last match ended', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    guide=HelpDoc(Categories.misc, 'Links to the guide', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    coin=HelpDoc(Categories.misc, 'Flips a coin. If you mention a user it will '
                                  'prompt them to answer heads or tails before the flip.', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    use_ext=HelpDoc(Categories.cb, 'Uses your teams time extension in a crew battle', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    ext=HelpDoc(Categories.cb, 'Prints out extension status', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    countdown=HelpDoc(Categories.cb, 'Counts down for x seconds (defaults to 3).', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    credits=HelpDoc(Categories.misc, 'Lists credits for the bot.', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    print_all_emojis=HelpDoc(Categories.misc, 'TEST.', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),    
    thank=HelpDoc(Categories.misc, 'Thanks alexjett', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    stagelist=HelpDoc(Categories.misc, 'Returns the stagelist', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
    invite=HelpDoc(Categories.misc, 'Returns the server invite', '**Usage:** battle Team1 Team2 Size', '', '**Example:** battle TeamThea @Team Aqua 5'),
)
