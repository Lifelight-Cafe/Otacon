from typing import Optional, List, Tuple
import discord
import asyncio # For the Character class factory method example

CHARACTERS = {
    'banjo_and_kazooie': ['banjo', 'banjokazooie'],
    'bayonetta': ['bayo'],
    'bowser': [],
    'bowser_jr': ['bjr', 'jr', 'larry', 'royjr', 'wendy', 'iggy', 'morton', 'lemmy', 'ludwig'],
    'byleth': [],
    'captain_falcon': ['falcon'],
    'chrom': [],
    'clouds': ['cloud'],
    'corrin': [],
    'daisy': [],
    'dark_pit': ['dpit'],
    'dark_samus': ['damus', 'ds', 'darkus', 'dsamus'],
    'diddy_kong': ['diddy'],
    'donkey_kong': ['dk', 'monke', 'monkee'],
    'dr_mario': ['dr.mario', 'doc'],
    'duck_hunt': ['dh', 'dhd','doge'],
    'falco': [],
    'foxs': ['fox'],
    'ganondorf': ['ganon'],
    'greninja': ['gren'],
    'hero': [],
    'ice_climbers': ['ic', 'ics', 'icies', 'climbers', 'iceclimber'],
    'ike': [],
    'incineroar': ['incin', 'roar'],
    'inkling': ['ink'],
    'isabelle': ['isa'],
    'jigglypuff': ['jiggs', 'jigg', 'jiggly', 'puff'],
    'joker': [],
    'kazuya': ['kaz'],
    'ken': [],
    'king_dedede': ['dedede', 'ddd'],
    'king_k_rool': ['krool', 'croc'],
    'kirby': [],
    'links': ['link'],
    'little_mac': ['mac'],
    'lucario': [],
    'lucas': [],
    'lucina': ['luci'],
    'luigi': [],
    'mario': [],
    'marth': [],
    'mega_man': ['mm'],
    'meta_knight': ['mk'],
    'mewtwo': ['m2'],
    'mii_brawler': ['brawler'],
    'mii_gunner': ['gunner'],
    'mii_swordfighter': ['swordfighter', 'msf'],
    'min_min': ['min'],
    'mr_game_and_watch': ['gnw', 'g&w', 'gameandwatch', 'game&watch', 'gw', 'mgw'],
    'ness': ['wide', 'thicc'],
    'olimar': ['oli', 'alph'],
    'pac_man': ['pac'],
    'palutena': ['palu'],
    'peachs': ['peach'],
    'pichu': [],
    'pikachu': ['pika'],
    'piranha_plant': ['plant', 'pp'],
    'pit': [],
    'pokemon_trainer': ['pt', 'trainer'],
    'pythra': ['pyra', 'mythra', 'aegis', 'baeblades', 'myra'],
    'random': ['rand'],
    'richter': [],
    'ridley': [],
    'rob': ['r.o.b.'],
    'robin': [],
    'rosalina_and_luma': ['rosa', 'rosalina', 'rosaluma'],
    'roy': [],
    'ryu': [],
    'samus': [],
    'sephiroth': ['seph'],
    'sheik': ['shiek'],
    'shulk': [],
    'simon': [],
    'snakes': ['snake'],
    'sonic': [],
    'sora': [],
    'steve': ['enderman', 'alex', 'zombie'],
    'terry': [],
    'toon_link': ['tink'],
    'villager': ['villi', 'villy'],
    'wario': [],
    'wii_fit_trainer': ['wiifit', 'wft', 'wii'],
    'wolfs': ['wolf'],
    'yoshi': [],
    'young_link': ['yink'],
    'zelda': [],
    'zero_suit_samus': ['zss'],
}

S_SET = {
    'clouds',
    'wolfs',
    'links',
    'peachs',
    'snakes',
    'foxs'
}

for name in CHARACTERS:
    CHARACTERS[name].append(name.replace('_', ''))

