# Cut part of the logic from the original IOG Rando

# Format = { ID:  [Quantity, Type code (1=item, 2=ability, 3=statue,4=other),
#                  ROM Code, Name, TakesInventorySpace,
#                  ProgressionType (1=unlocks new locations,2=quest item,3=no progression)] }
item_pool = {
    # Items
    0: [2, 1, b"\x00", "Nothing", False, 3],
    1: [45, 1, b"\x01", "Red Jewel", False, 1],
    2: [1, 1, b"\x02", "Prison Key", True, 1],
    3: [1, 1, b"\x03", "Inca Statue A", True, 1],
    4: [1, 1, b"\x04", "Inca Statue B", True, 1],
    5: [0, 1, b"\x05", "Inca Melody", True, 3],
    6: [12, 1, b"\x06", "Herb", False, 3],
    7: [1, 1, b"\x07", "Diamond Block", True, 1],
    8: [1, 1, b"\x08", "Wind Melody", True, 1],
    9: [1, 1, b"\x09", "Lola's Melody", True, 1],
    10: [1, 1, b"\x0a", "Large Roast", True, 1],
    11: [1, 1, b"\x0b", "Mine Key A", True, 1],
    12: [1, 1, b"\x0c", "Mine Key B", True, 1],
    13: [1, 1, b"\x0d", "Memory Melody", True, 1],
    14: [4, 1, b"\x0e", "Crystal Ball", True, 2],
    15: [1, 1, b"\x0f", "Elevator Key", True, 1],
    16: [1, 1, b"\x10", "Mu Palace Key", True, 1],
    17: [1, 1, b"\x11", "Purification Stone", True, 1],
    18: [2, 1, b"\x12", "Statue of Hope", True, 1],
    19: [2, 1, b"\x13", "Rama Statue", False, 2],
    20: [1, 1, b"\x14", "Magic Dust", True, 2],
    21: [0, 1, b"\x15", "Blue Journal", False, 3],
    22: [1, 1, b"\x16", "Lance's Letter", False, 3],
    23: [1, 1, b"\x17", "Necklace Stones", True, 1],
    24: [1, 1, b"\x18", "Will", True, 1],
    25: [1, 1, b"\x19", "Teapot", True, 1],
    26: [3, 1, b"\x1a", "Mushroom Drops", True, 1],
    27: [0, 1, b"\x1b", "Bag of Gold", False, 3],
    28: [1, 1, b"\x1c", "Black Glasses", False, 1],
    29: [1, 1, b"\x1d", "Gorgon Flower", True, 1],
    30: [1, 1, b"\x1e", "Hieroglyph", False, 2],
    31: [1, 1, b"\x1f", "Hieroglyph", False, 2],
    32: [1, 1, b"\x20", "Hieroglyph", False, 2],
    33: [1, 1, b"\x21", "Hieroglyph", False, 2],
    34: [1, 1, b"\x22", "Hieroglyph", False, 2],
    35: [1, 1, b"\x23", "Hieroglyph", False, 2],
    36: [1, 1, b"\x24", "Aura", True, 1],
    37: [1, 1, b"\x25", "Lola's Letter", False, 1],
    38: [1, 1, b"\x26", "Father's Journal", False, 2],
    39: [1, 1, b"\x27", "Crystal Ring", False, 1],
    40: [1, 1, b"\x28", "Apple", True, 1],
    41: [1, 1, b"\x2e", "2 Red Jewels", False, 1],
    42: [1, 1, b"\x2f", "3 Red Jewels", False, 1],

    # Status Upgrades
    50: [3, 1, b"\x87", "HP Upgrade", False, 3],
    51: [1, 1, b"\x89", "DEF Upgrade", False, 3],
    52: [2, 1, b"\x88", "STR Upgrade", False, 3],
    53: [1, 1, b"\x8a", "Psycho Dash Upgrade", False, 3],
    54: [2, 1, b"\x8b", "Dark Friar Upgrade", False, 3],
    55: [0, 1, b"\x8c", "Heart Piece", False, 3],

    # Abilities
    60: [0, 2, "", "Nothing", False, 3],
    61: [1, 2, "", "Psycho Dash", False, 1],
    62: [1, 2, "", "Psycho Slider", False, 1],
    63: [1, 2, "", "Spin Dash", False, 1],
    64: [1, 2, "", "Dark Friar", False, 1],
    65: [1, 2, "", "Aura Barrier", False, 1],
    66: [1, 2, "", "Earthquaker", False, 1],
    67: [0, 2, "", "Firebird", False, 1],

    # Mystic Statues
    100: [1, 3, "", "Mystic Statue 1", False, 2],
    101: [1, 3, "", "Mystic Statue 2", False, 2],
    102: [1, 3, "", "Mystic Statue 3", False, 2],
    103: [1, 3, "", "Mystic Statue 4", False, 2],
    104: [1, 3, "", "Mystic Statue 5", False, 2],
    105: [1, 3, "", "Mystic Statue 6", False, 2],
    106: [0, 3, "", "Mystic Statue", False, 2],

    # Event Switches
    500: [0, 4, "", "Kara Released", False, 1],
    501: [0, 4, "", "Itory: Got Lilly", False, 1],
    502: [0, 4, "", "Moon Tribe: Healed Spirits", False, 1],
    503: [0, 4, "", "Inca: Beat Castoth", False, 1],
    504: [0, 4, "", "Freejia: Found Laborer", False, 1],
    505: [0, 4, "", "Neil's: Memory Restored", False, 1],
    506: [0, 4, "", "Sky Garden: Map 82 NW Switch", False, 1],
    507: [0, 4, "", "Sky Garden: Map 82 NE Switch", False, 1],
    508: [0, 4, "", "Sky Garden: Map 82 NW Switch", False, 1],
    509: [0, 4, "", "Sky Garden: Map 84 Switch", False, 1],
    510: [0, 4, "", "Seaside: Fountain Purified", False, 1],
    511: [0, 4, "", "Mu: Water Lowered 1", False, 1],
    512: [0, 4, "", "Mu: Water Lowered 2", False, 1],
    513: [0, 4, "", "Angel: Puzzle Complete", False, 1],
    514: [0, 4, "", "Mt Kress: Drops Used 1", False, 1],
    515: [0, 4, "", "Mt Kress: Drops Used 2", False, 1],
    516: [0, 4, "", "Mt Kress: Drops Used 3", False, 1],
    517: [0, 4, "", "Pyramid: Hieroglyphs Placed", False, 1],
    518: [0, 4, "", "Babel: Castoth Defeated", False, 1],
    519: [0, 4, "", "Babel: Viper Defeated", False, 1],
    520: [0, 4, "", "Babel: Vampires Defeated", False, 1],
    521: [0, 4, "", "Babel: Sand Fanger Defeated", False, 1],
    522: [0, 4, "", "Babel: Mummy Queen Defeated", False, 1],
    523: [0, 4, "", "Mansion: Solid Arm Defeated", False, 1],

    # Misc
    600: [0, 4, "", "Freedan Access", False, 1],
    601: [0, 4, "", "Glitches", False, 1],
    602: [0, 4, "", "Early Firebird", False, 1]
}