CANONICAL_NAMES_MAP = {}  # Maps alternate names to canonical names.
for canonical_name in CHARACTERS:
    for alt_name in CHARACTERS[canonical_name]:
        CANONICAL_NAMES_MAP[alt_name] = canonical_name

# Assert that all names are distinct.
assert sum(len(x) for x in CHARACTERS.values()) == len(CANONICAL_NAMES_MAP)


def clean_emoji(input_str: str) -> str:
    if input_str.startswith('<:'):
        input_str = input_str[2:]
        if input_str.endswith('>'):
            input_str = input_str[:-1]
        # Handle potential animated emojis like <:name:id> or <a:name:id>
        parts = input_str.split(':')
        return parts[0] # Return just the name part
    return input_str


JR_LIST = ['bowser_jr', 'larry', 'royjr', 'wendy', 'iggy', 'morton', 'lemmy', 'ludwig']


def post_process(character: str, canonical_name: str, alt_num: int) -> Optional[str]:
    if canonical_name in S_SET and alt_num > 1:
        canonical_name = canonical_name[:-1]
    if canonical_name == 'bowser_jr': # Check against the base name for Bowser Jr. alts
        if alt_num > 1 and alt_num <= len(JR_LIST): # Ensure alt_num is within bounds for JR_LIST
            canonical_name = JR_LIST[alt_num -1] # JR_LIST is 0-indexed
            # alt_num = 1 # Skin is now embedded in canonical_name
        # If alt_num is 1, it remains bowser_jr, no change needed to alt_num
        # If character was one of the Koopalings directly (e.g. "larry"), it becomes bowser_jr in pre_process.
        # This post_process step then re-converts it to "larry" if an alt_num > 1 was specified,
        # or if it was "larry" initially (alt_num would be 1).
    elif character in JR_LIST and character != 'bowser_jr': # If input was a specific koopaling like "larry"
        canonical_name = character # Keep it as the specific koopaling
        # alt_num = 1 # Skin is embedded

    if canonical_name == 'olimar':
        if alt_num > 4: # Assuming 4 Olimar skins, then Alph skins
            canonical_name = 'alph'
            # alt_num -= 4 # Adjust alt_num relative to Alph (optional, depends on your emoji naming)
    if canonical_name == 'steve':
        if alt_num in [2, 4, 6]: # Steve (1,3,5) Alex (2,4,6) Zombie (7) Enderman (8)
            canonical_name = 'alex'
        elif alt_num == 7:
            canonical_name = 'zombie'
        elif alt_num == 8:
            canonical_name = 'enderman'
    # If an alt was processed (e.g. bowser_jr to larry), the alt_num effectively becomes 1 for that specific name
    # For Steve/Alex/etc., the specific name IS the alt.
    # For most characters, alt_num will be appended if > 1.
    # We need a clear convention: either 'character_name_altN' or 'specific_alt_name' (like larry)
    # The current logic seems to aim for specific_alt_name where applicable, otherwise append number.
    # Let's refine: if canonical_name was changed to a specific alt (e.g. 'larry', 'alph'), alt_num is conceptually 1 for that.
    if canonical_name in ['alph', 'alex', 'zombie', 'enderman'] or (canonical_name in JR_LIST and canonical_name != 'bowser_jr'):
        return canonical_name # These names are specific alts; no number needed

    return '{}{}'.format(canonical_name, '' if alt_num == 1 else str(alt_num))


def pre_process(input_str: str) -> Tuple[str, str, int]:
    input_str = clean_emoji(input_str)
    # Lowercase, remove ':', '_', and spaces.
    input_str = input_str.strip(':').lower().replace('_', '').replace(' ', '').replace('.', '') # also remove dots for dr.mario

    if not input_str:
        raise ValueError('Input string too short')
    last_char = input_str[-1]
    if last_char.isdigit():
        alt_num = int(last_char)
        if not 1 <= alt_num <= 8:
            raise ValueError('Alt number {} must be 1-8'.format(alt_num))
        character = input_str[:-1]
    else:
        alt_num = 1
        character = input_str
    
    if not character: # case where input was just a digit
        raise ValueError('Character name part is missing')

    if character in CANONICAL_NAMES_MAP:
        canonical_name = CANONICAL_NAMES_MAP[character]
        return character, canonical_name, alt_num
    else:
        raise ValueError('Unknown character: \'{}\'. Remember no spaces in character names. Try `,chars`'.format(character))


def string_to_canonical(input_str: str) -> Optional[str]:
    """
    Processes an input string to find the canonical representation for an emoji name.
    This can include specific alt names (like 'larry') or base names with alt numbers (like 'mario2').
    """
    try:
        character, base_canonical_name, alt_num = pre_process(input_str)
        return post_process(character, base_canonical_name, alt_num)
    except ValueError:
        return None # Or re-raise, depending on how you want to handle errors upstream

async def canonical_to_emote(canonical_name: str, bot: discord.Client) -> str:
    """
    Fetches an application emoji by its canonical name and returns its string representation.
    Returns a placeholder if not found.
    """
    if not canonical_name: # Should not happen if string_to_canonical filters Nones
        return ":question:"
    try:
        # This assumes your bot object is an instance of discord.Client or discord.Bot
        app_emoji = await bot.fetch_application_emoji(name=canonical_name)
        if app_emoji:
            return str(app_emoji)
        else:
            # This case might not be hit if fetch_application_emoji raises NotFound
            return f':{canonical_name}:' # Text fallback
    except discord.NotFound:
        return f':{canonical_name}_nf:' # Text fallback indicating "not found"
    except discord.HTTPException as e:
        print(f"HTTP error fetching application emoji {canonical_name}: {e}")
        return f':{canonical_name}_err:' # Text fallback for other errors
    except Exception as e: # Catch any other unexpected errors
        print(f"Unexpected error fetching application emoji {canonical_name}: {e}")
        return f':{canonical_name}_excp:'


async def string_to_emote(input_str: str, bot: discord.Client) -> Optional[str]:
    """
    Converts an input string (character name, possibly with alt) to an emoji string.
    """
    canonical_name = string_to_canonical(input_str)
    if canonical_name:
        return await canonical_to_emote(canonical_name, bot)
    return None # Return None if the character string couldn't be canonicalized


async def all_alts(input_str: str, bot: discord.Client) -> str:
    """
    Generates a string of all 8 alt emoji for a given base character input.
    """
    base_char_name = input_str
    last_char = base_char_name[-1]
    if last_char.isdigit(): # Remove any trailing digit if user accidentally provided one
        # Check if removing the digit makes it a valid character name part.
        # This is a bit tricky as pre_process handles this more robustly.
        # For simplicity, let's assume input_str is a base name like "mario", not "mario1".
        # Or, rely on string_to_canonical to handle "mario1" correctly for the first alt.
        # For all_alts, we usually want the base form.
        try:
            # Attempt to see if the string without the digit is a known char/alias.
            # This logic might need refinement based on how you want to interpret input_str here.
            # A safe bet is to always try to get the base canonical name first.
            _, base_canonical_for_check, _ = pre_process(base_char_name)
            # If pre_process worked, use its discovered character part.
            # However, pre_process expects potential alts. For `all_alts`, we want the root.
            # The simplest is to strip any number and proceed.
            if base_char_name[:-1] in CANONICAL_NAMES_MAP or base_char_name[:-1] in CHARACTERS:
                 base_char_name = base_char_name[:-1]

        except ValueError:
            pass # It wasn't a name ending in a digit that's also an alt.


    emoji_strings = []
    for i in range(1, 9):
        emote_str = await string_to_emote(base_char_name + str(i), bot)
        if emote_str:
            emoji_strings.append(emote_str)
        else:
            # Fallback if a specific alt doesn't resolve (e.g., bad name or emoji truly missing)
            # string_to_canonical might return None, or canonical_to_emote might return a fallback.
            # Let's use a placeholder based on the input attempt.
            processed_name_attempt = string_to_canonical(base_char_name + str(i))
            emoji_strings.append(f"[:{processed_name_attempt or (base_char_name + str(i) + '_err')}:]")
    return ''.join(emoji_strings)