# Define Item/Ability/Statue locations
# Format: { ID: [Region, Type (1=item,2=ability,3=statue,4=other), Filled Flag,
#                Filled Item, Restricted Items, Item Addr, Text Addr, Text2 Addr,
#                Special (map# or inventory addr), Name, Swapped Flag]}
#         (For random start, [6]=Type, [7]=XY_spawn_data)
item_locations = {
    # Jeweler
    0:   [2, 1, False, 0, [], "8d019", "8d19d", "", "8d260", "Jeweler Reward 1                    "],
    1:   [3, 1, False, 0, [], "8d028", "8d1ba", "", "8d274", "Jeweler Reward 2                    "],
    2:   [4, 1, False, 0, [], "8d037", "8d1d7", "", "8d288", "Jeweler Reward 3                    "],
    3:   [5, 1, False, 0, [], "8d04a", "8d1f4", "", "8d29c", "Jeweler Reward 4                    "],
    4:   [6, 1, False, 0, [], "8d059", "8d211", "", "8d2b0", "Jeweler Reward 5                    "],
    5:   [7, 1, False, 0, [], "8d069", "8d2ea", "", "8d2c4", "Jeweler Reward 6                    "],

    # South Cape
    6:   [21, 1, False, 0, [],  "F51D",  "F52D", "F543", "", "South Cape: Bell Tower              "],
    7:   [20, 1, False, 0, [], "4846e", "48479",     "", "", "South Cape: Fisherman               "],  # text2 was 0c6a1
    8:   [26, 1, False, 0, [],  "F59D",  "F5AD", "F5C3", "", "South Cape: Lance's House           "],
    9:   [23, 1, False, 0, [], "499e4", "49be5",     "", "", "South Cape: Lola                    "],

    10:  [21, 2, False, 0, [64, 65, 66], "c830a", "Safe", b"\xE0\x00\x70\x00\x83\x00\x43", b"\x01", "South Cape: Dark Space              "],

    # Edward's
    11:  [30, 1, False, 0, [], "4c214", "4c299", "", "", "Edward's Castle: Hidden Guard       "],
    12:  [30, 1, False, 0, [], "4d0ef", "4d141", "", "", "Edward's Castle: Basement           "],
    13:  [32, 1, False, 0, [], "4d32f", "4d4b1", "", "", "Edward's Prison: Hamlet             "],  # text 4d5f4?

    14:  [32, 2, False, 0, [64, 65, 66], "c8637", "", "", b"\x0b", "Edward's Prison: Dark Space         "],

    # Underground Tunnel
    15:  [42, 1, False, 0, [], "1AFA9",    "",     "", "", "Underground Tunnel: Spike's Chest   "],
    16:  [44, 1, False, 0, [], "1AFAE",    "",     "", "", "Underground Tunnel: Small Room Chest"],
    17:  [48, 1, False, 0, [], "1AFB3",    "",     "", "", "Underground Tunnel: Ribber's Chest  "],
    18:  [49, 1, False, 0, [], "F61D", "F62D", "F643", "", "Underground Tunnel: Barrels         "],

    19:  [47, 2, False, 0, [], "c8aa2", "Unsafe", b"\xA0\x00\xD0\x04\x83\x00\x74", b"\x12", "Underground Tunnel: Dark Space      "],  # Always open

    # Itory
    20:  [51, 1, False, 0, [],  "F69D",  "F6AD",  "F6C3", "", "Itory Village: Logs                 "],
    21:  [58, 1, False, 0, [], "4f375", "4f38d", "4f3a8", "", "Itory Village: Cave                 "],

    22:  [51, 2, False, 0, [64, 65, 66], "c8b34", "Safe", b"\x30\x04\x90\x00\x83\x00\x35", b"\x15", "Itory Village: Dark Space           "],

    # Moon Tribe
    23:  [62, 1, False, 0, [], "4fae1", "4faf9", "4fb16", "", "Moon Tribe: Cave                    "],

    # Inca
    24:  [71, 1, False, 0, [], "1AFB8",      "",      "", "", "Inca Ruins: Diamond-Block Chest     "],
    25:  [92, 1, False, 0, [], "1AFC2",      "",      "", "", "Inca Ruins: Broken Statues Chest    "],
    26:  [83, 1, False, 0, [], "1AFBD",      "",      "", "", "Inca Ruins: Stone Lord Chest        "],
    27:  [93, 1, False, 0, [], "1AFC6",      "",      "", "", "Inca Ruins: Slugger Chest           "],
    28:  [76, 1, False, 0, [], "9c5bd", "9c614", "9c637", "", "Inca Ruins: Singing Statue          "],

    29:  [96, 2, False, 0, [], "c9302", "Unsafe", b"\x10\x01\x90\x00\x83\x00\x32", b"\x28", "Inca Ruins: Dark Space 1            "],  # Always open
    30:  [93, 2, False, 0, [], "c923b", "Unsafe", b"\xC0\x01\x50\x01\x83\x00\x32", b"\x26", "Inca Ruins: Dark Space 2            "],
    31:  [77, 2, False, 0, [], "c8db8",       "",                              "", b"\x1e", "Inca Ruins: Final Dark Space        "],

    # Gold Ship
    32:  [100, 1, False, 0, [], "5965e", "5966e", "", "", "Gold Ship: Seth                     "],

    # Diamond Coast
    33:  [102, 1, False, 0, [], "F71D", "F72D", "F743", "", "Diamond Coast: Jar                  "],

    # Freejia
    34:  [121, 1, False, 0, [],  "F79D",  "F7AD",  "F7C3", "", "Freejia: Hotel                      "],
    35:  [110, 1, False, 0, [], "5b6d8", "5b6e8",      "", "", "Freejia: Creepy Guy                 "],
    36:  [110, 1, False, 0, [], "5cf9e", "5cfae", "5cfc4", "", "Freejia: Trash Can 1                "],
    37:  [110, 1, False, 0, [], "5cf3d", "5cf49",      "", "", "Freejia: Trash Can 2                "],  # text2 was 5cf5b
    38:  [115, 1, False, 0, [], "5b8b7", "5b962", "5b9ee", "", "Freejia: Snitch                     "],  # text1 was @5b94d

    39:  [125, 2, False, 0, [64, 65, 66], "c96ce", "Safe", b"\x40\x00\xa0\x00\x83\x00\x11", b"\x34", "Freejia: Dark Space                 "],

    # Diamond Mine
    40:  [134, 1, False, 0, [], "1AFD0",      "",      "", "", "Diamond Mine: Chest                 "],
    41:  [137, 1, False, 0, [], "5d7e4", "5d819", "5d830", "", "Diamond Mine: Trapped Laborer       "],
    42:  [143, 1, False, 0, [], "aa777", "aa85c",      "", "", "Diamond Mine: Laborer w/Elevator Key"],  # text1 was aa811
    43:  [148, 1, False, 0, [], "5d4d2", "5d4eb", "5d506", "", "Diamond Mine: Morgue                "],
    44:  [149, 1, False, 0, [], "aa757", "aa7ef",      "", "", "Diamond Mine: Laborer w/Mine Key    "],  # text1 was aa7b4
    45:  [150, 1, False, 0, [], "5d2b0", "5d2da",      "", "", "Diamond Mine: Sam                   "],

    46:  [136, 2, False, 0, [], "c9a87", "Unsafe", b"\xb0\x01\x70\x01\x83\x00\x32", b"\x40", "Diamond Mine: Appearing Dark Space  "],  # Always open
    47:  [131, 2, False, 0, [], "c98b0", "Unsafe", b"\xd0\x00\xc0\x00\x83\x00\x61", b"\x3d", "Diamond Mine: Dark Space at Wall    "],
    48:  [142, 2, False, 0, [], "c9b49",       "",                              "", b"\x42", "Diamond Mine: Dark Space behind Wall"],

    # Sky Garden
    49:  [172, 1, False, 0, [], "1AFDD", "", "", "", "Sky Garden: (NE) Platform Chest     "],
    50:  [173, 1, False, 0, [], "1AFD9", "", "", "", "Sky Garden: (NE) Blue Cyber Chest   "],
    51:  [174, 1, False, 0, [], "1AFD5", "", "", "", "Sky Garden: (NE) Statue Chest       "],
    52:  [180, 1, False, 0, [], "1AFE2", "", "", "", "Sky Garden: (SE) Dark Side Chest    "],
    53:  [185, 1, False, 0, [], "1AFE7", "", "", "", "Sky Garden: (SW) Ramp Chest         "],
    54:  [186, 1, False, 0, [], "1AFEC", "", "", "", "Sky Garden: (SW) Dark Side Chest    "],
    55:  [194, 1, False, 0, [], "1AFF1", "", "", "", "Sky Garden: (NW) Top Chest          "],
    56:  [194, 1, False, 0, [], "1AFF5", "", "", "", "Sky Garden: (NW) Bottom Chest       "],

    57:  [170, 2, False, 0, [64, 65, 66], "c9d63",   "Safe", b"\x90\x00\x70\x00\x83\x00\x22", b"\x4c", "Sky Garden: Dark Space (Foyer)      "],
    58:  [169, 2, False, 0,           [], "ca505", "Unsafe", b"\x70\x00\xa0\x00\x83\x00\x11", b"\x56", "Sky Garden: Dark Space (SE)         "],  # in the room
    59:  [183, 2, False, 0,           [], "ca173",       "",                              "", b"\x51", "Sky Garden: Dark Space (SW)         "],
    60:  [195, 2, False, 0,           [], "ca422", "Unsafe", b"\x20\x00\x70\x00\x83\x00\x44", b"\x54", "Sky Garden: Dark Space (NW)         "],

    # Seaside Palace
    61:  [202, 1, False, 0, [], "1AFFF",      "",      "", "", "Seaside Palace: Side Room Chest     "],
    62:  [200, 1, False, 0, [], "1AFFA",      "",      "", "", "Seaside Palace: First Area Chest    "],
    63:  [205, 1, False, 0, [], "1B004",      "",      "", "", "Seaside Palace: Second Area Chest   "],
    64:  [206, 1, False, 0, [], "68af7", "68ea9", "68f02", "", "Seaside Palace: Buffy               "],
    65:  [208, 1, False, 0, [], "6922d", "6939e", "693b7", "", "Seaside Palace: Coffin              "],  # text1 was 69377

    66:  [200, 2, False, 0, [64, 65, 66], "ca574", "Safe", b"\xf0\x02\x90\x00\x83\x00\x64", b"\x5a", "Seaside Palace: Dark Space          "],

    # Mu
    67:  [217, 1, False, 0, [], "1B012",      "", "", "", "Mu: Empty Chest 1                   "],
    68:  [220, 1, False, 0, [], "1B01B",      "", "", "", "Mu: Empty Chest 2                   "],
    69:  [225, 1, False, 0, [], "698be", "698d2", "", "", "Mu: Hope Statue 1                   "],
    70:  [236, 1, False, 0, [], "69966", "69975", "", "", "Mu: Hope Statue 2                   "],
    71:  [215, 1, False, 0, [], "1B00D",      "", "", "", "Mu: Chest s/o Hope Room 2           "],
    72:  [214, 1, False, 0, [], "1B009",      "", "", "", "Mu: Rama Chest N                    "],
    73:  [219, 1, False, 0, [], "1B016",      "", "", "", "Mu: Rama Chest E                    "],

    74:  [218, 2, False, 0, [], "ca92d", "", "", b"\x60", "Mu: Open Dark Space                 "],  # Always open
    75:  [228, 2, False, 0, [], "caa99", "", "", b"\x62", "Mu: Slider Dark Space               "],

    # Angel Village
    76:  [254, 1, False, 0, [], "F81D", "F82D", "F843", "", "Angel Village: Dance Hall           "],
    77:  [255, 2, False, 0, [64, 65, 66], "caf67", "Safe", b"\x90\x01\xb0\x00\x83\x01\x12", b"\x6c", "Angel Village: Dark Space           "],

    # Angel Dungeon
    78:  [265, 1, False, 0, [], "1B020",    "",     "", "", "Angel Dungeon: Slider Chest         "],
    79:  [271, 1, False, 0, [], "F89D", "F8AD", "F8C3", "", "Angel Dungeon: Ishtar's Room        "],
    80:  [274, 1, False, 0, [], "1B02A",    "",     "", "", "Angel Dungeon: Puzzle Chest 1       "],
    81:  [274, 1, False, 0, [], "1B02E",    "",     "", "", "Angel Dungeon: Puzzle Chest 2       "],
    82:  [273, 1, False, 0, [], "1B025",    "",     "", "", "Angel Dungeon: Ishtar's Chest       "],

    # Watermia
    83:  [280, 1, False, 0, [],  "F91D",  "F92D",  "F943", "", "Watermia: West Jar                  "],
    85:  [286, 1, False, 0, [], "7ad21", "7aede",      "", "", "Watermia: Lance                     "],  # text2 was 7afa7
    86:  [283, 1, False, 0, [],  "F99D",  "F9AD",  "F9C3", "", "Watermia: Gambling House            "],
    87:  [280, 1, False, 0, [], "79248", "79288", "792a1", "", "Watermia: Russian Glass             "],

    88:  [282, 2, False, 0, [64, 65, 66], "cb644", "Safe", b"\x40\x00\xa0\x00\x83\x00\x11", b"\x7c", "Watermia: Dark Space                "],

    # Great Wall
    89:  [290, 1, False, 0, [], "7b5c5", "7b5d1", "", "", "Great Wall: Necklace 1              "],
    90:  [292, 1, False, 0, [], "7b625", "7b631", "", "", "Great Wall: Necklace 2              "],
    91:  [292, 1, False, 0, [], "1B033",      "", "", "", "Great Wall: Chest 1                 "],
    92:  [294, 1, False, 0, [], "1B038",      "", "", "", "Great Wall: Chest 2                 "],

    93:  [295, 2, False, 0, [], "cbb11", "Unsafe", b"\x60\x00\xc0\x02\x83\x20\x38", b"\x85", "Great Wall: Archer Dark Space       "],
    94:  [297, 2, False, 0, [], "cbb80", "Unsafe", b"\x50\x01\x80\x04\x83\x00\x63", b"\x86", "Great Wall: Platform Dark Space     "],  # Always open
    95:  [300, 2, False, 0, [], "cbc60",       "",                              "", b"\x88", "Great Wall: Appearing Dark Space    "],

    # Euro
    96:  [310, 1, False, 0, [],  "FA1D",  "FA2D",  "FA43", "", "Euro: Alley                         "],
    97:  [310, 1, False, 0, [], "7c0b3", "7c0f3",      "", "", "Euro: Apple Vendor                  "],
    98:  [320, 1, False, 0, [], "7e51f", "7e534", "7e54a", "", "Euro: Hidden House                  "],
    99:  [323, 1, False, 0, [], "7cd12", "7cd39", "7cd9b", "", "Euro: Store Item 1                  "],
    100: [323, 1, False, 0, [], "7cdf9", "7ce28", "7ce3e", "", "Euro: Store Item 2                  "],  # text2 was 7cedd
    101: [321, 1, False, 0, [],  "FA9D",  "FAAD",  "FAC3", "", "Euro: Shrine                        "],
    102: [315, 1, False, 0, [], "7df58", "7e10a",      "", "", "Euro: Ann                           "],

    103: [325, 2, False, 0, [64, 65, 66], "cc0b0", "Safe", b"\xb0\x00\xb0\x00\x83\x00\x11", b"\x99", "Euro: Dark Space                    "],

    # Mt Temple
    104: [336, 1, False, 0, [], "1B03D", "", "", "", "Mt. Temple: Red Jewel Chest         "],
    105: [338, 1, False, 0, [], "1B042", "", "", "", "Mt. Temple: Drops Chest 1           "],
    106: [342, 1, False, 0, [], "1B047", "", "", "", "Mt. Temple: Drops Chest 2           "],
    107: [343, 1, False, 0, [], "1B04C", "", "", "", "Mt. Temple: Drops Chest 3           "],
    108: [345, 1, False, 0, [], "1B051", "", "", "", "Mt. Temple: Final Chest             "],

    109: [332, 2, False, 0, [], "cc24f", "Unsafe", b"\xf0\x01\x10\x03\x83\x00\x44", b"\xa1", "Mt. Temple: Dark Space 1            "],
    110: [337, 2, False, 0, [], "cc419", "Unsafe", b"\xc0\x07\xc0\x00\x83\x00\x28", b"\xa3", "Mt. Temple: Dark Space 2            "],
    111: [343, 2, False, 0, [], "cc7b8",       "",                              "", b"\xa7", "Mt. Temple: Dark Space 3            "],

    # Natives'
    112: [353, 1, False, 0, [],  "FB1D",  "FB2D", "FB43", "", "Natives' Village: Statue Room       "],
    113: [354, 1, False, 0, [], "893af", "8942a",     "", "", "Natives' Village: Statue            "],

    114: [350, 2, False, 0, [64, 65, 66], "cca37", "Safe", b"\xc0\x01\x50\x00\x83\x00\x22", b"\xac", "Natives' Village: Dark Space        "],

    # Ankor Wat
    115: [361, 1, False, 0, [], "1B056",      "",      "", "", "Ankor Wat: Ramp Chest               "],
    116: [370, 1, False, 0, [], "1B05B",      "",      "", "", "Ankor Wat: Flyover Chest            "],
    117: [378, 1, False, 0, [], "1B060",      "",      "", "", "Ankor Wat: U-Turn Chest             "],
    118: [382, 1, False, 0, [], "1B065",      "",      "", "", "Ankor Wat: Drop Down Chest          "],
    119: [389, 1, False, 0, [], "1B06A",      "",      "", "", "Ankor Wat: Forgotten Chest          "],
    120: [380, 1, False, 0, [], "89fa3", "89fbb",      "", "", "Ankor Wat: Glasses Location         "],  # slow text @89fdc
    121: [391, 1, False, 0, [], "89adc", "89af1", "89b07", "", "Ankor Wat: Spirit                   "],  # item was 89b0d, text was 89e2e

    122: [372, 2, False, 0, [], "cce92", "Unsafe", b"\x20\x04\x30\x03\x83\x00\x46", b"\xb6", "Ankor Wat: Garden Dark Space        "],  # Always open
    123: [377, 2, False, 0, [], "cd0a2",       "",                              "", b"\xb8", "Ankor Wat: Earthquaker Dark Space   "],
    124: [383, 2, False, 0, [], "cd1a7", "Unsafe", b"\xb0\x02\xc0\x01\x83\x00\x33", b"\xbb", "Ankor Wat: Drop Down Dark Space     "],  # Always open

    # Dao
    125: [400, 1, False, 0, [], "8b1b0",      "",      "", "", "Dao: Entrance Item 1                "],
    126: [400, 1, False, 0, [], "8b1b5",      "",      "", "", "Dao: Entrance Item 2                "],
    127: [400, 1, False, 0, [],  "FB9D",  "FBAD",  "FBC3", "", "Dao: East Grass                     "],
    128: [403, 1, False, 0, [], "8b016", "8b073", "8b090", "", "Dao: Snake Game                     "],

    129: [400, 2, False, 0, [64, 65, 66], "cd3d0", "Safe", b"\x20\x00\x80\x00\x83\x00\x23", b"\xc3", "Dao: Dark Space                     "],

    # Pyramid
    130: [411, 1, False, 0, [], "8dcb7", "8e66c", "8e800", "", "Pyramid: Dark Space Top             "],  # text2 was 8e800
    131: [412, 1, False, 0, [],  "FC1D",  "FC2D",  "FC43", "", "Pyramid: Hidden Platform            "],
    132: [442, 1, False, 0, [], "8c7b2", "8c7c9",      "", "", "Pyramid: Hieroglyph 1               "],
    133: [422, 1, False, 0, [], "1B06F",      "",      "", "", "Pyramid: Room 2 Chest               "],
    134: [443, 1, False, 0, [], "8c879", "8c88c",      "", "", "Pyramid: Hieroglyph 2               "],
    135: [432, 1, False, 0, [], "1B079",      "",      "", "", "Pyramid: Room 3 Chest               "],
    136: [444, 1, False, 0, [], "8c921", "8c934",      "", "", "Pyramid: Hieroglyph 3               "],
    137: [439, 1, False, 0, [], "1B07E",      "",      "", "", "Pyramid: Room 4 Chest               "],
    138: [445, 1, False, 0, [], "8c9c9", "8c9dc",      "", "", "Pyramid: Hieroglyph 4               "],
    139: [428, 1, False, 0, [], "1B074",      "",      "", "", "Pyramid: Room 5 Chest               "],
    140: [446, 1, False, 0, [], "8ca71", "8ca84",      "", "", "Pyramid: Hieroglyph 5               "],
    141: [447, 1, False, 0, [], "8cb19", "8cb2c",      "", "", "Pyramid: Hieroglyph 6               "],

    142: [413, 2, True, 0, [], "cd570", "Unsafe", b"\xc0\x01\x90\x03\x83\x00\x44", b"\xcc", "Pyramid: Dark Space Bottom          "],  # Always open

    # Babel
    143: [461, 1, False, 0, [],  "FC9D",  "FCAD",  "FCC3", "", "Babel: Pillow                       "],
    144: [461, 1, False, 0, [], "99a4f", "99ae4", "99afe", "", "Babel: Force Field                  "],  # item was  99a61

    145: [461, 2, False, 0, [64, 65, 66], "ce09b", "Forced Unsafe", b"\x90\x07\xb0\x01\x83\x10\x28", b"\xdf", "Babel: Dark Space Bottom            "],
    146: [472, 2, False, 0, [64, 65, 66], "ce159",          "Safe", b"\xb0\x02\xb0\x01\x83\x10\x23", b"\xe3", "Babel: Dark Space Top               "],

    # Jeweler's Mansion
    147: [480, 1, False, 0, [], "1B083", "", "", "", "Jeweler's Mansion: Chest            "],

    # Mystic Statues
    148: [101, 3, False, 0, [101, 102, 103, 104, 105], "", "", "", "", "Castoth Prize                       "],
    149: [198, 3, False, 0, [100, 102, 103, 104, 105], "", "", "", "", "Viper Prize                         "],
    150: [244, 3, False, 0, [100, 101, 103, 104, 105], "", "", "", "", "Vampires Prize                      "],
    151: [302, 3, False, 0, [100, 101, 102, 104, 105], "", "", "", "", "Sand Fanger Prize                   "],
    152: [448, 3, False, 0, [100, 101, 102, 103, 105], "", "", "", "", "Mummy Queen Prize                   "],
    153: [479, 3, False, 0, [100, 101, 102, 103, 104], "", "", "", "", "Babel Prize                         "],

    # Event Switches
    500: [500, 4, True, 500, [], "", "", "", "", "Kara                                "],
    501: [501, 4, True, 501, [], "", "", "", "", "Lilly                               "],
    502: [502, 4, True, 502, [], "", "", "", "", "Moon Tribe: Spirits Healed          "],
    503: [503, 4, True, 503, [], "", "", "", "", "Inca: Castoth defeated              "],
    504: [504, 4, True, 504, [], "", "", "", "", "Freejia: Found Laborer              "],
    505: [505, 4, True, 505, [], "", "", "", "", "Neil's Memory Restored              "],
    506: [506, 4, True, 506, [], "", "", "", "", "Sky Garden: Map 82 NW Switch        "],
    507: [507, 4, True, 507, [], "", "", "", "", "Sky Garden: Map 82 NE Switch        "],
    508: [508, 4, True, 508, [], "", "", "", "", "Sky Garden: Map 82 SE Switch        "],
    509: [509, 4, True, 509, [], "", "", "", "", "Sky Garden: Map 84 Switch           "],
    510: [510, 4, True, 510, [], "", "", "", "", "Seaside: Fountain Purified          "],
    511: [511, 4, True, 511, [], "", "", "", "", "Mu: Water Lowered 1                 "],
    512: [512, 4, True, 512, [], "", "", "", "", "Mu: Water Lowered 2                 "],
    513: [513, 4, True, 513, [], "", "", "", "", "Angel: Puzzle Complete              "],
    514: [514, 4, True, 514, [], "", "", "", "", "Mt Kress: Drops used 1              "],
    515: [515, 4, True, 515, [], "", "", "", "", "Mt Kress: Drops used 2              "],
    516: [516, 4, True, 516, [], "", "", "", "", "Mt Kress: Drops used 3              "],
    517: [517, 4, True, 517, [], "", "", "", "", "Pyramid: Hieroglyphs placed         "],
    518: [518, 4, True, 518, [], "", "", "", "", "Babel: Castoth defeated             "],
    519: [519, 4, True, 519, [], "", "", "", "", "Babel: Viper defeated               "],
    520: [520, 4, True, 520, [], "", "", "", "", "Babel: Vampires defeated            "],
    521: [521, 4, True, 521, [], "", "", "", "", "Babel: Sand Fanger defeated         "],
    522: [522, 4, True, 522, [], "", "", "", "", "Babel: Mummy Queen defeated         "],
    523: [523, 4, True, 523, [], "", "", "", "", "Mansion: Solid Arm defeated         "],

    # Misc
    600: [600, 4, True, 600, [], "", "", "", "", "Freedan Access                          "],
    601: [601, 4, True, 601, [], "", "", "", "", "Glitches                                "],
    602: [602, 4, True, 602, [], "", "", "", "", "Early Firebird                          "],
    603: [491, 4, True,  67, [], "", "", "", "", "Firebird                                "]
}