async def all_emojis(bot: discord.Client) -> List[Tuple[str, str]]:
    """
    Generates a list of tuples, each containing a character's canonical name
    and its emoji representation(s) along with aliases.
    """
    ret = []
    # Sort CHARACTERS by c_name for consistent output
    sorted_character_items = sorted(CHARACTERS.items())

    for c_name, alts in sorted_character_items:
        aliases_str = ", ".join(alts) if alts else "None"
        if c_name.startswith('mii') or c_name == 'random' or c_name == 'sora':
            # These typically don't have numbered alts in the same way, or only one primary emoji.
            emote = await string_to_emote(c_name, bot) # string_to_emote will give one emoji or None
            ret.append((c_name, f'{emote or f":{c_name}_nf:"} AKA: {aliases_str}'))
            continue
        
        # For characters with alts:
        alt_emotes_str = await all_alts(c_name, bot)
        ret.append((c_name, f'{alt_emotes_str} AKA: {aliases_str}'))
    return ret


class Character:
    # Option 1: Async factory method (recommended)
    @classmethod
    async def create(cls, char_input: str, bot: Optional[discord.Client] = None, valid_emoji: bool = False):
        # Create a temporary instance with __init__ which is synchronous
        instance = cls(char_input, valid_emoji=valid_emoji) # Pass valid_emoji if used
        if bot and instance.emoji_name: # If bot is provided and emoji_name is valid
            try:
                instance.emoji = await canonical_to_emote(instance.emoji_name, bot)
            except Exception as e:
                print(f"Error resolving emoji for {instance.emoji_name} in Character.create: {e}")
                # Keep the text-based emoji_name as fallback
                if instance.emoji_name: # Should always be true if we are in this block
                     instance.emoji = f':{instance.emoji_name}_err_create:'
                else: # Should not happen if emoji_name was required
                     instance.emoji = f':{char_input}_err_create_noname:'

        elif not instance.emoji_name: # If emoji_name itself is None (e.g. from string_to_canonical)
            instance.emoji = f':{char_input}_invalid:' # Fallback for invalid char input

        return instance

    def __init__(self, char_input: str, valid_emoji: bool = False): # Removed bot from __init__
        # `valid_emoji` is not used in the current logic, but kept for compatibility if needed later
        self.base: Optional[str] = None
        self.skin: Optional[int] = None
        self.emoji_name: Optional[str] = None
        self.emoji: str = '' # Default to empty or a placeholder

        if not char_input:
            self.emoji = ':question:' # Placeholder for empty input
            return

        cleaned_char_input = clean_emoji(char_input) # Clean first, e.g. discord emoji string
        
        try:
            # pre_process gives: original_input_to_matcher, base_canonical_name, alt_num
            # We care about the base_canonical_name and alt_num for further processing.
            _original_char_part, self.base, self.skin = pre_process(cleaned_char_input)
            # string_to_canonical will give the final emoji name (e.g., "mario2", "larry")
            self.emoji_name = string_to_canonical(cleaned_char_input)

            if self.emoji_name:
                self.emoji = f':{self.emoji_name}:' # Default to text representation until resolved by factory
            else:
                # This means string_to_canonical failed (e.g. post_process returned None, or pre_process failed)
                self.emoji = f':{cleaned_char_input}_processing_error:'
                # self.base, self.skin might be from pre_process but post_process failed.

        except ValueError as e: # Error from pre_process
            self.emoji_name = None # Ensure emoji_name is None on error
            self.emoji = f':{cleaned_char_input}_invalid_input ({e}):' # Store error indication
            # self.base and self.skin would not have been set or are None

    def __str__(self):
        return self.emoji