# World graph
# Format: { Region ID:
#                   Traversed_flag, [AccessibleRegions], type(0=other/misc,1=exterior,2=interior), [continentID,areaID,layer,MapID],
#                   4: DS_access (0=no_access,1=any_DS,2=form_change_DS),
#                   5: RegionName,
#                   6: [ItemsToRemove],
#                   7: ForceFormChange,
#                   8: [AccessibleFromNodes],
#                   9: [Accessible_DS_nodes],
#                   10: [Accessible_Nodes_w_Logic],
#                   11: [item_locations],
#                   12: [origin_logic],
#                   13: [dest_logic],
#                   14: [origin_exits],
#                   15: [dest_exits]        }
graph = {
    # Game Start
    0: [False, [22], 0, [0,0,0,b"\x00"], 0, "Game Start", [], True, [], [], [], [], [], [], [], []],

    # Jeweler
    1: [False, [], 0, [0,0,0,b"\x00"], 0, "Jeweler Access", [], False, [], [], [], [], [], [], [], []],
    2: [False, [], 0, [0,0,0,b"\x00"], 0, "Jeweler Reward 1", [], False, [], [], [], [], [], [], [], []],
    3: [False, [], 0, [0,0,0,b"\x00"], 0, "Jeweler Reward 2", [], False, [], [], [], [], [], [], [], []],
    4: [False, [], 0, [0,0,0,b"\x00"], 0, "Jeweler Reward 3", [], False, [], [], [], [], [], [], [], []],
    5: [False, [], 0, [0,0,0,b"\x00"], 0, "Jeweler Reward 4", [], False, [], [], [], [], [], [], [], []],
    6: [False, [], 0, [0,0,0,b"\x00"], 0, "Jeweler Reward 5", [], False, [], [], [], [], [], [], [], []],
    7: [False, [], 0, [0,0,0,b"\x00"], 0, "Jeweler Reward 6", [], False, [], [], [], [], [], [], [], []],
    8: [False, [], 0, [0,0,0,b"\x00"], 0, "Jeweler Reward 7", [], False, [], [], [], [], [], [], [], []],

    # Overworld Menus
    10: [False, [20,30,50,60,63],      0, [1,0,0,b"\x00"], 0, "Overworld: SW Continent", [], True, [], [], [], [], [], [], [], []],
    11: [False, [102,110,133,160,162], 0, [2,0,0,b"\x00"], 0, "Overworld: SE Continent", [], True, [], [], [], [], [], [], [], []],
    12: [False, [250,280,290],         0, [3,0,0,b"\x00"], 0, "Overworld: NE Continent", [], True, [], [], [], [], [], [], [], []],
    13: [False, [310,330,350,360],     0, [4,0,0,b"\x00"], 0, "Overworld: N Continent", [], True, [], [], [], [], [], [], [], []],
    14: [False, [400,410],             0, [5,0,0,b"\x00"], 0, "Overworld: NW Continent", [], True, [], [], [], [], [], [], [], []],

    # Passage Menus
    15: [False, [], 0, [0,0,0,b"\x00"], 0, "Passage: Seth", [], True, [], [], [], [], [], [], [], []],
    16: [False, [], 0, [0,0,0,b"\x00"], 0, "Passage: Moon Tribe", [], True, [], [], [], [], [], [], [], []],
    17: [False, [], 0, [0,0,0,b"\x00"], 0, "Passage: Neil", [], True, [], [], [], [], [], [], [], []],

    # South Cape
    20: [False, [1,10],  1, [1,1,0,b"\x00"], 0, "South Cape: Main Area", [], False, [], [], [], [], [], [], [], []],
    21: [False, [20],    1, [1,1,0,b"\x00"], 0, "South Cape: School Roof", [], False, [], [], [], [], [], [], [], []],
    22: [False, [],      2, [1,1,0,b"\x00"], 0, "South Cape: School", [], False, [], [], [], [], [], [], [], []],
    23: [False, [],      2, [1,1,0,b"\x00"], 0, "South Cape: Will's House", [], False, [], [], [], [], [], [], [], []],
    24: [False, [],      2, [1,1,0,b"\x00"], 0, "South Cape: East House", [], False, [], [], [], [], [], [], [], []],
    25: [False, [],      2, [1,1,0,b"\x00"], 0, "South Cape: Seth's House", [], False, [], [], [], [], [], [], [], []],
    26: [False, [],      2, [1,1,0,b"\x00"], 0, "South Cape: Lance's House", [], False, [], [], [], [], [], [], [], []],
    27: [False, [],      2, [1,1,0,b"\x00"], 0, "South Cape: Erik's House", [], False, [], [], [], [], [], [], [], []],
    28: [False, [],      2, [1,1,0,b"\x00"], 0, "South Cape: Seaside Cave", [], False, [], [], [], [], [], [], [], []],

    # Edward's / Prison
    30: [False, [10], 1, [1,2,0,b"\x00"], 0, "Edward's Castle: Main Area", [], False, [], [], [], [], [], [], [], []],
    31: [False, [30], 1, [1,2,0,b"\x00"], 0, "Edward's Castle: Behind Guard", [], False, [], [], [], [], [], [], [], []],
    32: [False, [],   2, [1,2,0,b"\x00"], 0, "Edward's Prison: Will's Cell", [2], False, [], [], [], [], [], [], [], []],
    33: [False, [],   2, [1,2,0,b"\x00"], 0, "Edward's Prison: Prison Main", [2], False, [], [], [], [], [], [], [], []],

    # Underground Tunnel
    40: [False, [],   2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Map 12", [], False, [], [], [], [], [], [], [], []],
    41: [False, [],   2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Map 13", [], False, [], [], [], [], [], [], [], []],
    42: [False, [],   2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Map 14", [], False, [], [], [], [], [], [], [], []],
    43: [False, [],   2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Map 15", [], False, [], [], [], [], [], [], [], []],
    44: [False, [],   2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Map 16", [], False, [], [], [], [], [], [], [], []],
    45: [False, [],   2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Map 17 (entrance)", [], False, [], [], [], [], [], [], [], []],
    46: [False, [45], 2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Map 17 (exit open)", [], False, [], [], [], [], [], [], [], []],
    47: [False, [],   2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Map 18 (before bridge)", [], False, [], [], [], [], [], [], [], []],
    48: [False, [],   2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Map 18 (after bridge)", [], False, [], [], [], [], [], [], [], []],
    49: [False, [],   2, [1,2,0,b"\x00"], 0, "Underground Tunnel: Exit", [], True, [], [], [], [], [], [], [], []],

    # Itory
    50: [False, [10],     1, [1,3,0,b"\x00"], 0, "Itory: Entrance", [9], False, [], [], [], [], [], [], [], []],
    51: [False, [50],     1, [1,3,0,b"\x00"], 0, "Itory: Main Area", [], False, [], [], [], [], [], [], [], []],
    52: [False, [],       1, [1,3,0,b"\x00"], 0, "Itory: Lilly's Back Porch", [], False, [], [], [], [], [], [], [], []],
    53: [False, [],       2, [1,3,0,b"\x00"], 0, "Itory: West House", [], False, [], [], [], [], [], [], [], []],
    54: [False, [],       2, [1,3,0,b"\x00"], 0, "Itory: North House", [], False, [], [], [], [], [], [], [], []],
    55: [False, [],       2, [1,3,0,b"\x00"], 0, "Itory: Lilly's House", [23], False, [], [], [], [], [], [], [], []],
    56: [False, [],       2, [1,3,0,b"\x00"], 0, "Itory: Cave", [], False, [], [], [], [], [], [], [], []],
    57: [False, [56],     2, [1,3,0,b"\x00"], 0, "Itory: Cave (behind false wall)", [], False, [], [], [], [], [], [], [], []],
    58: [False, [],       2, [1,3,0,b"\x00"], 0, "Itory: Cave (secret room)", [], False, [], [], [], [], [], [], [], []],
    59: [False, [55,501], 0, [1,3,0,b"\x00"], 0, "Itory: Got Lilly", [], False, [], [], [], [], [], [], [], []],

    # Moon Tribe / Inca Entrance
    60: [False, [10],     1, [1,4,0,b"\x00"], 0, "Moon Tribe: Main Area", [25], False, [], [], [], [], [], [], [], []],
    61: [False, [],       2, [1,4,0,b"\x00"], 0, "Moon Tribe: Cave", [], False, [], [], [], [], [], [], [], []],
    62: [False, [61],     2, [1,4,0,b"\x00"], 0, "Moon Tribe: Cave (Pedestal)", [], False, [], [], [], [], [], [], [], []],
    63: [False, [10],     1, [1,5,0,b"\x00"], 0, "Inca: Entrance", [], False, [], [], [], [], [], [], [], []],
    64: [False, [60,502], 0, [1,4,0,b"\x00"], 0, "Moon Tribe: Spirits Awake", [], False, [], [], [], [], [], [], [], []],

    # Inca Ruins
    70: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 29 (NE)", [], False, [], [], [], [], [], [], [], []],
    71: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 29 (NW)", [], False, [], [], [], [], [], [], [], []],
    72: [False, [70,73],  2, [1,5,0,b"\x00"], 0, "Inca: Map 29 (N)", [], False, [], [], [], [], [], [], [], []],
    73: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 29 (center)", [], False, [], [], [], [], [], [], [], []],
    74: [False, [72],     2, [1,5,0,b"\x00"], 0, "Inca: Map 29 (SW)", [], False, [], [], [], [], [], [], [], []],
    75: [False, [72,99],  2, [1,5,0,b"\x00"], 0, "Inca: Map 29 (SE)", [], False, [], [], [], [], [], [], [], []],
    76: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 29 (statue head)", [], False, [], [], [], [], [], [], [], []],
    77: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 30 (first area)", [3, 4], False, [], [], [], [], [], [], [], []],
    78: [False, [77],     2, [1,5,0,b"\x00"], 0, "Inca: Map 30 (second area)", [], False, [], [], [], [], [], [], [], []],
    79: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 31", [], False, [], [], [], [], [], [], [], []],
    80: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 32 (entrance)", [], False, [], [], [], [], [], [], [], []],
    81: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 32 (behind statue)", [], False, [], [], [], [], [], [], [], []],
    82: [False, [83],     2, [1,5,0,b"\x00"], 0, "Inca: Map 33 (entrance)", [], False, [], [], [], [], [], [], [], []],
    83: [False, [82],     2, [1,5,0,b"\x00"], 0, "Inca: Map 33 (over ramp)", [], False, [], [], [], [], [], [], [], []],      # Need to prevent softlocks here
    84: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 34", [], False, [], [], [], [], [], [], [], []],
    85: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 35 (entrance)", [], False, [], [], [], [], [], [], [], []],
    86: [False, [85],     2, [1,5,0,b"\x00"], 0, "Inca: Map 35 (over ramp)", [], False, [], [], [], [], [], [], [], []],
    87: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 36 (main)", [8], False, [], [], [], [], [], [], [], []],
    88: [False, [87],     2, [1,5,0,b"\x00"], 0, "Inca: Map 36 (exit opened)", [], False, [], [], [], [], [], [], [], []],
    89: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 37 (main area)", [7], False, [], [], [], [], [], [], [], []],
    90: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 37 (tile bridge)", [], False, [], [], [], [], [], [], [], []],     # Check for potential softlock?
    91: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 38 (south section)", [], False, [], [], [], [], [], [], [], []],
    92: [False, [91],     2, [1,5,0,b"\x00"], 0, "Inca: Map 38 (behind statues)", [], False, [], [], [], [], [], [], [], []],
    93: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 38 (north section)", [], False, [], [], [], [], [], [], [], []],
    94: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 39", [], False, [], [], [], [], [], [], [], []],
    95: [False, [96],     2, [1,5,0,b"\x00"], 0, "Inca: Map 40 (entrance)", [], False, [], [], [], [], [], [], [], []],
    96: [False, [95],     2, [1,5,0,b"\x00"], 0, "Inca: Map 40 (past tiles)", [], False, [], [], [], [], [], [], [], []],
    97: [False, [98,503], 2, [1,5,0,b"\x00"], 0, "Inca: Boss Room", [], True, [], [], [], [], [], [], [], []],       # might need to add an exit for this
    98: [False, [97],     2, [1,5,0,b"\x00"], 0, "Inca: Behind Boss Room", [], False, [], [], [], [], [], [], [], []],
    99: [False, [],       2, [1,5,0,b"\x00"], 0, "Inca: Map 29 (SE door)", [], False, [], [], [], [], [], [], [], []],

    # Gold Ship / Diamond Coast
    100: [False, [104], 1, [1,5,0,b"\x00"], 0, "Gold Ship: Deck", [], False, [], [], [], [], [], [], [], []],
    101: [False, [],    2, [1,5,0,b"\x00"], 0, "Gold Ship: Interior", [], False, [], [], [], [], [], [], [], []],
    102: [False, [11],  1, [2,6,0,b"\x00"], 0, "Diamond Coast: Main Area", [], False, [], [], [], [], [], [], [], []],
    103: [False, [],    2, [2,6,0,b"\x00"], 0, "Diamond Coast: House", [], False, [], [], [], [], [], [], [], []],
    104: [False, [],    0, [1,5,0,b"\x00"], 0, "Gold Ship: Crow's Nest Passage", [], False, [], [], [], [], [], [], [], []],

    # Freejia
    110: [False, [11],       1, [2,7,0,b"\x00"], 0, "Freejia: Main Area", [], False, [], [], [], [], [], [], [], []],
    111: [False, [1, 110],   1, [2,7,0,b"\x00"], 0, "Freejia: 2-story House Roof", [], False, [], [], [], [], [], [], [], []],
    112: [False, [],         1, [2,7,0,b"\x00"], 0, "Freejia: Laborer House Roof", [], False, [], [], [], [], [], [], [], []],
    113: [False, [110, 114], 1, [2,7,0,b"\x00"], 0, "Freejia: Labor Trade Roof", [], False, [], [], [], [], [], [], [], []],
    114: [False, [110, 112], 1, [2,7,0,b"\x00"], 0, "Freejia: Back Alley", [], False, [], [], [], [], [], [], [], []],
    115: [False, [110],      0, [2,7,0,b"\x00"], 0, "Freejia: Slaver", [], False, [], [], [], [], [], [], [], []],
    116: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: West House", [], False, [], [], [], [], [], [], [], []],
    117: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: 2-story House", [], False, [], [], [], [], [], [], [], []],
    118: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: Lovers' House", [], False, [], [], [], [], [], [], [], []],
    119: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: Hotel (common area)", [], False, [], [], [], [], [], [], [], []],
    120: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: Hotel (west room)", [], False, [], [], [], [], [], [], [], []],
    121: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: Hotel (east room)", [], False, [], [], [], [], [], [], [], []],
    122: [False, [504],      2, [2,7,0,b"\x00"], 0, "Freejia: Laborer House", [], False, [], [], [], [], [], [], [], []],
    123: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: Messy House", [], False, [], [], [], [], [], [], [], []],
    124: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: Erik House", [], False, [], [], [], [], [], [], [], []],
    125: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: Dark Space House", [], False, [], [], [], [], [], [], [], []],
    126: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: Labor Trade House", [], False, [], [], [], [], [], [], [], []],
    127: [False, [],         2, [2,7,0,b"\x00"], 0, "Freejia: Labor Market", [], False, [], [], [], [], [], [], [], []],

    # Diamond Mine
    130: [False, [131], 2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 61 (entrance)", [], False, [], [], [], [], [], [], [], []],
    131: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 61 (behind barriers)", [], False, [], [], [], [], [], [], [], []],
    132: [False, [131], 2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 61 (false wall)", [], False, [], [], [], [], [], [], [], []],
    133: [False, [11],  2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 62", [], False, [], [], [], [], [], [], [], []],
    134: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 63 (main)", [], False, [], [], [], [], [], [], [], []],
    135: [False, [134], 2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 63 (elevator)", [], False, [], [], [], [], [], [], [], []],
    136: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 64 (main)", [], False, [], [], [], [], [], [], [], []],
    137: [False, [136], 2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 64 (trapped laborer)", [], False, [], [], [], [], [], [], [], []],
    138: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 65 (main)", [], False, [], [], [], [], [], [], [], []],
    139: [False, [138], 2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 65 (behind ramp)", [], False, [], [], [], [], [], [], [], []],
    140: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 66 (elevator 1)", [], False, [], [], [], [], [], [], [], []],
    141: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 66 (elevator 2)", [], False, [], [], [], [], [], [], [], []],
    142: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 66 (Dark Space)", [], False, [], [], [], [], [], [], [], []],
    143: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 66 (laborer)", [], False, [], [], [], [], [], [], [], []],
    144: [False, [145], 2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 67 (entrance)", [], False, [], [], [], [], [], [], [], []],
    145: [False, [144], 2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 67 (exit)", [], False, [], [], [], [], [], [], [], []],         # potential softlock?
    146: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 68 (main)", [], False, [], [], [], [], [], [], [], []],
    147: [False, [146], 2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 68 (door open)", [], False, [], [], [], [], [], [], [], []],
    148: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 69", [], False, [], [], [], [], [], [], [], []],
    149: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 70", [], False, [], [], [], [], [], [], [], []],
    150: [False, [],    2, [2,8,0,b"\x00"], 0, "Diamond Mine: Map 71", [], False, [], [], [], [], [], [], [], []],

    # Neil's Cottage / Nazca
    160: [False, [11],         2, [2,9,0,b"\x00"],  0, "Neil's Cottage", [13], False, [], [], [], [], [], [], [], []],
    161: [False, [17,160,505], 2, [2,9,0,b"\x00"],  0, "Neil's Cottage: Neil", [], False, [], [], [], [], [], [], [], []],
    162: [False, [11],         1, [2,10,0,b"\x00"], 0, "Nazca Plain", [], False, [], [], [], [], [], [], [], []],

    # Sky Garden
    167: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 83 (SE)", [], False, [], [], [], [], [], [], [], []],
    168: [False, [181],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 81 (north)", [], False, [], [], [], [], [], [], [], []],
    169: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 86 (DS Room)", [], False, [], [], [], [], [], [], [], []],
    170: [False, [],         1, [2,10,0,b"\x00"], 0, "Sky Garden: Foyer", [14, 14, 14, 14], False, [], [], [], [], [], [], [], []],
    171: [False, [],         1, [2,10,0,b"\x00"], 0, "Sky Garden: Boss Entrance", [], False, [], [], [], [], [], [], [], []],
    172: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 77 (main)", [], False, [], [], [], [], [], [], [], []],
    173: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 77 (SW)", [], False, [], [], [], [], [], [], [], []],
    174: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 77 (SE)", [], False, [], [], [], [], [], [], [], []],
    175: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 78", [], False, [], [], [], [], [], [], [], []],
    176: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 79 (main)", [], False, [], [], [], [], [], [], [], []],
    177: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 79 (center)", [], False, [], [], [], [], [], [], [], []],
    178: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 79 (behind barrier)", [], False, [], [], [], [], [], [], [], []],
    179: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 80 (north)", [], False, [], [], [], [], [], [], [], []],
    180: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 80 (south)", [], False, [], [], [], [], [], [], [], []],
    181: [False, [168],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 81 (main)", [], False, [], [], [], [], [], [], [], []],
    182: [False, [181],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 81 (west)", [], False, [], [], [], [], [], [], [], []],
    183: [False, [182],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 81 (Dark Space cage)", [], False, [], [], [], [], [], [], [], []],
    184: [False, [182],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 81 (SE platform)", [], False, [], [], [], [], [], [], [], []],
    185: [False, [182],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 81 (SW platform)", [], False, [], [], [], [], [], [], [], []],
    186: [False, [506],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 82 (north)", [], False, [], [], [], [], [], [], [], []],        # deal with switches
    187: [False, [508],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 82 (south)", [], False, [], [], [], [], [], [], [], []],
    188: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 82 (NE)", [], False, [], [], [], [], [], [], [], []],
    189: [False, [188,507],  2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 82 (switch cage)", [], False, [], [], [], [], [], [], [], []],
    190: [False, [191],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 83 (NE)", [], False, [], [], [], [], [], [], [], []],
    191: [False, [190, 192], 2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 83 (NW)", [], False, [], [], [], [], [], [], [], []],
    192: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 83 (center)", [], False, [], [], [], [], [], [], [], []],
    193: [False, [194],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 83 (SW)", [], False, [], [], [], [], [], [], [], []],
    194: [False, [167],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 83 (chests)", [], False, [], [], [], [], [], [], [], []],
    195: [False, [196],      2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 84 (main)", [], False, [], [], [], [], [], [], [], []],
    196: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 84 (NE)", [], False, [], [], [], [], [], [], [], []],
    197: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 84 (behind statue)", [], False, [], [], [], [], [], [], [], []],
    198: [False, [],         2, [2,10,0,b"\x00"], 0, "Sky Garden: Boss Room", [], True, [], [], [], [], [], [], [], []],
    199: [False, [197,509],  2, [2,10,0,b"\x00"], 0, "Sky Garden: Map 84 (statue)", [], False, [], [], [], [], [], [], [], []],

    # Seaside Palace
    200: [False,    [], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Area 1", [16], False, [], [], [], [], [], [], [], []],
    201: [False, [200], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Area 1 (door unlocked)", [], False, [], [], [], [], [], [], [], []],
    202: [False,    [], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Area 1 NE Room", [], False, [], [], [], [], [], [], [], []],
    203: [False,    [], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Area 1 NW Room", [], False, [], [], [], [], [], [], [], []],
    204: [False,    [], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Area 1 SE Room", [], False, [], [], [], [], [], [], [], []],
    205: [False,    [], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Area 2", [], False, [], [], [], [], [], [], [], []],
    206: [False, [200], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Buffy", [], False, [], [], [], [], [], [], [], []],
    207: [False,    [], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Area 2 SW Room", [], False, [], [], [], [], [], [], [], []],
    208: [False, [205], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Coffin", [], False, [], [], [], [], [], [], [], []],
    209: [False,    [], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Fountain", [17], False, [], [], [], [], [], [], [], []],
    210: [False,    [], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Mu Passage", [16], False, [], [], [], [], [], [], [], []],
    211: [False, [210], 2, [3,11,0,b"\x00"], 0, "Seaside Palace: Mu Passage (door unlocked)", [], False, [], [], [], [], [], [], [], []],

    # Mu
    212: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 95 (top)", [], False, [], [], [], [], [], [], [], []],
    213: [False, [212],      2, [3,12,1,b"\x00"], 0, "Mu: Map 95 (middle E)", [], False, [], [], [], [], [], [], [], []],
    214: [False, [],         2, [3,12,1,b"\x00"], 0, "Mu: Map 95 (middle W)", [], False, [], [], [], [], [], [], [], []],
    215: [False, [213],      2, [3,12,2,b"\x00"], 0, "Mu: Map 95 (bottom E)", [], False, [], [], [], [], [], [], [], []],
    216: [False, [214],      2, [3,12,2,b"\x00"], 0, "Mu: Map 95 (bottom W)", [], False, [], [], [], [], [], [], [], []],
    217: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 96 (top)", [], False, [], [], [], [], [], [], [], []],
    218: [False, [217],      2, [3,12,1,b"\x00"], 0, "Mu: Map 96 (middle)", [], False, [], [], [], [], [], [], [], []],
    219: [False, [],         2, [3,12,2,b"\x00"], 0, "Mu: Map 96 (bottom)", [], False, [], [], [], [], [], [], [], []],
    220: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 97 (top main)", [], False, [], [], [], [], [], [], [], []],
    221: [False, [222, 223], 2, [3,12,0,b"\x00"], 0, "Mu: Map 97 (top island)", [], False, [], [], [], [], [], [], [], []],
    222: [False, [],         2, [3,12,1,b"\x00"], 0, "Mu: Map 97 (middle NE)", [], False, [], [], [], [], [], [], [], []],
    223: [False, [221],      2, [3,12,1,b"\x00"], 0, "Mu: Map 97 (middle SW)", [], False, [], [], [], [], [], [], [], []],
    224: [False, [],         2, [3,12,2,b"\x00"], 0, "Mu: Map 97 (bottom)", [], False, [], [], [], [], [], [], [], []],
    225: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 98 (top S)", [], False, [], [], [], [], [], [], [], []],
    226: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 98 (top N)", [], False, [], [], [], [], [], [], [], []],
    227: [False, [226],      2, [3,12,1,b"\x00"], 0, "Mu: Map 98 (middle E)", [], False, [], [], [], [], [], [], [], []],
    228: [False, [],         2, [3,12,1,b"\x00"], 0, "Mu: Map 98 (middle W)", [], False, [], [], [], [], [], [], [], []],
    229: [False, [227],      2, [3,12,2,b"\x00"], 0, "Mu: Map 98 (bottom E)", [], False, [], [], [], [], [], [], [], []],
    230: [False, [228],      2, [3,12,2,b"\x00"], 0, "Mu: Map 98 (bottom W)", [], False, [], [], [], [], [], [], [], []],
    231: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 99 (Room of Hope 1)", [18], False, [], [], [], [], [], [], [], []],
    232: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 99 (Room of Hope 2)", [18], False, [], [], [], [], [], [], [], []],
    233: [False, [],         2, [3,12,1,b"\x00"], 0, "Mu: Map 100 (middle E)", [], False, [], [], [], [], [], [], [], []],
    234: [False, [],         2, [3,12,1,b"\x00"], 0, "Mu: Map 100 (middle W)", [], False, [], [], [], [], [], [], [], []],
    235: [False, [],         2, [3,12,2,b"\x00"], 0, "Mu: Map 100 (bottom)", [], False, [], [], [], [], [], [], [], []],
    236: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 101 (top)", [], False, [], [], [], [], [], [], [], []],
    237: [False, [],         2, [3,12,1,b"\x00"], 0, "Mu: Map 101 (middle W)", [], False, [], [], [], [], [], [], [], []],
    238: [False, [236],      2, [3,12,1,b"\x00"], 0, "Mu: Map 101 (middle E)", [], False, [], [], [], [], [], [], [], []],
    239: [False, [],         2, [3,12,2,b"\x00"], 0, "Mu: Map 101 (bottom)", [], False, [], [], [], [], [], [], [], []],
    240: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 102 (pedestals)", [19, 19], False, [], [], [], [], [], [], [], []],
    241: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 102 (statues placed)", [], False, [], [], [], [], [], [], [], []],  # might need an exit for this
    242: [False, [],         2, [3,12,0,b"\x00"], 0, "Mu: Map 102 (statue get)", [], False, [], [], [], [], [], [], [], []],
    243: [False, [244],      2, [3,12,0,b"\x00"], 0, "Mu: Boss Room (entryway)", [], False, [], [], [], [], [], [], [], []],    # Might need to add an exit for this?
    244: [False, [242,243],  2, [3,12,0,b"\x00"], 0, "Mu: Boss Room (main)", [], True, [], [], [], [], [], [], [], []],
    245: [False, [212],      2, [3,12,0,b"\x00"], 0, "Mu: Map 95 (top, Slider exit)", [], False, [], [], [], [], [], [], [], []],
    246: [False, [226],      2, [3,12,0,b"\x00"], 0, "Mu: Map 98 (top, Slider exit)", [], False, [], [], [], [], [], [], [], []],
    247: [False, [231,511],  0, [3,12,0,b"\x00"], 0, "Mu: Water lowered 1", [], False, [], [], [], [], [], [], [], []],
    248: [False, [232,512],  0, [3,12,0,b"\x00"], 0, "Mu: Water lowered 2", [], False, [], [], [], [], [], [], [], []],

    # Angel Village
    250: [False, [12], 1, [3,13,0,b"\x00"], 0, "Angel Village: Outside", [], True, [], [], [], [], [], [], [], []],
    251: [False, [1],  2, [3,13,0,b"\x00"], 0, "Angel Village: Underground", [], False, [], [], [], [], [], [], [], []],
    252: [False, [],   2, [3,13,0,b"\x00"], 0, "Angel Village: Room 1", [], False, [], [], [], [], [], [], [], []],
    253: [False, [],   2, [3,13,0,b"\x00"], 0, "Angel Village: Room 2", [], False, [], [], [], [], [], [], [], []],
    254: [False, [],   2, [3,13,0,b"\x00"], 0, "Angel Village: Dance Hall", [], False, [], [], [], [], [], [], [], []],
    255: [False, [],   2, [3,13,0,b"\x00"], 0, "Angel Village: DS Room", [], False, [], [], [], [], [], [], [], []],
    #256: [False, [],   2, [3,13,0,b"\x00"], 0, "Angel Village: Room 3", [], False, [], [], [], [], [], [], [], []],

    # Angel Dungeon
    260: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 109", [], False, [], [], [], [], [], [], [], []],
    261: [False, [278], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 110 (main)", [], False, [], [], [], [], [], [], [], []],
    262: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 111", [], False, [], [], [], [], [], [], [], []],
    263: [False, [279], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 112 (main)", [], False, [], [], [], [], [], [], [], []],
    264: [False, [263], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 112 (slider)", [], False, [], [], [], [], [], [], [], []],
    265: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 112 (alcove)", [], False, [], [], [], [], [], [], [], []],
    266: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 113", [], False, [], [], [], [], [], [], [], []],
    267: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 114 (main)", [], False, [], [], [], [], [], [], [], []],
    268: [False, [267], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 114 (slider exit)", [], False, [], [], [], [], [], [], [], []],
    269: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 115 (main)", [], False, [], [], [], [], [], [], [], []],
    270: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 116 (portrait room)", [], False, [], [], [], [], [], [], [], []],
    271: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 116 (side room)", [], False, [], [], [], [], [], [], [], []],
    272: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 116 (Ishtar's room)", [], False, [], [], [], [], [], [], [], []],
    273: [False, [272], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 116 (Ishtar's chest)", [], False, [], [], [], [], [], [], [], []],
    274: [False, [513], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Puzzle Room", [], False, [], [], [], [], [], [], [], []],
    275: [False, [265], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 112 (alcove slider)", [], False, [], [], [], [], [], [], [], []],
    276: [False, [277], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 115 (slider exit)", [], False, [], [], [], [], [], [], [], []],
    277: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 115 (foyer)", [], False, [], [], [], [], [], [], [], []],
    278: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 110 (past Draco)", [], False, [], [], [], [], [], [], [], []],
    279: [False,    [], 2, [3,13,0,b"\x00"], 0, "Angel Dungeon: Map 112 (past Draco)", [], False, [], [], [], [], [], [], [], []],

    # Watermia
    280: [False,     [12], 1, [3,14,0,b"\x00"], 0, "Watermia: Main Area", [24], False, [], [], [], [], [], [], [], []],
    #281: [False, [15,280], 0, [3,14,0,b"\x00"], 0, "Watermia: Bridge Man", [], False, [], [], [], [], [], [], [], []],
    282: [False,       [], 2, [3,14,0,b"\x00"], 0, "Watermia: DS House", [], False, [], [], [], [], [], [], [], []],
    283: [False,      [1], 2, [3,14,0,b"\x00"], 0, "Watermia: Gambling House", [], False, [], [], [], [], [], [], [], []],
    284: [False,       [], 2, [3,14,0,b"\x00"], 0, "Watermia: West House", [], False, [], [], [], [], [], [], [], []],
    285: [False,       [], 2, [3,14,0,b"\x00"], 0, "Watermia: East House", [], False, [], [], [], [], [], [], [], []],
    286: [False,       [], 2, [3,14,0,b"\x00"], 0, "Watermia: Lance's House", [], False, [], [], [], [], [], [], [], []],
    287: [False,       [], 2, [3,14,0,b"\x00"], 0, "Watermia: NW House", [], False, [], [], [], [], [], [], [], []],
    288: [False,    [280], 0, [3,14,0,b"\x00"], 0, "Watermia: Stablemaster", [], True, [], [], [], [], [], [], [], []],

    # Great Wall
    290: [False, [12],  2, [3,15,0,b"\x00"], 0, "Great Wall: Map 130", [], False, [], [], [], [], [], [], [], []],
    291: [False, [292], 2, [3,15,0,b"\x00"], 0, "Great Wall: Map 131 (NW)", [], False, [], [], [], [], [], [], [], []],
    292: [False, [293], 2, [3,15,0,b"\x00"], 0, "Great Wall: Map 131 (S)", [], False, [], [], [], [], [], [], [], []],
    293: [False, [],    2, [3,15,0,b"\x00"], 0, "Great Wall: Map 131 (NE)", [], False, [], [], [], [], [], [], [], []],
    294: [False, [296], 2, [3,15,0,b"\x00"], 0, "Great Wall: Map 133 (W)", [], False, [], [], [], [], [], [], [], []],
    295: [False, [296], 2, [3,15,0,b"\x00"], 0, "Great Wall: Map 133 (center)", [], False, [], [], [], [], [], [], [], []],
    296: [False, [],    2, [3,15,0,b"\x00"], 0, "Great Wall: Map 133 (E)", [], False, [], [], [], [], [], [], [], []],
    297: [False, [],    2, [3,15,0,b"\x00"], 0, "Great Wall: Map 134", [], False, [], [], [], [], [], [], [], []],
    298: [False, [],    2, [3,15,0,b"\x00"], 0, "Great Wall: Map 135 (W)", [], False, [], [], [], [], [], [], [], []],
    299: [False, [],    2, [3,15,0,b"\x00"], 0, "Great Wall: Map 135 (E)", [], False, [], [], [], [], [], [], [], []],
    300: [False, [],    2, [3,15,0,b"\x00"], 0, "Great Wall: Map 136 (W)", [], False, [], [], [], [], [], [], [], []],
    301: [False, [],    2, [3,15,0,b"\x00"], 0, "Great Wall: Map 136 (E)", [], False, [], [], [], [], [], [], [], []],
    302: [False, [303], 2, [3,15,0,b"\x00"], 0, "Great Wall: Boss Room (entrance)", [], False, [], [], [], [], [], [], [], []],
    303: [False, [],    2, [3,15,0,b"\x00"], 0, "Great Wall: Boss Room (exit)", [], False, [], [], [], [], [], [], [], []],

    # Euro
    310: [False, [13],  1, [4,16,0,b"\x00"], 0, "Euro: Main Area", [24], False, [], [], [], [], [], [], [], []],
    311: [False, [310], 0, [4,16,0,b"\x00"], 0, "Euro: Stablemaster", [], True, [], [], [], [], [], [], [], []],
    312: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Rolek Company", [], False, [], [], [], [], [], [], [], []],
    313: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: West House", [], False, [], [], [], [], [], [], [], []],
    314: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Rolek Mansion", [40], False, [], [], [], [], [], [], [], []],
    315: [False, [314], 0, [4,16,0,b"\x00"], 0, "Euro: Ann", [], False, [], [], [], [], [], [], [], []],
    316: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Guest Room", [], False, [], [], [], [], [], [], [], []],
    317: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Central House", [], False, [], [], [], [], [], [], [], []],
    318: [False, [1],   2, [4,16,0,b"\x00"], 0, "Euro: Jeweler House", [], False, [], [], [], [], [], [], [], []],
    319: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Twins House", [], False, [], [], [], [], [], [], [], []],
    320: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Hidden House", [], False, [], [], [], [], [], [], [], []],
    321: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Shrine", [], False, [], [], [], [], [], [], [], []],
    322: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Explorer's House", [], False, [], [], [], [], [], [], [], []],
    323: [False, [324], 2, [4,16,0,b"\x00"], 0, "Euro: Store Entrance", [], False, [], [], [], [], [], [], [], []],
    324: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Store Exit", [], False, [], [], [], [], [], [], [], []],
    325: [False, [],    2, [4,16,0,b"\x00"], 0, "Euro: Dark Space House", [], False, [], [], [], [], [], [], [], []],

    # Mt. Kress
    330: [False, [13],        2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 160", [], False, [], [], [], [], [], [], [], []],
    331: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 161 (E)", [], False, [], [], [], [], [], [], [], []],
    332: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 161 (W)", [], False, [], [], [], [], [], [], [], []],
    333: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 162 (main)", [26], False, [], [], [], [], [], [], [], []],
    334: [False, [333],       2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 162 (S)", [], False, [], [], [], [], [], [], [], []],
    335: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 162 (NW)", [], False, [], [], [], [], [], [], [], []],
    336: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 162 (SE)", [], False, [], [], [], [], [], [], [], []],
    337: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 163", [], False, [], [], [], [], [], [], [], []],
    338: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 164", [], False, [], [], [], [], [], [], [], []],
    339: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 165 (S)", [26], False, [], [], [], [], [], [], [], []],
    340: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 165 (NE)", [26], False, [], [], [], [], [], [], [], []],
    341: [False, [338],       2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 165 (NW)", [], False, [], [], [], [], [], [], [], []],
    342: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 166", [], False, [], [], [], [], [], [], [], []],
    343: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 167", [], False, [], [], [], [], [], [], [], []],
    344: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 168", [], False, [], [], [], [], [], [], [], []],
    345: [False, [],          2, [4,17,0,b"\x00"], 0, "Mt. Kress: Map 169", [], False, [], [], [], [], [], [], [], []],

    # Natives' Village
    350: [False, [13],  1, [4,18,0,b"\x00"], 0, "Natives' Village: Main Area", [10], False, [], [], [], [], [], [], [], []],
    351: [False, [350], 0, [4,18,0,b"\x00"], 0, "Natives' Village: Child Guide", [], True, [], [], [], [], [], [], [], []],
    352: [False, [],    2, [4,18,0,b"\x00"], 0, "Natives' Village: West House", [], False, [], [], [], [], [], [], [], []],
    353: [False, [],    2, [4,18,0,b"\x00"], 0, "Natives' Village: House w/Statues", [29], False, [], [], [], [], [], [], [], []],
    354: [False, [353], 0, [4,18,0,b"\x00"], 0, "Natives' Village: Statues Awake", [], False, [], [], [], [], [], [], [], []],

    # Ankor Wat
    360: [False, [13],  2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 176", [], False, [], [], [], [], [], [], [], []],
    361: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 177 (E)", [], False, [], [], [], [], [], [], [], []],
    362: [False, [361], 2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 177 (W)", [], False, [], [], [], [], [], [], [], []],
    363: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 178 (S)", [], False, [], [], [], [], [], [], [], []],
    364: [False, [363], 2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 178 (center)", [], False, [], [], [], [], [], [], [], []],
    365: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 178 (N)", [], False, [], [], [], [], [], [], [], []],
    366: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 179 (E)", [], False, [], [], [], [], [], [], [], []],
    367: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 179 (W)", [], False, [], [], [], [], [], [], [], []],
    368: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 180", [], False, [], [], [], [], [], [], [], []],
    369: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 181 (N)", [], False, [], [], [], [], [], [], [], []],
    370: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 181 (center)", [], False, [], [], [], [], [], [], [], []],
    371: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 181 (S)", [], False, [], [], [], [], [], [], [], []],
    372: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 182", [], False, [], [], [], [], [], [], [], []],
    373: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 183 (S)", [], False, [], [], [], [], [], [], [], []],
    374: [False, [373], 2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 183 (NW)", [], False, [], [], [], [], [], [], [], []],
    375: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 183 (NE)", [], False, [], [], [], [], [], [], [], []],
    376: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 184 (S)", [], False, [], [], [], [], [], [], [], []],
    377: [False, [376], 2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 184 (N)", [], False, [], [], [], [], [], [], [], []],
    378: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 185", [], False, [], [], [], [], [], [], [], []],
    379: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 186 (main)", [], False, [], [], [], [], [], [], [], []],
    380: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 186 (NE)", [], False, [], [], [], [], [], [], [], []],
    381: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 187 (main)", [], False, [], [], [], [], [], [], [], []],
    382: [False, [381], 2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 187 (chest)", [], False, [], [], [], [], [], [], [], []],
    383: [False, [381], 2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 187 (Dark Space)", [], False, [], [], [], [], [], [], [], []],
    384: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 188 (N bright)", [], False, [], [], [], [], [], [], [], []],
    385: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 188 (S bright)", [], False, [], [], [], [], [], [], [], []],
    386: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 189 (floor S)", [], False, [], [], [], [], [], [], [], []],
    387: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 189 (floor N)", [], False, [], [], [], [], [], [], [], []],
    388: [False, [386], 2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 189 (platform)", [], False, [], [], [], [], [], [], [], []],
    389: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 190 (E)", [], False, [], [], [], [], [], [], [], []],
    390: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 190 (W)", [], False, [], [], [], [], [], [], [], []],
    391: [False, [],    2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 191", [], False, [], [], [], [], [], [], [], []],
    392: [False, [384], 2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 188 (N)", [], False, [], [], [], [], [], [], [], []],
    393: [False, [385], 2, [4,19,0,b"\x00"], 0, "Ankor Wat: Map 188 (S)", [], False, [], [], [], [], [], [], [], []],

    # Dao
    400: [False, [1,14], 1, [5,20,0,b"\x00"], 0, "Dao: Main Area", [], False, [], [], [], [], [], [], [], []],
    401: [False, [],     2, [5,20,0,b"\x00"], 0, "Dao: NW House", [], False, [], [], [], [], [], [], [], []],
    402: [False, [],     2, [5,20,0,b"\x00"], 0, "Dao: Neil's House", [], False, [], [], [], [], [], [], [], []],
    403: [False, [],     2, [5,20,0,b"\x00"], 0, "Dao: Snake Game", [], False, [], [], [], [], [], [], [], []],
    404: [False, [],     2, [5,20,0,b"\x00"], 0, "Dao: SW House", [], False, [], [], [], [], [], [], [], []],
    405: [False, [],     2, [5,20,0,b"\x00"], 0, "Dao: S House", [], False, [], [], [], [], [], [], [], []],
    406: [False, [],     2, [5,20,0,b"\x00"], 0, "Dao: SE House", [], False, [], [], [], [], [], [], [], []],

    # Pyramid
    410: [False, [14],      2, [5,21,0,b"\x00"], 0, "Pyramid: Entrance (main)", [], False, [], [], [], [], [], [], [], []],
    411: [False, [410],     2, [5,21,0,b"\x00"], 0, "Pyramid: Entrance (behind orbs)", [], False, [], [], [], [], [], [], [], []],
    412: [False, [413],     2, [5,21,0,b"\x00"], 0, "Pyramid: Entrance (hidden platform)", [], False, [], [], [], [], [], [], [], []],
    413: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Entrance (bottom)", [], False, [], [], [], [], [], [], [], []],
    414: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Entrance (boss entrance)", [], False, [], [], [], [], [], [], [], []],
    415: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Hieroglyph room", [30, 31, 32, 33, 34, 35, 38], False, [], [], [], [], [], [], [], []],
    416: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Map 206 (E)", [], False, [], [], [], [], [], [], [], []],
    417: [False, [416],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 206 (W)", [], False, [], [], [], [], [], [], [], []],
    418: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Map 207 (NE)", [], False, [], [], [], [], [], [], [], []],
    419: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 207 (SW)", [], False, [], [], [], [], [], [], [], []],
    420: [False, [421],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 208 (N)", [], False, [], [], [], [], [], [], [], []],
    421: [False, [420],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 208 (S)", [], False, [], [], [], [], [], [], [], []],
    422: [False, [423],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 209 (W)", [], False, [], [], [], [], [], [], [], []],
    423: [False, [422,411], 2, [5,21,0,b"\x00"], 0, "Pyramid: Map 209 (E)", [], False, [], [], [], [], [], [], [], []],
    424: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Map 210", [], False, [], [], [], [], [], [], [], []],
    425: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 211", [], False, [], [], [], [], [], [], [], []],
    426: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Map 212 (N)", [], False, [], [], [], [], [], [], [], []],
    427: [False, [426],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 212 (center)", [], False, [], [], [], [], [], [], [], []],
    428: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 212 (SE)", [], False, [], [], [], [], [], [], [], []],
    429: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Map 212 (SW)", [], False, [], [], [], [], [], [], [], []],
    430: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 213", [], False, [], [], [], [], [], [], [], []],
    431: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Map 214 (NW)", [], False, [], [], [], [], [], [], [], []],
    432: [False, [431],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 214 (NE)", [], False, [], [], [], [], [], [], [], []],
    433: [False, [431,434], 2, [5,21,0,b"\x00"], 0, "Pyramid: Map 214 (SE)", [], False, [], [], [], [], [], [], [], []],
    434: [False, [433],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 214 (SW)", [], False, [], [], [], [], [], [], [], []],
    435: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 215 (main)", [], False, [], [], [], [], [], [], [], []],
    436: [False, [437],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 216 (N)", [], False, [], [], [], [], [], [], [], []],
    437: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 216 (S)", [], False, [], [], [], [], [], [], [], []],
    438: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Map 217 (W)", [], False, [], [], [], [], [], [], [], []],
    439: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Map 217 (E)", [], False, [], [], [], [], [], [], [], []],
    440: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Map 219 (W)", [], False, [], [], [], [], [], [], [], []],
    441: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 219 (E)", [], False, [], [], [], [], [], [], [], []],
    442: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Hieroglyph 1", [], False, [], [], [], [], [], [], [], []],
    443: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Hieroglyph 2", [], False, [], [], [], [], [], [], [], []],
    444: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Hieroglyph 3", [], False, [], [], [], [], [], [], [], []],
    445: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Hieroglyph 4", [], False, [], [], [], [], [], [], [], []],
    446: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Hieroglyph 5", [], False, [], [], [], [], [], [], [], []],
    447: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Hieroglyph 6", [], False, [], [], [], [], [], [], [], []],
    448: [False, [],        2, [5,21,0,b"\x00"], 0, "Pyramid: Boss Room", [], True, [], [], [], [], [], [], [], []],
    449: [False, [415,517], 0, [5,21,0,b"\x00"], 0, "Pyramid: Hieroglyphs Placed", [], False, [], [], [], [], [], [], [], []],
    450: [False, [411],     2, [5,21,0,b"\x00"], 0, "Pyramid: Map 215 (past Killer 6)", [], False, [], [], [], [], [], [], [], []],

    # Babel
    460: [False, [],       2, [6,22,0,b"\x00"], 0, "Babel: Foyer", [], False, [], [], [], [], [], [], [], []],
    461: [False, [],       2, [6,22,0,b"\x00"], 0, "Babel: Map 223 (bottom)", [], False, [], [], [], [], [], [], [], []],
    462: [False, [461],    2, [6,22,0,b"\x00"], 0, "Babel: Map 223 (top)", [], False, [], [], [], [], [], [], [], []],
    463: [False, [518,519],2, [6,22,0,b"\x00"], 0, "Babel: Map 224 (bottom)", [], False, [], [], [], [], [], [], [], []],
    464: [False, [520,521],2, [6,22,0,b"\x00"], 0, "Babel: Map 224 (top)", [], False, [], [], [], [], [], [], [], []],
    465: [False, [466],    2, [6,22,0,b"\x00"], 0, "Babel: Map 225 (SW)", [], False, [], [], [], [], [], [], [], []],
    466: [False, [],       2, [6,22,0,b"\x00"], 0, "Babel: Map 225 (NW)", [], False, [], [], [], [], [], [], [], []],
    467: [False, [468],    2, [6,22,0,b"\x00"], 0, "Babel: Map 225 (SE)", [], False, [], [], [], [], [], [], [], []],
    468: [False, [],       2, [6,22,0,b"\x00"], 0, "Babel: Map 225 (NE)", [], False, [], [], [], [], [], [], [], []],
    469: [False, [470],    2, [6,22,0,b"\x00"], 0, "Babel: Map 226 (bottom)", [], False, [], [], [], [], [], [], [], []],
    470: [False, [],       2, [6,22,0,b"\x00"], 0, "Babel: Map 226 (top)", [], False, [], [], [], [], [], [], [], []],
    471: [False, [522],    2, [6,22,0,b"\x00"], 0, "Babel: Map 227 (bottom)", [], False, [], [], [], [], [], [], [], []],
    472: [False, [],       2, [6,22,0,b"\x00"], 0, "Babel: Map 227 (top)", [], False, [], [], [], [], [], [], [], []],
    473: [False, [],       2, [6,22,0,b"\x00"], 0, "Babel: Olman's Room", [], False, [], [], [], [], [], [], [], []],
    474: [False, [],       0, [6,22,0,b"\x00"], 0, "Babel: Castoth", [], False, [], [], [], [], [], [], [], []],
    475: [False, [],       0, [6,22,0,b"\x00"], 0, "Babel: Viper", [], False, [], [], [], [], [], [], [], []],
    476: [False, [],       0, [6,22,0,b"\x00"], 0, "Babel: Vampires", [], False, [], [], [], [], [], [], [], []],
    477: [False, [],       0, [6,22,0,b"\x00"], 0, "Babel: Sand Fanger", [], False, [], [], [], [], [], [], [], []],
    478: [False, [],       0, [6,22,0,b"\x00"], 0, "Babel: Mummy Queen", [], False, [], [], [], [], [], [], [], []],
    479: [False, [473],    0, [6,22,0,b"\x00"], 0, "Babel: Statue Get", [], False, [], [], [], [], [], [], [], []],

    # Jeweler's Mansion
    480: [False, [],    2, [6,23,0,b"\x00"], 0, "Jeweler's Mansion: Main", [], False, [], [], [], [], [], [], [], []],
    481: [False, [],    2, [6,23,0,b"\x00"], 0, "Jeweler's Mansion: Behind Psycho Slider", [], False, [], [], [], [], [], [], [], []],
    482: [False, [523], 2, [6,23,0,b"\x00"], 0, "Jeweler's Mansion: Solid Arm", [], False, [], [], [], [], [], [], [], []],

    # Game End
    490: [False, [500], 0, [0,0,0,b"\x00"], 0, "Kara Released", [], False, [], [], [], [], [], [], [], []],
    491: [False,    [], 0, [0,0,0,b"\x00"], 0, "Firebird", [], False, [], [], [], [], [], [], [], []],
    492: [False, [491], 0, [0,0,0,b"\x00"], 0, "Dark Gaia/End Game", [], False, [], [], [], [], [], [], [], []],

    # Event Switches
    500: [False, [], 0, [0,0,0,b"\x00"], 0, "Kara                                ", [], False, [], [], [], [], [], [], [], []],
    501: [False, [], 0, [0,0,0,b"\x00"], 0, "Lilly                               ", [], False, [], [], [], [], [], [], [], []],
    502: [False, [], 0, [0,0,0,b"\x00"], 0, "Moon Tribe: Spirits Healed          ", [], False, [], [], [], [], [], [], [], []],
    503: [False, [], 0, [0,0,0,b"\x00"], 0, "Inca: Castoth defeated              ", [], False, [], [], [], [], [], [], [], []],
    504: [False, [], 0, [0,0,0,b"\x00"], 0, "Freejia: Found Laborer              ", [], False, [], [], [], [], [], [], [], []],
    505: [False, [], 0, [0,0,0,b"\x00"], 0, "Neil's Memory Restored              ", [], False, [], [], [], [], [], [], [], []],
    506: [False, [], 0, [0,0,0,b"\x00"], 0, "Sky Garden: Map 82 NW Switch        ", [], False, [], [], [], [], [], [], [], []],
    507: [False, [], 0, [0,0,0,b"\x00"], 0, "Sky Garden: Map 82 NE Switch        ", [], False, [], [], [], [], [], [], [], []],
    508: [False, [], 0, [0,0,0,b"\x00"], 0, "Sky Garden: Map 82 SE Switch        ", [], False, [], [], [], [], [], [], [], []],
    509: [False, [], 0, [0,0,0,b"\x00"], 0, "Sky Garden: Map 84 Switch           ", [], False, [], [], [], [], [], [], [], []],
    510: [False, [], 0, [0,0,0,b"\x00"], 0, "Seaside: Fountain Purified          ", [], False, [], [], [], [], [], [], [], []],
    511: [False, [], 0, [0,0,0,b"\x00"], 0, "Mu: Water Lowered 1                 ", [], False, [], [], [], [], [], [], [], []],
    512: [False, [], 0, [0,0,0,b"\x00"], 0, "Mu: Water Lowered 2                 ", [], False, [], [], [], [], [], [], [], []],
    513: [False, [], 0, [0,0,0,b"\x00"], 0, "Angel: Puzzle Complete              ", [], False, [], [], [], [], [], [], [], []],
    514: [False, [333,335], 0, [0,0,0,b"\x00"], 0, "Mt Kress: Drops used 1              ", [], False, [], [], [], [], [], [], [], []],
    515: [False, [339,340], 0, [0,0,0,b"\x00"], 0, "Mt Kress: Drops used 2              ", [], False, [], [], [], [], [], [], [], []],
    516: [False, [340,341], 0, [0,0,0,b"\x00"], 0, "Mt Kress: Drops used 3              ", [], False, [], [], [], [], [], [], [], []],
    517: [False, [], 0, [0,0,0,b"\x00"], 0, "Pyramid: Hieroglyphs placed         ", [], False, [], [], [], [], [], [], [], []],
    518: [False, [], 0, [0,0,0,b"\x00"], 0, "Babel: Castoth defeated             ", [], False, [], [], [], [], [], [], [], []],
    519: [False, [], 0, [0,0,0,b"\x00"], 0, "Babel: Viper defeated               ", [], False, [], [], [], [], [], [], [], []],
    520: [False, [], 0, [0,0,0,b"\x00"], 0, "Babel: Vampires defeated            ", [], False, [], [], [], [], [], [], [], []],
    521: [False, [], 0, [0,0,0,b"\x00"], 0, "Babel: Sand Fanger defeated         ", [], False, [], [], [], [], [], [], [], []],
    522: [False, [], 0, [0,0,0,b"\x00"], 0, "Babel: Mummy Queen defeated         ", [], False, [], [], [], [], [], [], [], []],
    523: [False, [], 0, [0,0,0,b"\x00"], 0, "Mansion: Solid Arm defeated         ", [], False, [], [], [], [], [], [], [], []],

    # Misc
    600: [False, [], 0, [0,0,0,b"\x00"], 0, "Freedan Access                      ", [], False, [], [], [], [], [], [], [], []],
    601: [False, [], 0, [0,0,0,b"\x00"], 0, "Glitches                            ", [], False, [], [], [], [], [], [], [], []],
    602: [False, [], 0, [0,0,0,b"\x00"], 0, "Early Firebird                      ", [], False, [], [], [], [], [], [], [], []],

    INACCESSIBLE: [False, [], 0, [0,0,0,b"\x00"], 0, "Inaccessible", [], False, [], [], [], [], [], [], [], []]

}


# Define logical paths in dynamic graph
# Format: { ID: [Status(-1=restricted,0=locked,1=unlocked,2=forced_open), StartRegion, DestRegion, NeedFreedan, [[item1, qty1],[item2,qty2]...]]}
logic = {
    # Jeweler Rewards
    0:  [0, 1, 2, False, [[1, gem[0]]]],  # Jeweler Reward 1
    1:  [0, 1, 2, False, [[1, gem[0] - 2], [41, 1]]],
    2:  [0, 1, 2, False, [[1, gem[0] - 3], [42, 1]]],
    3:  [0, 1, 2, False, [[1, gem[0] - 5], [41, 1], [42, 1]]],
    4:  [0, 2, 3, False, [[1, gem[1]]]],  # Jeweler Reward 2
    5:  [0, 2, 3, False, [[1, gem[1] - 2], [41, 1]]],
    6:  [0, 2, 3, False, [[1, gem[1] - 3], [42, 1]]],
    7:  [0, 2, 3, False, [[1, gem[1] - 5], [41, 1], [42, 1]]],
    8:  [0, 3, 4, False, [[1, gem[2]]]],  # Jeweler Reward 3
    9:  [0, 3, 4, False, [[1, gem[2] - 2], [41, 1]]],
    10: [0, 3, 4, False, [[1, gem[2] - 3], [42, 1]]],
    11: [0, 3, 4, False, [[1, gem[2] - 5], [41, 1], [42, 1]]],
    12: [0, 4, 5, False, [[1, gem[3]]]],  # Jeweler Reward 4
    13: [0, 4, 5, False, [[1, gem[3] - 2], [41, 1]]],
    14: [0, 4, 5, False, [[1, gem[3] - 3], [42, 1]]],
    15: [0, 4, 5, False, [[1, gem[3] - 5], [41, 1], [42, 1]]],
    16: [0, 5, 6, False, [[1, gem[4]]]],  # Jeweler Reward 5
    17: [0, 5, 6, False, [[1, gem[4] - 2], [41, 1]]],
    18: [0, 5, 6, False, [[1, gem[4] - 3], [42, 1]]],
    19: [0, 5, 6, False, [[1, gem[4] - 5], [41, 1], [42, 1]]],
    20: [0, 6, 7, False, [[1, gem[5]]]],  # Jeweler Reward 6
    21: [0, 6, 7, False, [[1, gem[5] - 2], [41, 1]]],
    22: [0, 6, 7, False, [[1, gem[5] - 3], [42, 1]]],
    23: [0, 6, 7, False, [[1, gem[5] - 5], [41, 1], [42, 1]]],
    24: [0, 7, 8, False, [[1, gem[6]]]],  # Jeweler Reward 7 (Mansion)
    25: [0, 7, 8, False, [[1, gem[6] - 2], [41, 1]]],
    26: [0, 7, 8, False, [[1, gem[6] - 3], [42, 1]]],
    27: [0, 7, 8, False, [[1, gem[6] - 5], [41, 1], [42, 1]]],

    # Inter-Continental Travel
    30: [0, 28,   15, False, [[37, 1]]],   # South Cape: Erik w/ Lola's Letter
    31: [0, 102,  15, False, [[37, 1]]],   # Coast: Turbo w/ Lola's Letter
    32: [0, 280,  15, False, [[37, 1]]],   # Watermia: Bridgeman w/ Lola's Letter
    33: [0, 160, 161, False, [[13, 1]]],   # Neil's: Neil w/ Memory Melody
    34: [0, 314,  17, False, [[505, 1]]],  # Euro: Neil w/ Memory restored
    35: [0, 402,  17, False, [[505, 1]]],  # Dao: Neil w/ Memory restored
    36: [0,  60,  64, False, [[25, 1]]],   # Moon Tribe healed w/ Teapot
    37: [0, 170,  16, False, [[502, 1]]],  # Sky Garden: Spirits w/ spirits healed
    38: [0, 280, 288, False, [[24, 1]]],   # Watermia: Stablemaster w/ Will
    39: [0, 310, 311, False, [[24, 1]]],   # Euro: Stablemaster w/ Will
    40: [0, 350, 351, False, [[10, 1]]],   # Natives': Child Guide w/ Large Roast

    # Edward's / Tunnel
    60: [0, 32, 33, False, [[2, 1]]],    # Escape cell w/Prison Key
    61: [0, 33, 32, False, [[2, 1]]],    # Enter cell w/Prison Key
    62: [0, 45, 46, False, [[501, 1]]],  # Progression w/ Lilly
    63: [0, 47, 48,  True, []],          # Activate Bridge w/ Freedan

    # Itory
    70: [0, 50, 51, False, [[9, 1]]],    # Town appears w/ Lola's Melody
    71: [0, 55, 59, False, [[23, 1]]],   # Get Lilly w/ Necklace
    72: [0, 56, 57, False, [[61, 1]]],   # Cave w/ Psycho Dash
    73: [0, 56, 57, False, [[62, 1]]],   # Cave w/ Psycho Slide
    74: [0, 56, 57, False, [[63, 1]]],   # Cave w/ Spin Dash

    # Moon Tribe
    80: [0, 61, 62, False, [[61, 1]]],   # Cave challenge w/ Psycho Dash
    81: [0, 61, 62, False, [[62, 1]]],   # Cave challenge w/ Psycho Slide
    82: [0, 61, 62, False, [[63, 1]]],   # Cave challenge w/ Spin Dash

    # Inca / Gold Ship / Freejia
    89:  [0,  72,  99, False, [[601, 1]]],        # Map 29 progression w/ glitches
    90:  [0,  77,  78, False, [[3, 1], [4, 1]]],  # Map 30 progression w/ Inca Statues
    91:  [0,  80,  81, False, [[61, 1]]],         # Map 32 progression w/ Psycho Dash
    92:  [0,  80,  81, False, [[62, 1]]],         # Map 32 progression w/ Psycho Slider
    93:  [0,  80,  81, False, [[63, 1]]],         # Map 32 progression w/ Spin Dash
    94:  [0,  85,  86,  True, []],                # Map 35 progression w/ Freedan
    95:  [0,  87,  88, False, [[8, 1]]],          # Map 36 progression w/ Wind Melody
    96:  [0,  89,  90, False, [[7, 1]]],          # Map 37 progression w/ Diamond Block
    97:  [0,  91,  92, False, [[61, 1]]],         # Map 38 progression w/ Psycho Dash
    98:  [0,  91,  92, False, [[62, 1]]],         # Map 38 progression w/ Psycho Slider
    99:  [0,  91,  92, False, [[63, 1]]],         # Map 38 progression w/ Spin Dash
    #100: [0, 100, 104, False, [[100, 1]]],        # Gold Ship progression w/ Statue 1
    101: [0, 110, 115, False, [[504, 1]]],        # Freejia: Slaver item w/ Laborer Found

    # Diamond Mine
    110: [0, 131, 132, False, [[61, 1]]],            # Map 61 false wall w/ Psycho Dash
    111: [0, 131, 132, False, [[62, 1]]],            # Map 61 false wall w/ Psycho Slider
    112: [0, 131, 132, False, [[63, 1]]],            # Map 61 false wall w/ Spin Dash
    113: [0, 134, 135, False, [[15, 1]]],            # Map 63 progression w/ Elevator Key
    114: [0, 136, 137, False, [[61, 1]]],            # Map 64 trapped laborer w/ Psycho Dash
    115: [0, 136, 137, False, [[62, 1]]],            # Map 64 trapped laborer w/ Psycho Slider
    116: [0, 136, 137, False, [[63, 1]]],            # Map 64 trapped laborer w/ Spin Dash
    117: [0, 138, 139, False, [[63, 1]]],            # Map 65 progression w/ Spin Dash
    118: [0, 138, 139,  True, [[64, 1]]],            # Map 65 progression w/ Dark Friar
    119: [0, 146, 147, False, [[11, 1], [12, 1]]],   # Map 68 progression w/ mine keys

    # Sky Garden
    130: [0, 170, 171, False, [[14, 4]]],            # Boss access w/ Crystal Balls
    131: [0, 177, 178,  True, [[64, 1]]],             # Map 79 progression w/ Dark Friar
    132: [0, 177, 178,  True, [[67, 1]]],             # Map 79 progression w/ Firebird
    133: [0, 168, 182, False, [[506, 1]]],           # Map 81 progression w/ switch 1
    134: [0, 182, 183, False, [[507, 1]]],           # Map 81 progression w/ switch 2
    135: [0, 182, 184, False, [[61, 1]]],            # Map 81 progression w/ Psycho Dash
    136: [0, 182, 184, False, [[62, 1]]],            # Map 81 progression w/ Psycho Dash
    137: [0, 182, 184, False, [[63, 1]]],            # Map 81 progression w/ Psycho Dash
    138: [0, 184, 185, False, [[508, 1], [61, 1]]],  # Map 81 progression w/ switch 3 & Psycho Dash
    139: [0, 184, 185, False, [[508, 1], [62, 1]]],  # Map 81 progression w/ switch 3 & Psycho Slider
    140: [0, 184, 185, False, [[508, 1], [63, 1]]],  # Map 81 progression w/ switch 3 & Spin Dash
    141: [0, 181, 182, False, [[63, 1]]],            # Map 81 progression w/ Spin Dash
    142: [0, 181, 184, False, [[63, 1]]],            # Map 81 progression w/ Spin Dash
    143: [0, 182, 185, False, [[63, 1]]],            # Map 81 progression w/ Spin Dash
    144: [0, 188, 189,  True, []],                    # Map 82 progression w/ Freedan
    145: [0, 188, 189, False, [[601, 1]]],           # Map 82 progression w/ Glitches
    146: [0, 192, 190, False, [[63, 1]]],            # Map 83 progression w/ Spin Dash
    147: [0, 195, 199,  True, [[64, 1]]],            # Map 84 progression w/ Dark Friar
    148: [0, 195, 199,  True, [[67, 1]]],            # Map 84 progression w/ Firebird
    149: [0, 195, 199,  True, [[65, 1]]],            # Map 84 progression w/ Aura Barrier
    150: [0, 197, 199,  True, [[64, 1]]],            # Map 84 progression w/ Dark Friar
    151: [0, 197, 199,  True, [[67, 1]]],            # Map 84 progression w/ Firebird
    152: [0, 170,  16, False, [[502, 1]]],           # Moon Tribe passage w/ spirits healed

    # Seaside Palace
    160: [0, 205, 208, False, [[501, 1]]],   # Coffin access w/ Lilly
    161: [0, 209, 510, False, [[17, 1]]],    # Purify fountain w/stone
    162: [0, 200, 206, False, [[510, 1]]],   # Buffy access w/ purified fountain
    163: [0, 200, 201, False, [[16, 1]]],    # Seaside to Mu w/ Mu key
    164: [0, 210, 211, False, [[16, 1]]],    # Mu to Seaside w/ Mu key

    # Mu
    170: [0, 212, 245, False, [[62, 1]]],                       # Map 95 progression w/ Psycho Slider
    171: [0, 212, 213, False, [[511, 1]]],                      # Map 95 progression w/ water lowered 1
    172: [0, 213, 215, False, [[512, 1]]],                      # Map 95 progression w/ water lowered 2
    173: [0, 214, 216, False, [[512, 1]]],                      # Map 95 progression w/ water lowered 2
    174: [0, 217, 218, False, [[511, 1]]],                      # Map 96 progression w/ water lowered 1
    175: [0, 222, 221,  True, [[511, 1], [64, 1]]],             # Map 97 progression w/ water lowered 1 & Friar
    176: [0, 222, 221,  True, [[511, 1], [67, 1]]],             # Map 97 progression w/ water lowered 1 & Firebird
    177: [0, 222, 221, False, [[511, 1], [601, 1]]],            # Map 97 progression w/ water lowered 1 & glitches
    178: [0, 226, 227, False, [[511, 1]]],                      # Map 98 progression w/ water lowered 1
    179: [0, 227, 229, False, [[512, 1]]],                      # Map 98 progression w/ water lowered 2
    180: [0, 228, 230, False, [[512, 1]]],                      # Map 98 progression w/ water lowered 2
    181: [0, 229, 230, False, [[62, 1]]],                       # Map 98 progression w/ Psycho Slider
    182: [0, 230, 229, False, [[62, 1]]],                       # Map 98 progression w/ Psycho Slider
    183: [0, 226, 246, False, [[62, 1]]],                       # Map 98 progression w/ Psycho Slider
    184: [0, 237, 238, False, [[62, 1]]],                       # Map 101 progression w/ Psycho Slider
    185: [0, 240, 241, False, [[19, 2]]],                       # Map 102 progression w/ Rama Statues
    186: [0, 231, 247, False, [[18, 1]]],                       # Water lowered 1 w/ Hope Statue
    187: [0, 232, 248, False, [[18, 2]]],                       # Water lowered 2 w/ Hope Statues

    # Angel Dungeon
    210: [0, 263, 264, False, [[62, 1]]],    # Map 112 progression w/ Psycho Slider
    211: [0, 265, 275, False, [[62, 1]]],    # Map 112 backwards progression w/ Psycho Slider
    212: [0, 267, 268, False, [[62, 1]]],    # Map 114 progression w/ Psycho Slider
    213: [0, 277, 276, False, [[62, 1]]],    # Map 114 backwards progression w/ Psycho Slider
    214: [0, 272, 273, False, [[513, 1]]],   # Ishtar's chest w/ puzzle complete

    # Great Wall
    220: [0, 294, 295, False, [[601, 1]]],           # Map 133 progression w/ glitches
    221: [0, 296, 295, False, [[63, 1]]],            # Map 133 progression w/ Spin Dash
    222: [0, 296, 295,  True, []],                   # Map 133 progression w/ Freedan
    223: [0, 298, 299,  True, [[64, 1]]],            # Map 135 progression w/ Friar
    224: [0, 298, 299,  True, [[67, 1]]],            # Map 135 progression w/ Firebird
    225: [0, 299, 298, False, [[64, 1], [54, 2]]],   # Map 135 progression w/ Friar III
    227: [0, 300, 301, False, [[63, 1]]],            # Map 136 progression w/ Spin Dash
    228: [0, 295, 294, False, [[63, 1]]],            # Map 133 progression w/ Spin Dash

    # Euro
    230: [0, 314, 315, False, [[40, 1]]],    # Ann item w/ Apple

    # Mt. Temple
    240: [0, 331, 332, False, [[63, 1]]],   # Map 161 progression w/ Spin Dash
    241: [0, 332, 331, False, [[63, 1]]],   # Map 161 backwards progression w/ Spin Dash
    242: [0, 333, 514, False, [[26, 1]]],   # Map 162 progression w/ Mushroom drops 1
    243: [0, 335, 514, False, [[26, 1]]],   # Map 162 progression w/ Mushroom drops 1  -- IS THIS TRUE?
    244: [0, 339, 515, False, [[26, 2]]],   # Map 162 progression w/ Mushroom drops 2
    245: [0, 340, 515, False, [[26, 2]]],   # Map 162 progression w/ Mushroom drops 2  -- IS THIS TRUE?
    246: [0, 340, 516, False, [[26, 3]]],   # Map 162 progression w/ Mushroom drops 3
    247: [0, 341, 516, False, [[26, 3]]],   # Map 162 progression w/ Mushroom drops 3  -- IS THIS TRUE?

    # Natives'
    250: [0, 353, 354, False, [[29, 1]]],    # Statues awake w/ Gorgon Flower

    # Ankor Wat
    260: [-1, 361, 362,  True, [[64, 1]]],                     # Map 177 progression w/ Friar
    261: [0, 363, 364, False, [[63, 1]]],                      # Map 178 progression w/ Spin Dash
    262: [0, 364, 365, False, [[62, 1]]],                      # Map 178 progression w/ Psycho Slider
    263: [0, 365, 364, False, [[62, 1]]],                      # Map 178 progression w/ Psycho Slider
    264: [0, 367, 366, False, [[63, 1]]],                      # Map 179 progression w/ Spin Dash
    265: [0, 369, 370, False, [[62, 1]]],                      # Map 181 progression w/ Psycho Slider
    266: [0, 370, 371, False, [[63, 1]]],                      # Map 181 progression w/ Spin Dash
    267: [0, 373, 374,  True, [[66, 1]]],                      # Map 183 progression w/ Earthquaker
    268: [0, 373, 374,  True, [[64, 1], [54, 2]]],             # Map 183 progression w/ upgraded Friar
    269: [0, 373, 374,  True, [[64, 1], [601, 1]]],            # Map 183 progression w/ Friar and glitches
    270: [0, 373, 374,  True, [[67, 1]]],                      # Map 183 progression w/ Firebird       -- IS THIS TRUE?
    271: [0, 376, 377,  True, [[64, 1]]],                      # Map 184 progression w/ Friar
    272: [0, 376, 377,  True, [[36, 1]]],                      # Map 184 progression w/ Shadow
    273: [0, 384, 392, False, [[28, 1]]],                      # Map 188 progression w/ Black Glasses
    274: [0, 385, 393, False, [[28, 1]]],                      # Map 188 progression w/ Black Glasses
    275: [0, 384, 392, False, [[601, 1]]],                     # Map 188 progression w/ glitches
    276: [0, 385, 393, False, [[601, 1]]],                     # Map 188 progression w/ glitches
    277: [0, 392, 393, False, [[62, 1]]],                      # Map 188 progression w/ Slider
    278: [0, 393, 392, False, [[62, 1]]],                      # Map 188 progression w/ Slider
    279: [0, 386, 387, False, [[62, 1]]],                      # Map 188 progression w/ Psycho Slider
    280: [0, 387, 386, False, [[62, 1]]],                      # Map 188 progression w/ Psycho Slider

    # Pyramid
    290: [0, 410, 411, False, [[62, 1]]],             # Map 204 progression w/ Slider
    291: [0, 410, 411, False, [[63, 1]]],             # Map 204 progression w/ Spin
    292: [0, 410, 411, False, [[601, 1]]],            # Map 204 progression w/ glitches
    293: [0, 411, 412, False, [[36, 1]]],             # Map 204 progression w/ Aura
    294: [0, 411, 413, False, [[36, 1]]],             # Map 204 progression w/ Aura
    295: [0, 415, 449, False, [[30, 1], [31, 1], [32, 1], [33, 1], [34, 1], [35, 1], [38, 1]]],
                                                      # Boss door open w/ Hieroglyphs
    296: [0, 416, 417, False, [[63, 1]]],             # Map 206 progression w/ Spin Dash
    297: [0, 417, 416, False, [[63, 1]]],             # Map 206 progression w/ Spin Dash
    298: [0, 418, 419, False, [[63, 1]]],             # Map 206 progression w/ Spin Dash
    299: [0, 419, 418, False, [[63, 1]]],             # Map 206 progression w/ Spin Dash
    300: [0, 426, 427,  True, [[36, 1]]],             # Map 212 progression w/ Aura
    301: [0, 426, 427,  True, [[66, 1]]],             # Map 212 progression w/ Earthquaker
    302: [0, 427, 428,  True, [[36, 1]]],             # Map 212 progression w/ Aura
    303: [0, 427, 429,  True, [[36, 1]]],             # Map 212 progression w/ Aura
    304: [0, 427, 429,  True, [[66, 1]]],             # Map 212 progression w/ Earthquaker
    305: [0, 431, 432, False, [[63, 1]]],             # Map 214 progression w/ Spin Dash
    306: [0, 431, 434,  True, [[36, 1]]],             # Map 214 progression w/ Aura
    307: [0, 431, 433,  True, [[64, 1]]],             # Map 214 progression w/ Friar
    308: [0, 438, 439, False, [[63, 1]]],             # Map 217 progression w/ Spin Dash
    309: [0, 439, 438, False, [[63, 1]]],             # Map 217 progression w/ Spin Dash
    310: [0, 440, 441, False, [[63, 1]]],             # Map 219 progression w/ Spin Dash
    311: [0, 441, 440, False, [[63, 1]]],             # Map 219 progression w/ Spin Dash
    312: [0, 435, 450, False, [[6, 6], [50, 2], [51, 1], [52, 1]]],
                                                      # Killer 6 w/ herbs and upgrades
    313: [0, 435, 450,  True, [[64, 1], [54, 1]]],
                                                      # Killer 6 w/ Friar II
    314: [0, 411, 414, False, [[517, 1]]],            # Pyramid to boss w/hieroglyphs placed

    # Babel / Mansion
    320: [0, 461, 462, False, [[36, 1], [39, 1]]],    # Map 219 progression w/ Aura and Ring
    321: [0, 473, 479, False, [[522, 1]]],            # Olman statue w/ Mummy Queen 2
    322: [0, 473, 479, False, [[523, 1]]],            # Olman statue w/ Solid Arm
    323: [0, 480, 481, False, [[62, 1]]],             # Mansion progression w/ Slider

    # Endgame / Misc
    400: [-1, 49, 490, False, [[20, 1]]],                       # Rescue Kara from Edward's w/ Magic Dust
    401: [-1, 150, 490, False, [[20, 1]]],                      # Rescue Kara from Mine w/ Magic Dust
    402: [-1, 270, 490, False, [[20, 1]]],                      # Rescue Kara from Angel w/ Magic Dust
    403: [-1, 345, 490, False, [[20, 1]]],                      # Rescue Kara from Mt. Temple w/ Magic Dust
    404: [-1, 391, 490, False, [[20, 1]]],                      # Rescue Kara from Ankor Wat w/ Magic Dust
    405: [0, 490, 491, False, [[36, 1], [39, 1], [602, 1]]],    # Early Firebird w/ Kara, Aura and Ring
    406: [0, 490, 492, False, [[36, 1], [100, 0], [101, 0], [102, 0], [103, 0], [104, 0], [105, 0]]],
                                                                # Beat Game w/Mystic Statues and Aura
    407: [0, 490, 492, False, [[36, 1], [106, statues_required]]]              # Beat Game w/Mystic Statues and Aura (player choice variant)

}
