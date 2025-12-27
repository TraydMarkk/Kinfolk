"""
Werewolf: The Apocalypse 20th Anniversary Edition Character Data
Contains all game data for attributes, abilities, backgrounds, gifts, forms, etc.
"""

# ============================================================================
# ATTRIBUTES
# ============================================================================

ATTRIBUTES = {
    "Physical": ["Strength", "Dexterity", "Stamina"],
    "Social": ["Charisma", "Manipulation", "Appearance"],
    "Mental": ["Perception", "Intelligence", "Wits"]
}

# ============================================================================
# ABILITIES
# ============================================================================

PRIMARY_ABILITIES = {
    "Talents": [
        "Alertness", "Athletics", "Brawl", "Empathy", "Expression",
        "Intimidation", "Leadership", "Primal-Urge", "Streetwise", "Subterfuge"
    ],
    "Skills": [
        "Animal Ken", "Crafts", "Drive", "Etiquette", "Firearms",
        "Larceny", "Melee", "Performance", "Stealth", "Survival", "Technology"
    ],
    "Knowledges": [
        "Academics", "Computer", "Enigmas", "Investigation", "Law",
        "Medicine", "Occult", "Politics", "Rituals", "Science"
    ]
}

SECONDARY_ABILITIES = {
    "Talents": [
        "Hobby Talent"
    ],
    "Skills": [
        "Archery", "Commerce", "Riding"
    ],
    "Knowledges": [
        "Area Knowledge", "Cosmology", "Culture", "Linguistics", "Lore"
    ]
}

# ============================================================================
# BREEDS
# ============================================================================

BREEDS = {
    "Homid": {
        "description": "Born to human or homid Garou mothers. Grew up among humans.",
        "initial_gnosis": 1,
        "beginning_gifts": ["Apecraft's Blessings", "City Running", "Master of Fire", "Persuasion", "Smell of Man"],
        "restrictions": []
    },
    "Metis": {
        "description": "Born to two werewolves who broke the Litany. Deformed and sterile.",
        "initial_gnosis": 3,
        "beginning_gifts": ["Create Element", "Primal Anger", "Rat Head", "Sense Wyrm", "Shed"],
        "restrictions": [],
        "deformities": [
            "Albino", "Blind", "Fits of Madness", "Hairless", "Horns",
            "Hunchback", "No Sense of Smell", "No Tail", "Seizures",
            "Tough Hide", "Wasting Disease", "Weak Immune System", "Withered Limb"
        ]
    },
    "Lupus": {
        "description": "Born a wolf. Closest to nature and the spirit world.",
        "initial_gnosis": 5,
        "beginning_gifts": ["Hare's Leap", "Heightened Senses", "Predator's Arsenal", "Prey Mind", "Sense Prey"],
        "restrictions": {
            "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
            "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
        }
    }
}

# ============================================================================
# AUSPICES
# ============================================================================

AUSPICES = {
    "Ragabash": {
        "description": "New Moon - Questioners and tricksters who stalk the Wyrm with guile and cunning.",
        "initial_rage": 1,
        "beginning_renown": {"total": 3, "distribution": "any combination"},
        "beginning_gifts": ["Blur of the Milky Eye", "Infectious Laughter", "Liar's Face", "Open Seal", "Scent of Running Water"]
    },
    "Theurge": {
        "description": "Crescent Moon - Seers and shamans who clearly understand spirits and their ways.",
        "initial_rage": 2,
        "beginning_renown": {"total": 3, "distribution": "Wisdom"},
        "beginning_gifts": ["Mother's Touch", "Sense Wyrm", "Spirit Snare", "Spirit Speech", "Umbral Tether"]
    },
    "Philodox": {
        "description": "Half Moon - Judges and lawmakers who balance the dual nature of man and wolf.",
        "initial_rage": 3,
        "beginning_renown": {"total": 3, "distribution": "Honor"},
        "beginning_gifts": ["Fangs of Judgment", "Persuasion", "Resist Pain", "Scent of the True Form", "Truth of Gaia"]
    },
    "Galliard": {
        "description": "Gibbous Moon - Lore-keepers and tale-singers who tell the deeds of Garou past to inspire the present.",
        "initial_rage": 4,
        "beginning_renown": {"total": 3, "distribution": "2 Glory, 1 Wisdom"},
        "beginning_gifts": ["Beast Speech", "Call of the Wyld", "Heightened Senses", "Mindspeak", "Perfect Recall"]
    },
    "Ahroun": {
        "description": "Full Moon - Warriors and protectors who bring destruction to the Wyrm wherever it dwells and breeds.",
        "initial_rage": 5,
        "beginning_renown": {"total": 3, "distribution": "2 Glory, 1 Honor"},
        "beginning_gifts": ["Falling Touch", "Inspiration", "Pack Tactics", "Razor Claws", "Spur Claws"]
    }
}

# ============================================================================
# TRIBES
# ============================================================================

TRIBES = {
    "Black Furies": {
        "description": "The living incarnation of a woman's anger. Daughters of Luna-as-Artemis.",
        "initial_willpower": 3,
        "beginning_gifts": ["Breath of the Wyld", "Man's Skin", "Heightened Senses", "Sense Wyrm", "Wyld Resurgence"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    },
    "Bone Gnawers": {
        "description": "Ragged and luckless, the most populous tribe. Survivors who play the game of survival.",
        "initial_willpower": 3,
        "beginning_gifts": ["Cooking", "Resist Toxin", "Smell of Man", "Urban Tracking", "Wall Running"],
        "restrictions": {"backgrounds": ["Ancestors", "Pure Breed"]},
        "discouraged": {"backgrounds": ["Resources"]}
    },
    "Children of Gaia": {
        "description": "Peacemakers and healers who seek to unite the Garou Nation and heal the world.",
        "initial_willpower": 4,
        "beginning_gifts": ["Calm", "Mother's Touch", "Persuasion", "Resist Pain", "Scent of the True Form"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    },
    "Fianna": {
        "description": "Celtic warriors and bards who celebrate life, honor, and the glory of battle.",
        "initial_willpower": 3,
        "beginning_gifts": ["Beast Speech", "Blarney", "Persuasion", "Resist Pain", "Song of Rage"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    },
    "Get of Fenris": {
        "description": "Fierce warriors of Germanic and Norse descent. Strength and honor above all.",
        "initial_willpower": 3,
        "beginning_gifts": ["Falling Touch", "Inspiration", "Razor Claws", "Resist Pain", "True Fear"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    },
    "Glass Walkers": {
        "description": "Urban werewolves who embrace technology and civilization to fight the Wyrm.",
        "initial_willpower": 3,
        "beginning_gifts": ["Control Simple Machine", "Cybersenses", "Persuasion", "Smell of Man", "Urban Tracking"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": ["Contacts"]}
    },
    "Red Talons": {
        "description": "Fierce lupus warriors who reject humanity and fight to preserve the wild.",
        "initial_willpower": 3,
        "beginning_gifts": ["Heightened Senses", "Prey Mind", "Sense Prey", "Shed", "True Fear"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    },
    "Shadow Lords": {
        "description": "Manipulative strategists who believe in winning at any cost through cunning and power.",
        "initial_willpower": 3,
        "beginning_gifts": ["Fatal Flaw", "Liar's Face", "Persuasion", "Scent of the True Form", "Staredown"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": ["Mentor"]}
    },
    "Silent Striders": {
        "description": "Wanderers and messengers who travel the world, never staying in one place long.",
        "initial_willpower": 3,
        "beginning_gifts": ["Hare's Leap", "Heightened Senses", "Open Seal", "Speed of Thought", "Wisdom of the Ancient"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": ["Allies", "Contacts"]}
    },
    "Silver Fangs": {
        "description": "Noble leaders and aristocrats who claim descent from the first werewolves.",
        "initial_willpower": 4,
        "beginning_gifts": ["Falling Touch", "Inspiration", "Lambent Flame", "Persuasion", "True Fear"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    },
    "Stargazers": {
        "description": "Ascetics who seek to master their own Rage and find inner peace through meditation.",
        "initial_willpower": 4,
        "beginning_gifts": ["Balance", "Calm", "Heightened Senses", "Resist Pain", "Wisdom of the Ancient"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    },
    "Uktena": {
        "description": "Mystics and keepers of secrets who guard ancient knowledge and forbidden lore.",
        "initial_willpower": 3,
        "beginning_gifts": ["Mother's Touch", "Sense Wyrm", "Spirit Speech", "Umbral Tether", "Wisdom of the Ancient"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    },
    "Wendigo": {
        "description": "Fierce warriors of Native American descent who protect their people and the wild.",
        "initial_willpower": 3,
        "beginning_gifts": ["Heightened Senses", "Prey Mind", "Resist Pain", "Sense Prey", "True Fear"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    },
    "Black Spiral Dancers": {
        "description": "The only werewolf tribe to have wholly turned to the Wyrm. Corrupted descendants of the White Howlers.",
        "initial_willpower": 3,
        "beginning_gifts": ["Bane Protector", "Resist Pain", "Resist Toxin", "Sense Wyrm", "Shroud"],
        "restrictions": {"backgrounds": []},
        "discouraged": {"backgrounds": []}
    }
}

# ============================================================================
# FORMS
# ============================================================================

FORMS = {
    "Homid": {
        "description": "The Human form - allows Garou to move through man's world more or less unseen.",
        "statistics_adjustment": {
            "Strength": 0, "Dexterity": 0, "Stamina": 0,
            "Charisma": 0, "Manipulation": 0, "Appearance": 0,
            "Perception": 0, "Intelligence": 0, "Wits": 0
        },
        "shift_difficulty": 6,
        "size": "5'-6½' tall, 100-250 lbs.",
        "special": "Metis and lupus Garou still possess their regenerative abilities and vulnerability to silver in this form."
    },
    "Glabro": {
        "description": "The Near-Human form - unusually tall, feral, muscular person.",
        "statistics_adjustment": {
            "Strength": 2, "Dexterity": 0, "Stamina": 2,
            "Charisma": 0, "Manipulation": -2, "Appearance": -1,
            "Perception": 0, "Intelligence": 0, "Wits": 0
        },
        "shift_difficulty": 7,
        "size": "5½'-7½' tall, 200-400 lbs.",
        "special": "Teeth and nails thicken and sharpen. Can speak, but not well."
    },
    "Crinos": {
        "description": "The War-Wolf form - living embodiment of Rage combining the most terrible elements of man and wolf.",
        "statistics_adjustment": {
            "Strength": 4, "Dexterity": 1, "Stamina": 3,
            "Charisma": 0, "Manipulation": 0, "Appearance": 0,
            "Perception": 0, "Intelligence": 0, "Wits": 0
        },
        "shift_difficulty": 6,
        "size": "8'-10' tall, 400-850 lbs.",
        "special": "Requires Willpower point to speak human words. Dice-pool penalties to Manipulation and Appearance do not affect spirits or other Garou."
    },
    "Hispo": {
        "description": "The Dire Wolf form - primal nightmare of ancient man, recalls the titanic dire wolves.",
        "statistics_adjustment": {
            "Strength": 3, "Dexterity": 2, "Stamina": 3,
            "Charisma": 0, "Manipulation": 0, "Appearance": 0,
            "Perception": 0, "Intelligence": 0, "Wits": 0
        },
        "shift_difficulty": 7,
        "size": "4'-6' at the shoulder, 350-800 lbs.",
        "special": "Reduces all Perception-based difficulties by one. Adds another die to the usual bite damage. Cannot speak (save a few words in the Garou tongue)."
    },
    "Lupus": {
        "description": "The Wolf form - to all appearances a large normal wolf.",
        "statistics_adjustment": {
            "Strength": 1, "Dexterity": 2, "Stamina": 2,
            "Charisma": 0, "Manipulation": 0, "Appearance": 0,
            "Perception": 0, "Intelligence": 0, "Wits": 0
        },
        "shift_difficulty": 6,
        "size": "3'-4' at the shoulder, 120-250 lbs.",
        "special": "Perception-based difficulties reduced by two. Can run at twice normal human speed. Can bite for aggravated damage (except lupus-breed inflict only lethal)."
    }
}

# ============================================================================
# GIFTS
# ============================================================================

# Breed Gifts
BREED_GIFTS = {
    "Homid": {
        1: [
            ("Apecraft's Blessings", "The werewolf can use any tool or object created by human hands with supernatural skill. The purpose is irrelevant—this Gift is about mastery over human creation. (W20 Core, p. 152)"),
            ("City Running", "The werewolf can scale buildings and navigate urban environments with ease, moving like a spider or monkey. (W20 Core, p. 152)"),
            ("Master of Fire", "The werewolf can control and manipulate fire, creating it, extinguishing it, or directing it. (W20 Core, p. 152)"),
            ("Persuasion", "The werewolf can convince others to see things from their perspective, making social interactions easier. (W20 Core, p. 153)"),
            ("Smell of Man", "The werewolf can blend into human society, appearing as a normal person and avoiding detection. (W20 Core, p. 153)")
        ],
        2: [
            ("Jam Technology", "The werewolf can cause technological devices to malfunction or stop working entirely. (W20 Core, p. 153)"),
            ("Mark of the Wolf", "The werewolf can mark others with the Curse, causing them to be feared by humans. (W20 Core, p. 154)"),
            ("Speech of the World", "The werewolf can speak and understand any human language. (W20 Core, p. 154)"),
            ("Staredown", "The werewolf can cause others to flee or freeze in fear with a mere glance. (W20 Core, p. 154)")
        ],
        3: [
            ("Calm the Savage Beast", "The werewolf can calm a frenzying Garou, helping them regain control. (W20 Core, p. 154)"),
            ("Cowing the Bullet", "The werewolf gains protection against crafted weapons, gaining additional soak dice. (W20 Core, p. 154)"),
            ("Disquiet", "The werewolf can cause depression and listlessness in others, preventing them from recovering Rage. (W20 Core, p. 154)"),
            ("Reshape Object", "The werewolf can transform once-living material into other objects instantly. (W20 Core, p. 154)")
        ],
        4: [
            ("Body Shift", "The werewolf can shift physical Attribute dots between Strength, Dexterity, and Stamina. (W20 Core, p. 154)"),
            ("Bury the Wolf", "The werewolf can appear completely human, nullifying the Curse and locking them in homid form. (W20 Core, p. 154)"),
            ("Cocoon", "The werewolf can wrap themselves in a protective cocoon, becoming nearly impervious to harm. (W20 Core, p. 155)"),
            ("Spirit Ward", "The werewolf can protect themselves from spirits with a warding rite. (W20 Core, p. 155)")
        ],
        5: [
            ("Assimilation", "The werewolf can blend into any culture, speaking the language and mimicking behaviors. (W20 Core, p. 155)"),
            ("Beyond Human", "The werewolf radiates an aura of importance and can boost Social Attributes with Rage or Gnosis. (W20 Core, p. 155)"),
            ("Part the Veil", "The werewolf can immunize a human from the Delirium for a scene. (W20 Core, p. 155)")
        ]
    },
    "Metis": {
        1: [
            ("Create Element", "The werewolf can create small amounts of elemental matter (fire, water, earth, air) from nothing. (W20 Core, p. 155)"),
            ("Primal Anger", "The werewolf can channel their inner rage to become more powerful in combat. (W20 Core, p. 156)"),
            ("Rat Head", "The werewolf can squeeze through impossibly small gaps by making their bone structure collapsible. (W20 Core, p. 156)"),
            ("Sense Wyrm", "The werewolf can sense nearby manifestations of the Wyrm. This Gift involves a mystical sense, not a visual or olfactory image, although Garou often describe the Wyrm's spiritual emanations as a stench. (W20 Core, p. 156)"),
            ("Shed", "The werewolf can shed their skin to escape bonds or remove toxins. (W20 Core, p. 156)")
        ],
        2: [
            ("Burrow", "The werewolf can burrow through earth, creating tunnels. (W20 Core, p. 156)"),
            ("Curse of Hatred", "The werewolf can layer hate into their words, causing opponents to lose Willpower and Rage. (W20 Core, p. 156)"),
            ("Form Mastery", "The werewolf gains greater control over shapeshifting, reducing difficulties. (W20 Core, p. 156)"),
            ("Sense Silver", "The werewolf can detect the presence of silver within 100 yards. (W20 Core, p. 156)")
        ],
        3: [
            ("Chameleon", "The werewolf can blend with their surroundings, becoming difficult to see. (W20 Core, p. 156)"),
            ("Eyes of the Cat", "The werewolf can see clearly in complete darkness. (W20 Core, p. 157)"),
            ("Mental Speech", "The werewolf can communicate telepathically over vast distances. (W20 Core, p. 157)"),
            ("Shell", "The werewolf can create an emotional barrier, immunizing themselves against mind-altering magic. (W20 Core, p. 157)")
        ],
        4: [
            ("Gift of the Porcupine", "The werewolf's fur becomes sharp quills that damage those who touch them. (W20 Core, p. 157)"),
            ("Lash of Rage", "The werewolf can lash out with Rage to inflict unsoakable aggravated damage. (W20 Core, p. 157)"),
            ("Rattler's Bite", "The werewolf can inject deadly poison with their bite. (W20 Core, p. 157)"),
            ("Wither Limb", "The werewolf can cause a target's limb to wither and become useless. (W20 Core, p. 157)")
        ],
        5: [
            ("Madness", "The werewolf can drive others insane with a touch. (W20 Core, p. 157)"),
            ("Protean Form", "The werewolf can take on aspects of different animals. (W20 Core, p. 157)"),
            ("Totem Gift", "The werewolf can call upon their totem for aid. (W20 Core, p. 158)")
        ]
    },
    "Lupus": {
        1: [
            ("Hare's Leap", "The werewolf can leap great distances and heights with supernatural agility. (W20 Core, p. 158)"),
            ("Heightened Senses", "The werewolf's senses become incredibly acute, allowing them to perceive things others cannot. (W20 Core, p. 158)"),
            ("Predator's Arsenal", "The werewolf gains bite and claw attacks in Homid form. (W20 Core, p. 159)"),
            ("Prey Mind", "The werewolf can sense the fear and weaknesses of their prey. (W20 Core, p. 159)"),
            ("Sense Prey", "The werewolf can track and locate prey with supernatural accuracy. (W20 Core, p. 159)")
        ],
        2: [
            ("Axis Mundi", "The werewolf always knows what direction they are facing within the Gaia Realm. (W20 Core, p. 159)"),
            ("Eye of the Eagle", "The werewolf can see over impossibly long distances. (W20 Core, p. 159)"),
            ("Name the Spirit", "The werewolf can sense the type and approximate Trait levels of spirits. (W20 Core, p. 159)"),
            ("Scent of Sight", "The werewolf can use their sense of smell to compensate for lost vision. (W20 Core, p. 159)")
        ],
        3: [
            ("Catfeet", "The werewolf gains perfect balance and immunity to falls under 100 feet. (W20 Core, p. 159)"),
            ("Monkey Tail", "The werewolf can use their tail as a prehensile appendage. (W20 Core, p. 159)"),
            ("Sense the Unnatural", "The werewolf can sense any supernatural presence and determine its type. (W20 Core, p. 159)"),
            ("Silence the Weaver", "The werewolf can destroy nearby delicate electronics with a howl. (W20 Core, p. 160)"),
            ("Strength of Gaia", "While in lupus form, the werewolf enjoys the full might of Crinos. (W20 Core, p. 160)")
        ],
        4: [
            ("Beast Life", "The werewolf can communicate with and command wild animals. (W20 Core, p. 160)"),
            ("Gnaw", "The werewolf's jaws can chew through nearly anything and inflict extra damage. (W20 Core, p. 160)"),
            ("Scream of Gaia", "The werewolf emits a scream that batters foes and knocks them down. (W20 Core, p. 160)"),
            ("Terror of the Dire Wolf", "The werewolf can invoke the full Delirium on humans and formerly-human creatures. (W20 Core, p. 160)")
        ],
        5: [
            ("Elemental Gift", "The werewolf can command elemental forces of the world. (W20 Core, p. 160)"),
            ("Song of the Great Beast", "The werewolf can call upon ancient Great Beasts of antiquity. (W20 Core, p. 160)")
        ]
    }
}

# Auspice Gifts
AUSPICE_GIFTS = {
    "Ragabash": {
        1: [
            ("Blur of the Milky Eye", "The werewolf can become partially invisible or blur their form to avoid detection. (W20 Core, p. 161)"),
            ("Infectious Laughter", "The werewolf can cause others to laugh uncontrollably, disrupting their concentration. (W20 Core, p. 161)"),
            ("Liar's Face", "The werewolf can lie with perfect conviction, making their falsehoods seem like truth. (W20 Core, p. 161)"),
            ("Open Seal", "The werewolf can unlock doors, break seals, and open any barrier. (W20 Core, p. 161)"),
            ("Scent of Running Water", "The werewolf can mask their scent, making them harder to track. (W20 Core, p. 161)")
        ],
        2: [
            ("Blissful Ignorance", "The werewolf can become completely invisible to all senses by remaining still. (W20 Core, p. 161)"),
            ("Pulse of the Prey", "The werewolf can track any target they know anything about, anywhere. (W20 Core, p. 161)"),
            ("Spider's Song", "The werewolf can eavesdrop on telephone conversations and intercept messages. (W20 Core, p. 161)"),
            ("Taking the Forgotten", "The werewolf can steal something and make the victim forget they ever possessed it. (W20 Core, p. 162)")
        ],
        3: [
            ("Gremlins", "The werewolf can cause technological devices to malfunction by touching them. (W20 Core, p. 162)"),
            ("Liar's Craft", "The werewolf can tell outrageous lies and have them accepted as truth. (W20 Core, p. 162)"),
            ("Monkey Tail", "The werewolf can use their tail as a prehensile appendage. (W20 Core, p. 159)"),
            ("Open Moon Bridge", "The werewolf can open a moon bridge without the caern totem's permission. (W20 Core, p. 162)"),
            ("Pathfinder", "The werewolf can find the fastest and shortest routes between locations. (W20 Core, p. 162)")
        ],
        4: [
            ("Luna's Blessing", "When the moon is visible, silver ceases to act as a bane to the Garou. (W20 Core, p. 162)"),
            ("Umbral Dodge", "The werewolf can dodge attacks by sending the attacker into the Umbra. (W20 Core, p. 161)"),
            ("Whelp Body", "The werewolf can curse a foe's body, permanently reducing their Physical Attributes. (W20 Core, p. 162)")
        ],
        5: [
            ("Thieving Talons of the Magpie", "The werewolf can steal the powers of others and use them. (W20 Core, p. 163)"),
            ("Thousand Forms", "The werewolf can change into any animal between the sizes of a small bird and a bison. (W20 Core, p. 163)")
        ],
        6: [
            ("Firebringer", "The werewolf can steal a supernatural power and turn it into a Gift to bestow upon others. (W20 Core, p. 164)")
        ]
    },
    "Theurge": {
        1: [
            ("Mother's Touch", "The werewolf can heal wounds by touch, restoring health to themselves or others. (W20 Core, p. 164)"),
            ("Sense Wyrm", "The werewolf can sense nearby manifestations of the Wyrm. (W20 Core, p. 156)"),
            ("Spirit Snare", "The werewolf can trap and bind spirits. (W20 Core, p. 164)"),
            ("Spirit Speech", "The werewolf can communicate with spirits in their own language. (W20 Core, p. 164)"),
            ("Umbral Tether", "The werewolf can create a connection to the Umbra, allowing easier passage between worlds. (W20 Core, p. 164)")
        ],
        2: [
            ("Battle Mandala", "The werewolf creates a mystical sigil that drains Essence from spirits caught within it. (W20 Core, p. 164)"),
            ("Command Spirit", "The werewolf can give commands to spirits and expect obedience. (W20 Core, p. 164)"),
            ("Name the Spirit", "The werewolf can sense the type and approximate Trait levels of spirits. (W20 Core, p. 159)"),
            ("Sight From Beyond", "The werewolf becomes an oracle, prone to prophetic dreams and visions. (W20 Core, p. 165)")
        ],
        3: [
            ("Exorcism", "The werewolf can eject spirits from places, objects, or people. (W20 Core, p. 165)"),
            ("Pulse of the Invisible", "The werewolf gains constant awareness of the spirit world. (W20 Core, p. 161)"),
            ("Umbral Camouflage", "The werewolf becomes undetectable to spirits. (W20 Core, p. 165)"),
            ("Web Walker", "The werewolf can travel on the Pattern Web through the Umbra. (W20 Core, p. 165)")
        ],
        4: [
            ("Blurring the Mirror", "The werewolf can cloud minds, making it impossible for others to find the Umbra. (W20 Core, p. 165)"),
            ("Grasp the Beyond", "The werewolf can carry things in and out of the Umbra without dedicating them. (W20 Core, p. 165)"),
            ("Spirit Drain", "The werewolf can drain power from a spirit to feed their own resolve. (W20 Core, p. 165)"),
            ("Spirit Ward", "The werewolf can protect themselves from spirits with a warding rite. (W20 Core, p. 155)")
        ],
        5: [
            ("Feral Lobotomy", "The werewolf can devolve an opponent's mind into that of an animal. (W20 Core, p. 166)"),
            ("Malleable Spirit", "The werewolf can change a spirit's form or purpose. (W20 Core, p. 166)"),
            ("Ultimate Argument of Logic", "The werewolf can cause others to believe implicitly in any aspect of existence. (W20 Core, p. 166)")
        ]
    },
    "Philodox": {
        1: [
            ("Fangs of Judgment", "The werewolf's bite can reveal the truth or judge the guilt of their target. (W20 Core, p. 166)"),
            ("Persuasion", "The werewolf can convince others through logical argument and moral authority. (W20 Core, p. 153)"),
            ("Resist Pain", "The werewolf can ignore pain and continue fighting despite injuries. (W20 Core, p. 166)"),
            ("Scent of the True Form", "The werewolf can see through illusions and disguises to perceive the true nature of things. (W20 Core, p. 166)"),
            ("Truth of Gaia", "The werewolf can compel others to speak the truth. (W20 Core, p. 166)")
        ],
        2: [
            ("Call to Duty", "The werewolf can summon and command any spirit they know by name, or call all spirits in times of need. (W20 Core, p. 166)"),
            ("Command the Gathering", "The werewolf can command attention, preventing interruptions or departures. (W20 Core, p. 167)"),
            ("King of the Beasts", "The werewolf can command the loyalty of any single animal. (W20 Core, p. 167)"),
            ("Strength of Purpose", "The werewolf can recover Willpower by turning Rage into resolve. (W20 Core, p. 167)")
        ],
        3: [
            ("Mental Speech", "The werewolf can communicate telepathically over vast distances. (W20 Core, p. 157)"),
            ("Scent of the Oathbreaker", "The werewolf can sanctify oaths and track those who break them. (W20 Core, p. 167)"),
            ("Sense Balance", "The werewolf can sense an overabundance of Wyrm, Wyld, or Weaver energies. (W20 Core, p. 167)"),
            ("Weak Arm", "The werewolf can evaluate an opponent's fighting style and exploit weaknesses. (W20 Core, p. 167)"),
            ("Wisdom of the Ancient Ways", "The werewolf can tap into ancestral memories to remember ancient lore. (W20 Core, p. 167)")
        ],
        4: [
            ("Roll Over", "The werewolf radiates authority, forcing others to submit. (W20 Core, p. 167)"),
            ("Scent of Beyond", "The werewolf can hurl their senses to any familiar location, perceiving it from above. (W20 Core, p. 167)"),
            ("Take the True Form", "The werewolf can force a being into its true form. (W20 Core, p. 168)")
        ],
        5: [
            ("Geas", "The werewolf can bind an individual or group to a sacred oath. (W20 Core, p. 168)"),
            ("Wall of Granite", "The werewolf can create an unbreakable barrier of will. (W20 Core, p. 168)")
        ]
    },
    "Galliard": {
        1: [
            ("Beast Speech", "The werewolf can communicate with animals in their own languages. (W20 Core, p. 169)"),
            ("Call of the Wyld", "The werewolf can inspire others to greatness through song, story, or performance. (W20 Core, p. 169)"),
            ("Heightened Senses", "The werewolf's senses become incredibly acute. (W20 Core, p. 158)"),
            ("Mindspeak", "The werewolf can communicate telepathically with others. (W20 Core, p. 169)"),
            ("Perfect Recall", "The werewolf can remember events with perfect clarity, never forgetting details. (W20 Core, p. 169)")
        ],
        2: [
            ("Call of the Wyrm", "The werewolf can attract creatures of the Wyrm, luring them into traps. (W20 Core, p. 169)"),
            ("Command the Gathering", "The werewolf can command attention, preventing interruptions. (W20 Core, p. 167)"),
            ("Distractions", "The werewolf can make distracting sounds to divert attention. (W20 Core, p. 169)"),
            ("Dreamspeak", "The werewolf can walk among another's dreams and affect their course. (W20 Core, p. 169)"),
            ("Howls in the Night", "The werewolf's howl evokes primal terror in Gaia's enemies. (W20 Core, p. 169)")
        ],
        3: [
            ("Eye of the Cobra", "The werewolf can draw anyone to within striking distance with a stare. (W20 Core, p. 169)"),
            ("Song of Heroes", "The werewolf conjures the spirit of fallen heroes, infusing listeners with power. (W20 Core, p. 170)"),
            ("Song of Rage", "The werewolf can force others into frenzy or berserker rage. (W20 Core, p. 170)"),
            ("Song of the Siren", "The werewolf's song can entrance anyone who hears it. (W20 Core, p. 170)")
        ],
        4: [
            ("Bridge Walker", "The werewolf can create minor moon bridges for instant travel. (W20 Core, p. 170)"),
            ("Gift of Dreams", "The werewolf can craft and breathe dreams into sleeping individuals. (W20 Core, p. 170)"),
            ("Shadows by the Firelight", "The werewolf can create a shadow-play that sweeps others into a narrative. (W20 Core, p. 170)")
        ],
        5: [
            ("Fabric of the Mind", "The werewolf can bring the products of their imagination to life. (W20 Core, p. 170)")
        ]
    },
    "Ahroun": {
        1: [
            ("Falling Touch", "The werewolf's touch can cause enemies to fall or stumble. (W20 Core, p. 170)"),
            ("Inspiration", "The werewolf can inspire their packmates to fight harder and better. (W20 Core, p. 171)"),
            ("Pack Tactics", "The werewolf can coordinate pack attacks with supernatural efficiency. (W20 Core, p. 171)"),
            ("Razor Claws", "The werewolf's claws become incredibly sharp and deadly. (W20 Core, p. 171)"),
            ("Spur Claws", "The werewolf can extend their claws even further, dealing more damage. (W20 Core, p. 171)")
        ],
        2: [
            ("Sense Silver", "The werewolf can detect the presence of silver within 100 yards. (W20 Core, p. 156)"),
            ("Shield of Rage", "The werewolf's Rage causes all lesser furies to quail before it. (W20 Core, p. 188)"),
            ("Spirit of the Fray", "The werewolf gains blinding speed and lightning reflexes. (W20 Core, p. 171)"),
            ("True Fear", "The werewolf can cow an enemy into quiescence with terror. (W20 Core, p. 171)")
        ],
        3: [
            ("Combat Healing", "The werewolf can mend injuries without rest, even in combat. (W20 Core, p. 171)"),
            ("Heart of Fury", "The werewolf can suppress their Rage, making frenzy more difficult. (W20 Core, p. 171)"),
            ("Silver Claws", "The werewolf's claws transform into silver, inflicting aggravated damage. (W20 Core, p. 171)"),
            ("Wind Claws", "The werewolf's attacks ignore all armor protection. (W20 Core, p. 172)")
        ],
        4: [
            ("Body Shift", "The werewolf can shift physical Attribute dots between Strength, Dexterity, and Stamina. (W20 Core, p. 154)"),
            ("Clenched Jaw", "The werewolf's bite locks onto a target and won't release until they choose. (W20 Core, p. 172)"),
            ("Full Moon's Light", "The werewolf can illuminate any who oppose them within one mile. (W20 Core, p. 172)"),
            ("Stoking Fury's Furnace", "The werewolf regains Rage when taking damage and can spend Rage without losing it. (W20 Core, p. 172)")
        ],
        5: [
            ("Kiss of Helios", "The werewolf gains immunity to flame and can ignite portions of their body. (W20 Core, p. 172)"),
            ("Strength of Will", "The werewolf becomes a pillar of indomitable will, sharing it with allies. (W20 Core, p. 172)")
        ],
        6: [
            ("Unstoppable Warrior", "The werewolf can heal all aggravated damage as though it were lethal, save for silver wounds. (W20 Core, p. 172)")
        ]
    }
}

# Tribe Gifts - Level 1 only for character creation
TRIBE_GIFTS = {
    "Black Furies": {
        1: [
            ("Breath of the Wyld", "The werewolf can channel the power of the Wyld to enhance their abilities. (W20 Core, p. 173)"),
            ("Man's Skin", "The werewolf can appear completely human, hiding their werewolf nature. (W20 Core, p. 173)"),
            ("Heightened Senses", "The werewolf's senses become incredibly acute. (W20 Core, p. 158)"),
            ("Sense Wyrm", "The werewolf can sense nearby manifestations of the Wyrm. (W20 Core, p. 156)"),
            ("Wyld Resurgence", "The werewolf can restore natural areas and heal the land. (W20 Core, p. 173)")
        ],
        2: [
            ("Curse of Aeolus", "The werewolf can call up a thick fog that obscures vision and unnerves opponents. (W20 Core, p. 173)"),
            ("Form Mastery", "The werewolf gains greater control over shapeshifting, reducing difficulties. (W20 Core, p. 156)"),
            ("Kali's Tongue", "The werewolf can prevent enemies from healing damage. (W20 Core, p. 173)"),
            ("Kneel", "The werewolf can force a target to their knees with a gesture. (W20 Core, p. 173)"),
            ("Pulse of the Prey", "The werewolf can track any target they know anything about. (W20 Core, p. 161)")
        ],
        3: [
            ("Coup de Grace", "The werewolf finds their foe's greatest weakness and strikes at it. (W20 Core, p. 173)"),
            ("Heart Claw", "The werewolf breaks off a claw in a wound, which burrows toward the heart. (W20 Core, p. 173)"),
            ("Visceral Agony", "The werewolf's claws become barbed talons that inflict crippling pain. (W20 Core, p. 174)"),
            ("Wings of Pegasus", "The werewolf can sprout wings in Hispo form, allowing flight. (W20 Core, p. 174)")
        ],
        4: [
            ("Beast Life", "The werewolf can communicate with and command wild animals. (W20 Core, p. 160)"),
            ("Body Wrack", "The werewolf induces debilitating agony in opponents. (W20 Core, p. 174)"),
            ("Wasp Talons", "The werewolf can fire their claws like darts. (W20 Core, p. 174)")
        ],
        5: [
            ("Gorgon's Gaze", "The werewolf's gaze can transform living flesh into stone. (W20 Core, p. 174)"),
            ("Thousand Forms", "The werewolf can change into any animal between small bird and bison size. (W20 Core, p. 163)"),
            ("Wyld Warp", "The werewolf summons a swarm of Wyld-spirits to aid them. (W20 Core, p. 174)")
        ]
    },
    "Bone Gnawers": {
        1: [
            ("Cooking", "The werewolf can create nourishing meals from almost nothing, turning scraps into sustenance. (W20 Core, p. 174)"),
            ("Resist Toxin", "The werewolf can resist poisons, drugs, and toxins. (W20 Core, p. 174)"),
            ("Smell of Man", "The werewolf can blend into human society. (W20 Core, p. 153)"),
            ("Urban Tracking", "The werewolf can track targets through urban environments. (W20 Core, p. 161)"),
            ("Wall Running", "The werewolf can run up walls and across vertical surfaces. (W20 Core, p. 152)")
        ],
        2: [
            ("Between the Cracks", "The werewolf can find isolated, abandoned urban locations. (W20 Core, p. 175)"),
            ("Blissful Ignorance", "The werewolf can become completely invisible by remaining still. (W20 Core, p. 161)"),
            ("Cornered Rat's Ferocity", "The werewolf gains combat bonuses when backed into a corner. (W20 Core, p. 175)"),
            ("Guise of the Hound", "The werewolf can disguise their Lupus form to appear as a large dog. (W20 Core, p. 175)"),
            ("Odious Aroma", "The werewolf can amplify their musk to incapacitate foes. (W20 Core, p. 175)")
        ],
        3: [
            ("Call the Rust", "The werewolf can summon destructive rust onto any metal. (W20 Core, p. 175)"),
            ("Gift of the Skunk", "The werewolf can spray musk like a skunk. (W20 Core, p. 175)"),
            ("Gift of the Termite", "The werewolf can cause wood and paper to rot with astonishing speed. (W20 Core, p. 175)")
        ]
    },
    "Children of Gaia": {
        1: [
            ("Calm", "The werewolf can calm others, reducing their Rage and preventing violence. (W20 Core, p. 195)"),
            ("Mother's Touch", "The werewolf can heal wounds by touch. (W20 Core, p. 164)"),
            ("Persuasion", "The werewolf can convince others through peaceful means. (W20 Core, p. 153)"),
            ("Resist Pain", "The werewolf can ignore pain and continue fighting. (W20 Core, p. 166)"),
            ("Scent of the True Form", "The werewolf can see through illusions. (W20 Core, p. 166)")
        ],
        2: [
            ("Calm", "The werewolf can quell the anger in others, removing Rage points. (W20 Core, p. 195)"),
            ("Grandmother's Touch", "The werewolf can heal wounds by touch, including themselves. (W20 Core, p. 177)"),
            ("Luna's Armor", "The werewolf gains protection from moonlight, adding dice to soak pools. (W20 Core, p. 177)"),
            ("Para Bellum", "The werewolf gains combat bonuses when defending against unprovoked attacks. (W20 Core, p. 177)"),
            ("Unicorn's Arsenal", "The werewolf's claws and fangs become pearlescent, causing enemies to lose the will to fight. (W20 Core, p. 177)")
        ],
        3: [
            ("Calm the Savage Beast", "The werewolf can calm a frenzying Garou. (W20 Core, p. 154)"),
            ("Dazzle", "The werewolf can flood a target's mind with the glory of Gaia, rendering them harmless. (W20 Core, p. 178)"),
            ("Lover's Touch", "The werewolf can restore wounds, Willpower, Essence, or suppress Derangements. (W20 Core, p. 178)"),
            ("Spirit Friend", "The werewolf projects tranquility that spirits naturally perceive. (W20 Core, p. 178)")
        ],
        4: [
            ("Beast Life", "The werewolf can communicate with and command wild animals. (W20 Core, p. 160)"),
            ("Serenity", "The werewolf can fill a heart with peace, preventing Rage rolls and frenzy. (W20 Core, p. 178)"),
            ("Strike the Air", "The werewolf becomes unable to attack but also unable to be hit. (W20 Core, p. 178)"),
            ("Uncaught Since the Primal Morn", "The werewolf gains perfect speed, outrunning any pursuer. (W20 Core, p. 178)")
        ],
        5: [
            ("Halo of the Sun", "The werewolf is surrounded by blazing sunlight, harming Wyrm-creatures. (W20 Core, p. 178)"),
            ("The Living Wood", "The werewolf can animate nearby trees to protect them. (W20 Core, p. 178)")
        ]
    },
    "Fianna": {
        1: [
            ("Beast Speech", "The werewolf can communicate with animals. (W20 Core, p. 169)"),
            ("Blarney", "The werewolf can charm others with words and stories. (W20 Core, p. 179)"),
            ("Persuasion", "The werewolf can convince others. (W20 Core, p. 153)"),
            ("Resist Pain", "The werewolf can ignore pain. (W20 Core, p. 166)"),
            ("Song of Rage", "The werewolf can inspire Rage in others through song. (W20 Core, p. 170)")
        ],
        2: [
            ("Glib Tongue", "Listeners hear whatever the werewolf wishes them to hear. (W20 Core, p. 179)"),
            ("Flame Dance", "The werewolf can dodge attacks with enhanced reflexes. (W20 Core, p. 179)"),
            ("Form Mastery", "The werewolf gains greater control over shapeshifting. (W20 Core, p. 156)"),
            ("Howl of the Banshee", "The werewolf emits a fearful howl that causes terror. (W20 Core, p. 179)"),
            ("Howl of the Unseen", "The werewolf's howl echoes across both sides of the Gauntlet. (W20 Core, p. 179)")
        ],
        3: [
            ("Faerie Kin", "The werewolf can call upon ancient pacts with the fae. (W20 Core, p. 179)"),
            ("Fair Fortune", "The werewolf is blessed with luck, allowing re-rolls of failed rolls. (W20 Core, p. 179)"),
            ("Ley Lines", "The werewolf can manipulate ley lines to disorient trackers. (W20 Core, p. 179)"),
            ("Reshape Object", "The werewolf can transform once-living material into other objects. (W20 Core, p. 154)"),
            ("Song of the Siren", "The werewolf's song can entrance anyone who hears it. (W20 Core, p. 170)")
        ],
        4: [
            ("Balor's Gaze", "The werewolf's gaze inflicts terrible agony on enemies. (W20 Core, p. 179)"),
            ("Phantasm", "The werewolf creates realistic illusions with multiple sensory elements. (W20 Core, p. 180)")
        ],
        5: [
            ("Call the Hunt", "The werewolf calls forth the Huntsman of Celtic mythology. (W20 Core, p. 180)"),
            ("Fog on the Moor", "The werewolf becomes incorporeal, passing through anything except silver. (W20 Core, p. 180)"),
            ("Gift of the Spriggan", "The werewolf can grow to three times normal size or shrink to puppy size. (W20 Core, p. 180)")
        ]
    },
    "Get of Fenris": {
        1: [
            ("Falling Touch", "The werewolf's touch can cause enemies to fall. (W20 Core, p. 170)"),
            ("Inspiration", "The werewolf can inspire their packmates. (W20 Core, p. 171)"),
            ("Razor Claws", "The werewolf's claws become incredibly sharp. (W20 Core, p. 171)"),
            ("Resist Pain", "The werewolf can ignore pain. (W20 Core, p. 166)"),
            ("True Fear", "The werewolf can inspire supernatural fear in their enemies. (W20 Core, p. 171)")
        ],
        2: [
            ("Fangs of the North", "The werewolf's claws and teeth become ice daggers that cause wounds to fester. (W20 Core, p. 180)"),
            ("Halt the Coward's Flight", "The werewolf can slow a fleeing foe. (W20 Core, p. 180)"),
            ("Snarl of the Predator", "The werewolf's snarl terrifies opponents and reduces their dice pools. (W20 Core, p. 180)"),
            ("Troll Skin", "The werewolf's skin grows tough and thick, adding dice to soak rolls. (W20 Core, p. 181)")
        ],
        3: [
            ("Might of Thor", "The werewolf can double their Strength temporarily. (W20 Core, p. 181)"),
            ("Redirect Pain", "The werewolf can visit the pain of their wounds upon those who inflicted them. (W20 Core, p. 181)"),
            ("Venom Blood", "The werewolf's blood becomes acidic bile that poisons those who touch it. (W20 Core, p. 181)")
        ],
        4: [
            ("Body Shift", "The werewolf can shift physical Attribute dots between Strength, Dexterity, and Stamina. (W20 Core, p. 154)"),
            ("Heart of the Mountain", "The werewolf becomes untiring and cannot be defeated in endurance tests. (W20 Core, p. 181)"),
            ("Hero's Stand", "The werewolf channels Gaia's power, gaining bonuses but cannot move from the spot. (W20 Core, p. 181)"),
            ("Scream of Gaia", "The werewolf emits a scream that batters foes and knocks them down. (W20 Core, p. 160)")
        ],
        5: [
            ("Endurance of Heimdall", "The werewolf's Stamina rating is doubled for the scene. (W20 Core, p. 182)"),
            ("Horde of Valhalla", "The werewolf summons Great Wolves to aid them. (W20 Core, p. 182)"),
            ("Fenris' Bite", "The werewolf's bite can mangle and sever limbs. (W20 Core, p. 182)")
        ],
        6: [
            ("Call Great Fenris", "The werewolf can summon the war-avatar of Great Fenris to aid in combat. (W20 Core, p. 182)")
        ]
    },
    "Glass Walkers": {
        1: [
            ("Control Simple Machine", "The werewolf can control and manipulate technology. (W20 Core, p. 182)"),
            ("Cybersenses", "The werewolf can perceive and interact with digital information. (W20 Core, p. 183)"),
            ("Persuasion", "The werewolf can convince others. (W20 Core, p. 153)"),
            ("Smell of Man", "The werewolf can blend into human society. (W20 Core, p. 153)"),
            ("Urban Tracking", "The werewolf can track through urban environments. (W20 Core, p. 161)")
        ],
        2: [
            ("Cybersenses", "The werewolf can exchange natural senses for those of machines. (W20 Core, p. 183)"),
            ("Hands Full of Thunder", "The werewolf's firearms never run out of ammunition. (W20 Core, p. 184)"),
            ("Jam Technology", "The werewolf can cause technological devices to malfunction. (W20 Core, p. 153)"),
            ("Power Surge", "The werewolf can cause a blackout over a widespread area. (W20 Core, p. 184)"),
            ("Steel Fur", "The werewolf's fur becomes hardened metal, adding dice to soak rolls. (W20 Core, p. 184)")
        ],
        3: [
            ("Control Complex Machine", "The werewolf can command the spirits of electronic devices. (W20 Core, p. 184)"),
            ("Electroshock", "The werewolf can use electricity to damage opponents. (W20 Core, p. 184)"),
            ("Elemental Favor", "The werewolf can convince urban elementals to do favors. (W20 Core, p. 186)"),
            ("Intrusion", "The werewolf can open any barrier presented to them. (W20 Core, p. 184)")
        ],
        4: [
            ("Attunement", "The werewolf can commune with city spirits for information. (W20 Core, p. 193)"),
            ("Doppelganger", "The werewolf can take the exact likeness of any other human, wolf, or Garou. (W20 Core, p. 184)"),
            ("Signal Rider", "The werewolf can open a moon bridge that rides telephone signals. (W20 Core, p. 184)"),
            ("Tech Speak", "The werewolf can contact others through any technological device. (W20 Core, p. 185)")
        ],
        5: [
            ("Chaos Mechanics", "The werewolf may use Rage and Gnosis in the same turn with no penalty. (W20 Core, p. 185)"),
            ("Summon Net-Spider", "The werewolf can summon a Net-Spider for control over computer systems. (W20 Core, p. 185)")
        ]
    },
    "Red Talons": {
        1: [
            ("Heightened Senses", "The werewolf's senses become incredibly acute. (W20 Core, p. 158)"),
            ("Prey Mind", "The werewolf can sense the fear of their prey. (W20 Core, p. 159)"),
            ("Sense Prey", "The werewolf can track and locate prey. (W20 Core, p. 159)"),
            ("Shed", "The werewolf can shed their skin to escape. (W20 Core, p. 156)"),
            ("True Fear", "The werewolf can inspire supernatural fear. (W20 Core, p. 171)")
        ],
        2: [
            ("Beastmind", "The werewolf can reduce a victim's mental faculties to that of an animal. (W20 Core, p. 186)"),
            ("Pulse of the Prey", "The werewolf can track any target they know anything about. (W20 Core, p. 161)"),
            ("Howls in the Night", "The werewolf's howl evokes primal terror in Gaia's enemies. (W20 Core, p. 169)"),
            ("Shadows of the Impergium", "The werewolf becomes the embodiment of humanity's primal fears of the wolf. (W20 Core, p. 186)")
        ],
        3: [
            ("Elemental Favor", "The werewolf can convince natural elementals to do favors. (W20 Core, p. 186)"),
            ("Render Down", "The werewolf can destroy any man-made substance with a touch. (W20 Core, p. 186)"),
            ("Territory", "The werewolf can extend their senses to any area they have marked. (W20 Core, p. 187)"),
            ("Trackless Waste", "The werewolf can call upon wilderness spirits to mislead and confuse invaders. (W20 Core, p. 187)")
        ],
        4: [
            ("Gorge", "The werewolf can store extra Rage, Gnosis, or Willpower beyond their permanent rating. (W20 Core, p. 187)"),
            ("Howl of Death", "The werewolf's howl inflicts grievous wounds on a target. (W20 Core, p. 187)"),
            ("Quicksand", "The werewolf turns the ground into a sticky morass that catches foes. (W20 Core, p. 187)")
        ],
        5: [
            ("Curse of Lycaon", "The werewolf can force the wolf-skin onto another. (W20 Core, p. 187)"),
            ("Gaia's Vengeance", "The werewolf calls upon Gaia to strike on their behalf. (W20 Core, p. 187)"),
            ("Scabwalker Curse", "The werewolf makes a target violently allergic to Weaver-works of man. (W20 Core, p. 187)")
        ],
        6: [
            ("Shield of Gaia", "The werewolf becomes immune to the effects of one form of technology. (W20 Core, p. 188)")
        ]
    },
    "Shadow Lords": {
        1: [
            ("Fatal Flaw", "The werewolf can perceive and exploit the weaknesses of others. (W20 Core, p. 188)"),
            ("Liar's Face", "The werewolf can lie with perfect conviction. (W20 Core, p. 161)"),
            ("Persuasion", "The werewolf can convince others. (W20 Core, p. 153)"),
            ("Scent of the True Form", "The werewolf can see through illusions. (W20 Core, p. 166)"),
            ("Staredown", "The werewolf can intimidate others with a mere glance. (W20 Core, p. 154)")
        ],
        2: [
            ("Clap of Thunder", "The werewolf creates a thunderclap that stuns those who hear it. (W20 Core, p. 189)"),
            ("Cold Voice of Reason", "The werewolf can talk their way out of attacks with clever remarks. (W20 Core, p. 189)"),
            ("Howls in the Night", "The werewolf's howl evokes primal terror in Gaia's enemies. (W20 Core, p. 169)"),
            ("Luna's Armor", "The werewolf gains protection from moonlight, adding dice to soak pools. (W20 Core, p. 177)"),
            ("Song of the Earth Mother", "The werewolf can sense supernatural activity within a broad area. (W20 Core, p. 190)")
        ],
        3: [
            ("Direct the Storm", "The werewolf can direct the frenzy of another werewolf. (W20 Core, p. 190)"),
            ("Icy Chill of Despair", "The werewolf appears larger and more imposing, becoming a terrible shadowy version of themselves. (W20 Core, p. 190)")
        ],
        4: [
            ("Shadow Pack", "The werewolf can create shadow duplicates of themselves. (W20 Core, p. 191)"),
            ("Storm's Wrath", "The werewolf can call down lightning from the sky. (W20 Core, p. 182)")
        ],
        5: [
            ("Grandfather Thunder's Wrath", "The werewolf can summon a devastating storm. (W20 Core, p. 182)"),
            ("Shadow Mastery", "The werewolf gains complete control over shadows in an area. (W20 Core, p. 188)")
        ]
    },
    "Silent Striders": {
        1: [
            ("Hare's Leap", "The werewolf can leap great distances. (W20 Core, p. 158)"),
            ("Heightened Senses", "The werewolf's senses become incredibly acute. (W20 Core, p. 158)"),
            ("Open Seal", "The werewolf can unlock doors and break seals. (W20 Core, p. 161)"),
            ("Speed of Thought", "The werewolf can move with incredible speed. (W20 Core, p. 191)"),
            ("Wisdom of the Ancient", "The werewolf can access ancient knowledge and memories. (W20 Core, p. 167)")
        ],
        2: [
            ("Axis Mundi", "The werewolf always knows what direction they are facing within the Gaia Realm. (W20 Core, p. 159)"),
            ("Blissful Ignorance", "The werewolf can become completely invisible by remaining still. (W20 Core, p. 161)"),
            ("Messenger's Fortitude", "The werewolf can run at full speed for three days without rest, food, or water. (W20 Core, p. 192)"),
            ("Speech of the World", "The werewolf can speak and understand any human language. (W20 Core, p. 154)"),
            ("Tread Sebek's Back", "The werewolf can walk or run across water or other liquids. (W20 Core, p. 192)")
        ],
        3: [
            ("Adaptation", "The werewolf takes no damage from poison or disease and can exist in any environment. (W20 Core, p. 192)"),
            ("Great Leap", "The werewolf can jump truly astounding distances. (W20 Core, p. 192)"),
            ("Mark of the Death-Wolf", "The werewolf gouges a sigil that fascinates and attracts the unquiet dead. (W20 Core, p. 192)"),
            ("Sense the Unnatural", "The werewolf can sense any supernatural presence and determine its type. (W20 Core, p. 159)")
        ],
        4: [
            ("Attunement", "The werewolf can commune with city or wilderness spirits for information. (W20 Core, p. 193)"),
            ("Black Mark", "The werewolf's claws mark foes fit for the attentions of the restless dead. (W20 Core, p. 193)"),
            ("Dam the Heartflood", "The werewolf can nullify the magic inherent to blood. (W20 Core, p. 193)"),
            ("Speed Beyond Thought", "The werewolf can run at 10 times normal land speed. (W20 Core, p. 193)")
        ],
        5: [
            ("Gate of the Moon", "The werewolf creates a specialized moon bridge for instant travel. (W20 Core, p. 193)"),
            ("Reach the Umbra", "The werewolf may step in and out of the Umbra at will. (W20 Core, p. 193)")
        ]
    },
    "Silver Fangs": {
        1: [
            ("Falling Touch", "The werewolf's touch can cause enemies to fall. (W20 Core, p. 170)"),
            ("Inspiration", "The werewolf can inspire their packmates. (W20 Core, p. 171)"),
            ("Lambent Flame", "The werewolf can create and control fire. (W20 Core, p. 193)"),
            ("Persuasion", "The werewolf can convince others. (W20 Core, p. 153)"),
            ("True Fear", "The werewolf can inspire supernatural fear. (W20 Core, p. 171)")
        ],
        2: [
            ("Empathy", "The werewolf can read the feelings and expectations of groups. (W20 Core, p. 193)"),
            ("Hand Blade", "The werewolf can turn their arm into a razor-sharp blade. (W20 Core, p. 193)"),
            ("Luna's Armor", "The werewolf gains protection from moonlight, adding dice to soak pools. (W20 Core, p. 177)"),
            ("Sense Silver", "The werewolf can detect the presence of silver within 100 yards. (W20 Core, p. 156)"),
            ("Unity of the Pack", "The werewolf's pack gains bonuses when executing Pack Tactics. (W20 Core, p. 194)")
        ],
        3: [
            ("Burning Blade", "The werewolf's weapon burns with deadly fire. (W20 Core, p. 194)"),
            ("Silver Claws", "The werewolf's claws transform into silver, inflicting aggravated damage. (W20 Core, p. 171)"),
            ("Talons of the Falcon", "The werewolf's claws transform into impaling weapons. (W20 Core, p. 194)"),
            ("Wrath of Gaia", "The werewolf shows himself in full, terrible glory, overwhelming minions of the Wyrm. (W20 Core, p. 194)")
        ],
        4: [
            ("Mastery", "The werewolf can command other Garou to do their bidding. (W20 Core, p. 194)"),
            ("Mindblock", "The werewolf fortifies their will against mystical influences. (W20 Core, p. 194)"),
            ("Sidestep Death", "The werewolf can sidestep what would have become their deathblow. (W20 Core, p. 194)")
        ],
        5: [
            ("Luna's Avenger", "The werewolf transforms their body into living silver, immune to silver's effects. (W20 Core, p. 194)"),
            ("Paws of the Newborn Cub", "The werewolf can temporarily suppress an opponent's supernatural powers. (W20 Core, p. 195)")
        ],
        6: [
            ("Renew the Cycle", "The werewolf can correct grievous wrongs done to the natural cycle, destroying the undead. (W20 Core, p. 195)")
        ]
    },
    "Stargazers": {
        1: [
            ("Balance", "The werewolf can maintain perfect balance and equilibrium. (W20 Core, p. 195)"),
            ("Calm", "The werewolf can calm others and reduce Rage. (W20 Core, p. 195)"),
            ("Heightened Senses", "The werewolf's senses become incredibly acute. (W20 Core, p. 158)"),
            ("Resist Pain", "The werewolf can ignore pain. (W20 Core, p. 166)"),
            ("Wisdom of the Ancient", "The werewolf can access ancient knowledge. (W20 Core, p. 167)")
        ],
        2: [
            ("Inner Light", "The werewolf can step sideways into the Umbra using only their own inner light. (W20 Core, p. 196)"),
            ("Inner Strength", "The werewolf can convert inner anger into iron resolve. (W20 Core, p. 195)"),
            ("Resist Temptation", "The werewolf can resist worldly, material, and spiritual temptations. (W20 Core, p. 195)"),
            ("Surface Attunement", "The werewolf can traverse any terrain at normal speed without leaving tracks. (W20 Core, p. 195)"),
            ("Wuxing", "The werewolf can transform one Asian element into another. (W20 Core, p. 195)")
        ],
        3: [
            ("Clarity", "The werewolf can see through fog, darkness, invisibility, and recognize illusions. (W20 Core, p. 196)"),
            ("Merciful Blow", "The werewolf can subdue a foe in combat without harming them. (W20 Core, p. 196)"),
            ("Sense Balance", "The werewolf can sense an overabundance of Wyrm, Wyld, or Weaver energies. (W20 Core, p. 167)"),
            ("Wind's Returning Favor", "The werewolf can steal an opponent's weapon during combat. (W20 Core, p. 196)")
        ],
        4: [
            ("Preternatural Awareness", "The werewolf becomes preternaturally aware, anticipating opponents' actions. (W20 Core, p. 196)"),
            ("Mindblock", "The werewolf fortifies their will against mystical influences. (W20 Core, p. 194)"),
            ("Strike the Air", "The werewolf becomes unable to attack but also unable to be hit. (W20 Core, p. 178)")
        ],
        5: [
            ("Circular Attack", "The werewolf can dodge and redirect attacks, turning a mob into a weapon against itself. (W20 Core, p. 196)"),
            ("Harmonious Unity of the Emerald Mother", "The werewolf enjoys Crinos form bonuses while in Homid. (W20 Core, p. 196)"),
            ("Wisdom of the Seer", "The werewolf becomes a channel for the wisdom of the Tellurian. (W20 Core, p. 196)")
        ]
    },
    "Uktena": {
        1: [
            ("Mother's Touch", "The werewolf can heal wounds by touch. (W20 Core, p. 164)"),
            ("Sense Wyrm", "The werewolf can sense the Wyrm. (W20 Core, p. 156)"),
            ("Spirit Speech", "The werewolf can communicate with spirits. (W20 Core, p. 164)"),
            ("Umbral Tether", "The werewolf can create connections to the Umbra. (W20 Core, p. 164)"),
            ("Wisdom of the Ancient", "The werewolf can access ancient knowledge. (W20 Core, p. 167)")
        ],
        2: [
            ("Coils of the Serpent", "The werewolf calls forth dark tentacles of mist that wrap around enemies. (W20 Core, p. 197)"),
            ("Fetish Fetch", "The werewolf can draw fetishes from a hidden cache and return them easily. (W20 Core, p. 197)"),
            ("Shadows at Dawn", "The werewolf can share knowledge that later vanishes from the subject's memory. (W20 Core, p. 198)"),
            ("Spirit of the Bird", "The werewolf may hover, fly, or float. (W20 Core, p. 198)"),
            ("Spirit of the Fish", "The werewolf can breathe underwater and swim as fast as they can run. (W20 Core, p. 198)")
        ],
        3: [
            ("Banish Totem", "The werewolf can bar pack or personal totems from giving their children aid. (W20 Core, p. 198)"),
            ("Chains of Mist", "The werewolf's claws spin out silvery filaments that enwrap and confound spirits. (W20 Core, p. 198)"),
            ("Invisibility", "The werewolf can vanish from sight. (W20 Core, p. 198)"),
            ("Rending the Craft", "The werewolf's claws burn with mystic force, rending apart magical workings. (W20 Core, p. 198)"),
            ("Scrying", "The werewolf may view events elsewhere by staring into a reflective surface. (W20 Core, p. 198)")
        ],
        4: [
            ("Call Elemental", "The werewolf can call one of the four classic elementals to their aid. (W20 Core, p. 198)"),
            ("Durance", "The werewolf dominates a talen-bound spirit, forcibly lengthening its service. (W20 Core, p. 190)"),
            ("Hand of the Earth Lords", "The werewolf can move any object weighing up to 2,000 pounds by gesturing. (W20 Core, p. 199)")
        ],
        5: [
            ("Fabric of the Mind", "The werewolf can bring the products of their imagination to life. (W20 Core, p. 170)"),
            ("Fetish Doll", "The werewolf can harm victims from afar using a specially-created doll. (W20 Core, p. 199)")
        ]
    },
    "Wendigo": {
        1: [
            ("Heightened Senses", "The werewolf's senses become incredibly acute. (W20 Core, p. 158)"),
            ("Prey Mind", "The werewolf can sense the fear of their prey. (W20 Core, p. 159)"),
            ("Resist Pain", "The werewolf can ignore pain. (W20 Core, p. 166)"),
            ("Sense Prey", "The werewolf can track and locate prey. (W20 Core, p. 159)"),
            ("True Fear", "The werewolf can inspire supernatural fear. (W20 Core, p. 171)")
        ],
        2: [
            ("Cutting Wind", "The werewolf conjures a bitterly cold blast of wind that knocks opponents down. (W20 Core, p. 200)"),
            ("Claws of Frozen Death", "The werewolf's claws and teeth become ice daggers that cause wounds to fester. (W20 Core, p. 180)"),
            ("Salmon Swim", "The werewolf can swim as easily as a fish or walk on the surface of water. (W20 Core, p. 200)"),
            ("Speak with Wind Spirits", "The werewolf may call upon wind-spirits for knowledge and guidance. (W20 Core, p. 200)"),
            ("True Fear", "The werewolf can cow an enemy into quiescence with terror. (W20 Core, p. 171)")
        ],
        3: [
            ("Blood of the North", "The werewolf takes winter as their brother, ignoring cold penalties. (W20 Core, p. 201)"),
            ("Bloody Feast", "The werewolf gains strength from an enemy's flesh and blood. (W20 Core, p. 201)"),
            ("Sky Running", "The werewolf gains the ability to run at 50 mph through the skies. (W20 Core, p. 201)"),
            ("Wisdom of the Ancient Ways", "The werewolf can tap into ancestral memories to remember ancient lore. (W20 Core, p. 167)")
        ],
        4: [
            ("Call of the Cannibal Spirit", "The werewolf can summon an avatar of Great Wendigo to hunt down a target. (W20 Core, p. 201)"),
            ("Chill of Early Frost", "The werewolf calls down a mystical chill, freezing the surrounding land. (W20 Core, p. 201)"),
            ("Hero's Stand", "The werewolf channels Gaia's power, gaining bonuses but cannot move from the spot. (W20 Core, p. 181)"),
            ("Scream of Gaia", "The werewolf emits a scream that batters foes and knocks them down. (W20 Core, p. 160)")
        ],
        5: [
            ("Invoke the Spirits of the Storm", "The werewolf can summon nearly any weather effect. (W20 Core, p. 201)"),
            ("Heart of Ice", "The werewolf can call down the curse of the Wendigo, turning a victim's innards to ice. (W20 Core, p. 201)")
        ]
    },
    "Black Spiral Dancers": {
        1: [
            # From W20 Core
            ("Bane Protector", "The werewolf can protect themselves and others from the harmful effects of Banes and Wyrm-tainted creatures. (W20 Core, p. 426)"),
            ("Resist Pain", "The werewolf can ignore pain and continue fighting despite injuries. (W20 Core, p. 166)"),
            ("Resist Toxin", "The werewolf can resist poisons, drugs, and toxins. (W20 Core, p. 174)"),
            ("Sense Wyrm", "The werewolf can sense nearby manifestations of the Wyrm. (W20 Core, p. 156)"),
            ("Shroud", "The werewolf can hide their presence from detection, masking their spiritual aura and making them harder to track. (W20 Core, p. 197)"),
            # From Book of the Wyrm
            ("Bale Armor", "The Black Spiral Dancer's body is limned in a terrible green-black radiance that saps the strength from her enemies' blows and inflicts toxic burns upon their flesh. (Book of the Wyrm, p. 121)"),
            ("Spiral-Shadow Dance", "The Black Spiral Dancer learns to twine herself through the darkness, becoming swift as a scream. (Book of the Wyrm, p. 121)"),
            ("Repress Taint", "The werewolf can hide their Wyrm taint from detection, making it harder for others to sense their corruption. (Book of the Wyrm, p. 123)"),
            ("Bale Aura", "The Dancer can shroud herself in the green light of balefire. The light causes no physical damage, but shadows cast by the light seem to move of their own accord and the whispers of the Wyrm crackle within the green flames, stoking the Rage within the Garou. (Book of the Wyrm, p. 123)"),
        ],
        2: [
            # From W20 Core
            ("Ears of the Bat", "The Black Spiral can use echolocation and sense concealed creatures. (W20 Core, p. 426)"),
            ("Wyrm Hide", "The Black Spiral can harden their skin into a leathery hide, gaining soak dice and treating lethal damage as bashing. (W20 Core, p. 426)"),
            ("A Thousand Voices", "The Black Spiral can create illusory images and sounds of a pack of shapeshifter allies. (W20 Core, p. 426)"),
            ("Allies Below", "The Galliard can summon spirits of the Earth to create tremors, sinkholes, or collapse buildings. (W20 Core, p. 426)"),
            ("Horns of the Impaler", "The Black Spiral grows chitinous horns for powerful attacks. (W20 Core, p. 426)"),
            # From Book of the Wyrm
            ("Grave Claws", "The werewolf's claws and fangs become obsidian daggers, capable of tearing the soul loose from Gaia's cycle and pinning it to the Dark Umbra. Any creature slain by this Gift is guaranteed to leave behind a ghost. (Book of the Wyrm, p. 121)"),
            ("Hidden Killer", "The werewolf can leave behind no physical evidence that would betray her hand in a slaying. After a battle, the Garou must touch or lick once each corpse she slew. The wounds alter themselves so that they resemble stabbing or slashing injuries rather than bite or claw marks. Any peripheral damage remains as it was, but all forensic evidence such as hair, saliva, or blood from the werewolf's body disappears from the scene. The werewolf can also choose to alter the evidence to match another Garou so long as she has a piece of the target. (Book of the Wyrm, p. 123)"),
            ("Submit", "Stolen from the Black Furies, with a snarl, a Black Spiral Dancer can force a target to kneel before him, agony coursing through her body until she submits. (Book of the Wyrm, p. 123)"),
        ],
        3: [
            # From W20 Core
            ("Patagia", "The Black Spiral has membranous flaps of skin for gliding and controlled flight. (W20 Core, p. 427)"),
            ("Foaming Fury", "The Black Spiral's bite can cause victims to frenzy. (W20 Core, p. 427)"),
            ("Beautiful Lie", "The Black Spiral can cover up ugly truths with mass delusions and false memories. (W20 Core, p. 427)"),
            ("Touch of the Eel", "The Black Spiral can release an electrical current through conductive materials or by touch. (W20 Core, p. 428)"),
            # From Book of the Wyrm
            ("Claws of Corrosion", "One of the greatest Black Spiral Gifts, this wicked magic allows the werewolf to poison a spirit with mystical toxins that slowly corrupt it into a servant of the Wyrm. (Book of the Wyrm, p. 121)"),
            ("Ichor Blade", "The Spiral's arm changes into a black blade dripping with dark green poison. The ichor poisons the blood of anyone injured by the blade, causing crippling agony. (Book of the Wyrm, p. 123)"),
            ("Gift of the Tainted Totem", "A twisted version of an Uktena Gift, a Dancer can not only bar a pack totem from aiding its children, she can temporarily replace the totem with her own pack or personal totem. (Book of the Wyrm, p. 123)"),
        ],
        4: [
            # From W20 Core
            ("Crawling Poison", "The Black Spiral can infect other shapeshifters with a slow-acting poison that suppresses regeneration. (W20 Core, p. 428)"),
            ("Call Elemental", "The Black Spiral summons a Wyrm elemental. (W20 Core, p. 198)"),
            ("Open Wounds", "The werewolf causes the next wound they inflict to bleed profusely, dealing continuous damage. (W20 Core, p. 190)"),
            # From Book of the Wyrm
            ("Hungry Rust", "The werewolf summons a Bane and invests it into a mechanical device. The Bane awakens when someone next uses the device, spewing corruption throughout. (Book of the Wyrm, p. 122)"),
            ("Stolen Hide", "The Black Spiral Dancer can don tormented spirits like a cloak, consigning them to oblivion to protect himself. (Book of the Wyrm, p. 122)"),
            ("Howl of the Bane", "The Dancers have their own fearsome spirits to call, and in a blatant mockery of the Wendigo, a Spiral dances in a Blight or Hellhole, hooting, laughing, and slashing profane glyphs into the air. (Book of the Wyrm, p. 123)"),
            ("Summon Wyrm Elemental", "The Dancer performs a short dance around a piece of a pure element. The dance corrupts the element and summons forth a Wyrm Elemental. (Book of the Wyrm, p. 123)"),
        ],
        5: [
            # From W20 Core
            ("Balefire", "The Black Spiral can project burning globules of unholy green flame that inflict aggravated damage and Wyrm-fueled mutations. (W20 Core, p. 428)"),
            # From Book of the Wyrm
            ("The White Howl", "Once the most sacred blessing of the White Howlers, this mighty Gift is still passed down among the ranks of the Black Spiral Dancers as a reminder of the past to their Garou enemies. (Book of the Wyrm, p. 122)"),
            ("Mask Taint", "The werewolf may completely camouflage Wyrm-taint from all senses, including Gifts that detect such taint. This Gift allows a Black Spiral Dancer to hide their corruption from detection. (Book of the Wyrm, p. 123; see W20 Core, p. 199)"),
            ("Cloak of Anthelios", "Sculpted from Halo of the Sun, the character speaks the sacred word of Helios while drawing on his own Wyrm-tainted powers. The character is wreathed in violent red flame that drapes about him as a cloak. (Book of the Wyrm, p. 123)"),
        ]
    }
}

# ============================================================================
# WYRMISH GIFTS (Book of the Wyrm)
# ============================================================================

WYRMISH_BREED_GIFTS = {
    "Homid": {
        1: [
            ("Aura of Poison", "The Black Spiral Dancer surrounds herself in a toxic miasma strong enough to cause even a human's dull sense of smell to pick up the reek of a lethal stew of mercury, sulfuric acid, formaldehyde, and countless other chemicals. The message is clear: the Dancer is death, and should not be trifled with. (Book of the Wyrm, p. 117)"),
        ],
        4: [
            ("Feast of Man-Flesh", "The Black Spiral Dancers know of the power locked away in the flesh of men. By eating the uncooked flesh of a human being, the werewolf may temporarily borrow that person's knowledge and skills. (Book of the Wyrm, p. 117)"),
        ],
    },
    "Metis": {
        1: [
            ("Bleed", "The metis can leak phantasmal blood, manifesting false injuries if she is unwounded, or producing enormous quantities of blood from minor wounds. Many Spirals use this Gift to 'play dead' when a battle is going poorly, or to frame innocents for vicious attacks. (Book of the Wyrm, p. 119)"),
        ],
        3: [
            ("Nobody's Bastard", "Nobody wants to recognize a metis, and with this Gift, nobody will. A metis using this Gift is unrecognizable to all who see her. (Book of the Wyrm, p. 119)"),
        ],
    },
    "Lupus": {
        1: [
            ("Ways of the Urban Wolf", "The Black Spiral Dancers are free to indulge in those natural urges that Gaia bids her defenders to restrain: to hunt man through the streets of the cities, to revel in his fear-stench, to drink his blood and eat his flesh. This Gift makes the Dancer a master of such urban hunts. (Book of the Wyrm, p. 119)"),
        ],
        3: [
            ("Thousand Teeth", "Sharp teeth are the hallmarks of the ultimate predator, and the ways of the Wyrm's wolves celebrate nothing if not excess. The muzzle of a werewolf using this Gift erupts with dozens of extra teeth. (Book of the Wyrm, p. 119)"),
        ],
        5: [
            ("Instincts Unbound", "Gaia's warriors must explain the behavior of their fallen cousins as madness — why else would a wolf seek to despoil the world? The greatest among Black Spiral lupus use this Gift to teach the Garou the folly of their thinking by showing them the joys of unbound freedom. (Book of the Wyrm, p. 119)"),
        ],
    },
}

WYRMISH_AUSPICE_GIFTS = {
    "Ragabash": {
        1: [
            ("Bestowing the Predator's Shadow", "It would be fair to say that Black Spiral Dancers have even less tolerance for being tricked or mocked than other werewolves. This valuable Gift helps Dancer Ragabash survive the fallout of their Auspice's duties by passing their identity onto someone else. (Book of the Wyrm, p. 119)"),
        ],
        4: [
            ("Cassandra's Blessing", "The Wyrm's tricksters use division and isolation as instructive tools, particularly against their many enemies. The victim of this Gift's 'blessing' will find that nobody will believe anything she has to say, no matter how much evidence she has to back it up. (Book of the Wyrm, p. 120)"),
            ("Silver Reprisal", "Luna's servants only rarely extend her blessing to those who have danced the Black Spiral, but some Banes can add their own retributive curse to the Garou's vulnerability to silver. Rather than protecting the Dancer, this Gift causes silver to burn its wielder in the same moment it harms the werewolf. (Book of the Wyrm, p. 120)"),
        ],
        5: [
            ("Patience of the Wyrm", "This Gift allows incredibly elaborate acts of sabotage and revenge by allowing the Spiral Dancer to dictate the moment her curses strike her foes. (Book of the Wyrm, p. 120)"),
        ],
    },
    "Theurge": {
        2: [
            ("Poisoned Gauntlet", "The Black Spiral Dancer can breathe spiritual toxins into the wall between worlds, turning the Gauntlet into a deadly trap. (Book of the Wyrm, p. 120)"),
        ],
        3: [
            ("Feast of Essence", "The Black Spiral Dancer's claws are covered with barbed hooks, which catch and absorb the tattered power of slain spirits, refreshing the werewolf. (Book of the Wyrm, p. 120)"),
        ],
        6: [
            ("Prelude to Apocalypse", "This mighty Gift allows the Black Spiral Theurge to summon Wyrm-spirits of all kinds, calling forth a legion of Banes and corrupted spirits to do their bidding. This twisted version of the Gaian Gift As In the Beginning summons the full might of the Wyrm's spiritual forces. No Black Spiral Theurge has yet learned this Gift. (Book of the Wyrm, p. 120)"),
        ],
    },
    "Philodox": {
        1: [
            ("Acid Talons", "The Black Spiral Dancer's claws become a vibrant mixture of black, red, and yellow, and burn anything they cut. (Book of the Wyrm, p. 120)"),
        ],
        5: [
            ("Omen Claws", "The Black Spiral Dancer's claws become blades of anti-light, the area surrounding them suffused with a false glow as a contrast to their nullity. Anyone struck by these terrible claws suffers visions of the Apocalypse. (Book of the Wyrm, p. 120)"),
        ],
    },
    "Galliard": {
        2: [
            ("Howl of the Hunter", "Setting a particular quarry in her mind, the Black Spiral Dancer crafts a howl specifically designed to elicit terror in her prey. If her victim can hear the howl, it strikes terror into his heart, haunting him whenever he tries to find rest. (Book of the Wyrm, p. 121)"),
        ],
    },
    "Ahroun": {
        2: [
            ("Tar Shadow", "The Ahroun's shadow becomes solid and sticky, trapping unwary foes and making them easy prey. (Book of the Wyrm, p. 121)"),
        ],
        5: [
            ("Strength Without Limit", "Wyrmish power suffuses the flesh and bones of the warrior who uses this Gift, exaggerating his power beyond the limits of his body. His muscles bulk up until they tear through his skin, and his flesh peels back from wildly elongated teeth and claws. (Book of the Wyrm, p. 121)"),
        ],
    },
}

# ============================================================================
# BACKGROUNDS
# ============================================================================

BACKGROUNDS = {
    "standard": [
        ("Allies", "Friends who'll help you out"),
        ("Ancestors", "Spirits of your ancestors who guide and protect you"),
        ("Contacts", "Information sources and social networks"),
        ("Fetish", "A magical item with spirit powers"),
        ("Kinfolk", "Relatives who are not Garou but carry werewolf blood"),
        ("Mentor", "An elder Garou who teaches and guides you"),
        ("Pure Breed", "The strength of your bloodline, showing your connection to ancient Garou heroes"),
        ("Resources", "Financial credit, cash flow, and property"),
        ("Rites", "Knowledge of and ability to perform Garou rituals"),
        ("Totem", "A powerful spirit ally that protects and guides your pack")
    ],
    "restricted": [
        ("Fetish", "A magical item with spirit powers (restricted by some tribes)"),
        ("Pure Breed", "The strength of your bloodline (restricted by Bone Gnawers)")
    ]
}

# ============================================================================
# RENOWN
# ============================================================================

RENOWN_TYPES = ["Glory", "Honor", "Wisdom"]

# ============================================================================
# CHARACTER CREATION RULES
# ============================================================================

CREATION_RULES = {
    "attributes": {
        "primary": 7,
        "secondary": 5,
        "tertiary": 3,
        "base": 1  # All attributes start at 1
    },
    "abilities": {
        "primary": 13,
        "secondary": 9,
        "tertiary": 5,
        "max_at_creation": 3
    },
    "backgrounds": 5,
    "gifts": {
        "starting": 3,  # One from breed, auspice, and tribe
        "must_be_level": 1
    },
    "freebie_points": 15,
    "max_flaw_points": 7
}

FREEBIE_COSTS = {
    "attribute": 5,
    "ability": 2,
    "background": 1,
    "gift": 7,
    "rage": 2,
    "gnosis": 2,
    "willpower": 1,
    "renown": 1,
    "merit": 1,
    "specialty": 1
}

EXPERIENCE_COSTS = {
    "new_ability": 3,
    "new_gift": 10,
    "attribute": 4,  # current rating x 4
    "ability": 2,    # current rating x 2
    "background": 3, # current rating x 3
    "willpower": 1,  # current rating x 1
    "rage": 1,       # current rating x 1
    "gnosis": 2,     # current rating x 2
    "renown": 1,     # current rating x 1
    "specialty": 3
}

# ============================================================================
# ARCHETYPES (Nature & Demeanor) - Same as Mage
# ============================================================================

ARCHETYPES = {
    "Activist": "You fix a broken world",
    "Benefactor": "You've got the power to help, and so you do",
    "Contrary": "You invert order to reveal greater truths",
    "Crusader": "You're a front-line fighter for a better tomorrow",
    "Hacker": "You upgrade things by taking them apart",
    "Idealist": "A greater Truth awaits us, and you know what it is",
    "Innovator": "Your imagination drives progress forward",
    "Kid": "Innocent and playful, you inspire others to take care of you",
    "Loner": "You need no one else",
    "Machine": "Weakness is for lesser beings",
    "Mad Scientist": "True science knows no bounds!",
    "Martyr": "It's your pleasure to serve",
    "Monster": "You're the unapologetic shadow in the mirror of your world",
    "Prophet": "Speaking truth to power is your life's work",
    "Rogue": "Rebellion is your gospel and your fame",
    "Sensualist": "Sensation is your drug of choice",
    "Survivor": "No matter what happens, you endure",
    "Traditionalist": "As far as you're concerned, the old ways are best",
    "Trickster": "You make the world your toy",
    "Visionary": "You see beyond the obvious and chase a greater vision"
}

# ============================================================================
# MERITS AND FLAWS
# ============================================================================
# Using the same Merits and Flaws as Mage, as they're largely compatible
# Additional Werewolf-specific ones can be added later

MERITS = {
    "Physical": {
        "Acute Senses (Single)": {"cost": 1, "description": "One physical sense is unusually sharp (-2 difficulty to Perception rolls with that sense)"},
        "Acute Senses (All)": {"cost": 3, "description": "All five physical senses are unusually sharp (-2 difficulty to Perception rolls)"},
        "Ambidextrous": {"cost": 1, "description": "No penalty for using off-hand"},
        "Catlike Balance": {"cost": 1, "description": "-2 difficulty on balance-related rolls"},
        "Light Sleeper": {"cost": 1, "description": "Four hours of sleep works fine; wake up ready for action"},
        "Physically Impressive": {"cost": 2, "description": "+2 dice to intimidation rolls"},
        "Poison Resistance": {"cost": 2, "description": "+2 dice to Stamina rolls resisting toxins"},
        "Daredevil": {"cost": 3, "description": "+3 dice to non-combat acts of physical recklessness"},
        "Huge Size": {"cost": 4, "description": "Over 7 feet tall; one extra Bruised health level"},
        "Too Tough to Die": {"cost": 5, "description": "Can soak lethal damage"}
    },
    "Mental": {
        "Common Sense": {"cost": 1, "description": "Storyteller warns you before doing something stupid"},
        "Concentration": {"cost": 1, "description": "Eliminates modifiers from distractions"},
        "Code of Honor": {"cost": 2, "description": "+2 dice to Willpower when acting according to your code"},
        "Eidetic Memory": {"cost": 2, "description": "Photographic memory"},
        "Iron Will": {"cost": 3, "description": "+3 dice for Willpower rolls resisting mental influence"},
        "Berserker": {"cost": 4, "description": "Berserk rage grants combat bonuses but lose control"}
    },
    "Social": {
        "Natural Leader": {"cost": 1, "description": "-2 difficulty to Leadership rolls"},
        "Pitiable": {"cost": 1, "description": "People want to help you"},
        "Ties": {"cost": 3, "description": "Connections in a specific social group"},
        "True Love": {"cost": 4, "description": "Willpower restored when pursuing your true love"}
    },
    "Supernatural": {
        "Spirit Affinity": {"cost": 3, "description": "Easier to communicate with and bind spirits"},
        "Umbral Affinity": {"cost": 4, "description": "Reduced ill effects from Otherworld travel"},
        "Spirit Sight": {"cost": 4, "description": "Can see spirits without using Gifts"}
    }
}

FLAWS = {
    "Physical": {
        "Addiction (Minor)": {"bonus": 1, "description": "Addicted to something trivial"},
        "Impediment (Minor)": {"bonus": 1, "description": "Minor physical condition"},
        "Easily Intoxicated": {"bonus": 2, "description": "+3 difficulty to resist intoxication"},
        "Impediment (Moderate)": {"bonus": 2, "description": "Moderate physical condition (+1 difficulty)"},
        "Addiction (Severe)": {"bonus": 3, "description": "Addicted to something dangerous/illegal"},
        "Impediment (Significant)": {"bonus": 3, "description": "Significant physical condition (+1 difficulty)"},
        "Permanent Wound": {"bonus": 3, "description": "Always at Wounded health level"},
        "Impediment (Major)": {"bonus": 4, "description": "Major physical condition (+2 difficulty)"},
        "Impediment (Severe)": {"bonus": 6, "description": "Severe condition (+2-3 difficulty)"}
    },
    "Mental": {
        "Compulsion": {"bonus": 1, "description": "Compelled to perform a specific behavior"},
        "Nightmares": {"bonus": 1, "description": "Plagued by disturbing dreams"},
        "Phobia (Minor)": {"bonus": 1, "description": "Fear of something that can be avoided"},
        "Absent-Minded": {"bonus": 2, "description": "Forget things and lose track of time"},
        "Intolerance": {"bonus": 2, "description": "Strong prejudice against something"},
        "Phobia (Major)": {"bonus": 2, "description": "Fear of something common"},
        "Deranged (Moderate)": {"bonus": 3, "description": "Suffer from a mental illness"},
        "Phobia (Severe)": {"bonus": 3, "description": "Debilitating fear"},
        "Deranged (Severe)": {"bonus": 5, "description": "Severe mental illness"}
    },
    "Social": {
        "Blacklisted": {"bonus": 1, "description": "Barred from certain groups"},
        "Dark Secret": {"bonus": 1, "description": "A secret that would ruin you"},
        "Enemy (Minor)": {"bonus": 1, "description": "Someone wants to harm you"},
        "Enemy (Moderate)": {"bonus": 2, "description": "A dangerous person wants to harm you"},
        "Enemy (Major)": {"bonus": 3, "description": "A powerful person wants to harm you"},
        "Infamy": {"bonus": 2, "description": "Bad reputation"},
        "Notoriety": {"bonus": 3, "description": "Known for something shameful"},
        "Hunted": {"bonus": 4, "description": "Being actively pursued"}
    },
    "Supernatural": {
        "Cursed (Minor)": {"bonus": 1, "description": "Minor quirks of fate"},
        "Cursed (Annoying)": {"bonus": 2, "description": "Small but annoying problems"},
        "Cursed (Chronic)": {"bonus": 3, "description": "Chronic misfortune"},
        "Cursed (Major)": {"bonus": 4, "description": "Major problems arise"},
        "Cursed (Pervasive)": {"bonus": 5, "description": "Pervasive bad luck"}
    }
}

# ============================================================================
# SAMPLE CONCEPTS
# ============================================================================

CONCEPTS = [
    "Activist", "Artist", "Athlete", "Caretaker", "Criminal",
    "Executive", "Guardian", "Intellectual", "Kid", "Laborer",
    "Mystic", "Night-Owl", "Rebel", "Technician", "Warrior"
]

# ============================================================================
# CHANGING BREEDS
# ============================================================================

CHANGING_BREEDS = {
    "Garou": {
        "display_name": "Garou (Werewolf)",
        "breeds": BREEDS,
        "auspices": AUSPICES,
        "tribes": TRIBES,
        "forms": FORMS,
        "renown_types": ["Glory", "Honor", "Wisdom"],
        "starting_traits": {
            "rage": "by_auspice",  # Set by auspice
            "gnosis": "by_breed",   # Set by breed
            "willpower": "by_tribe"  # Set by tribe
        },
        "gifts": {
            "breed": BREED_GIFTS,
            "auspice": AUSPICE_GIFTS,
            "tribe": TRIBE_GIFTS,
            "wyrmish_breed": WYRMISH_BREED_GIFTS,
            "wyrmish_auspice": WYRMISH_AUSPICE_GIFTS,
        }
    },
    "Ajaba": {
        "display_name": "Ajaba (Werehyena)",
        "breeds": {
            "Homid": {
                "description": "Born to human mothers, raised among humans.",
                "initial_gnosis": 1,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Metis": {
                "description": "Born to two Ajaba. Fully accepted, develop faster than Garou metis.",
                "initial_gnosis": 3,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Hyaenid": {
                "description": "Born a hyena, closest to nature.",
                "initial_gnosis": 5,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {
            "Dawn": {
                "description": "First Change at dawn. Warriors and hunters.",
                "initial_rage": 5,
                "initial_gnosis": 1,
                "initial_willpower": 3,
                "beginning_gifts": []
            },
            "Midnight": {
                "description": "First Change at midnight. Storytellers and mediators.",
                "initial_rage": 3,
                "initial_gnosis": 3,
                "initial_willpower": 3,
                "beginning_gifts": []
            },
            "Dusk": {
                "description": "First Change at dusk. Tricksters and scouts.",
                "initial_rage": 1,
                "initial_gnosis": 5,
                "initial_willpower": 3,
                "beginning_gifts": []
            }
        },
        "tribes": {},  # Ajaba don't have tribes
        "forms": {
            "Homid": {
                "description": "Human form, bristly-haired, stocky torsos, long slim limbs.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Normal human appearance"
            },
            "Anthros": {
                "description": "Hybrid human/hyena form, upright but inhuman, terrifying appearance.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 1, "Stamina": 1,
                    "Charisma": 0, "Manipulation": -1, "Appearance": -3,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Larger than human",
                "special": "Invokes Delirium"
            },
            "Crinos": {
                "description": "War form, thickly matted fur, massive, several times Homid mass.",
                "statistics_adjustment": {
                    "Strength": 3, "Dexterity": 2, "Stamina": 4,
                    "Charisma": 0, "Manipulation": -2, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Massive, several times Homid mass",
                "special": "Invokes Delirium"
            },
            "Crocas": {
                "description": "Primordial war-form, bear-sized hyena, barrel-chested, thick-necked.",
                "statistics_adjustment": {
                    "Strength": 3, "Dexterity": 2, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -2, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Bear-sized",
                "special": "Crushing bite inflicts +1 die damage"
            },
            "Hyaenid": {
                "description": "Normal hyena form, endurance-based hunter.",
                "statistics_adjustment": {
                    "Strength": 1, "Dexterity": 2, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -2, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal hyena size",
                "special": "Endurance-based hunter"
            }
        },
        "renown_types": ["Glory", "Honor", "Wisdom"],
        "starting_traits": {
            "rage": "by_auspice",
            "gnosis": "by_breed",
            "willpower": 3  # Fixed for all Ajaba
        },
        "gifts": {
            "breed": BREED_GIFTS,  # Use Garou breed gifts (Homid/Metis/Hyaenid uses Lupus)
            "auspice": {
                "Dawn": {
                    1: [
                        ("Beat of the Heart-Drum", "The Ajaba can coordinate pack attacks with supernatural efficiency. (Changing Breeds, p. 52)"),
                        ("Finishing Blow", "The Ajaba can deliver a devastating final strike to finish off wounded enemies. (Changing Breeds, p. 52)"),
                        ("Lightning Reflexes", "The Ajaba gains blinding speed and lightning reflexes in combat. (Changing Breeds, p. 52)"),
                        ("Pack Tactics", "The Ajaba can coordinate pack attacks with supernatural efficiency. (Changing Breeds, p. 52)"),
                        ("Razor Claws", "The Ajaba's claws become incredibly sharp and deadly. (Changing Breeds, p. 52)"),
                        ("Resist Pain", "The Ajaba can ignore pain and continue fighting despite injuries. (Changing Breeds, p. 52)"),
                        ("Sense Wyrm", "The Ajaba can sense nearby manifestations of the Wyrm. (Changing Breeds, p. 52)")
                    ],
                    2: [
                        ("Command Spirit", "The Ajaba can give commands to spirits and expect obedience. (Changing Breeds, p. 52)"),
                        ("Dancing with the Dawn", "The Ajaba can move with incredible speed and grace at dawn. (Changing Breeds, p. 52)"),
                        ("Shield of Rage", "The Ajaba's Rage causes all lesser furies to quail before it. (Changing Breeds, p. 52)"),
                        ("Spirit of the Fray", "The Ajaba gains blinding speed and lightning reflexes. (Changing Breeds, p. 52)"),
                        ("Teeth at Dawn", "The Ajaba's bite becomes especially deadly at dawn. (Changing Breeds, p. 52)")
                    ],
                    3: [
                        ("Bloody Feast", "The Ajaba gains strength from an enemy's flesh and blood. (Changing Breeds, p. 52)"),
                        ("Redirect Pain", "The Ajaba can visit the pain of their wounds upon those who inflicted them. (Changing Breeds, p. 52)"),
                        ("Sense the Unnatural", "The Ajaba can sense any supernatural presence and determine its type. (Changing Breeds, p. 52)"),
                        ("Silver Jaws", "The Ajaba's jaws transform into silver, inflicting aggravated damage. (Changing Breeds, p. 52)")
                    ],
                    4: [
                        ("Battle Fury Focus", "The Ajaba can focus their rage into devastating combat prowess. (Changing Breeds, p. 52)"),
                        ("Grasp the Beyond", "The Ajaba can carry things in and out of the Umbra without dedicating them. (Changing Breeds, p. 52)"),
                        ("Stoking Fury's Furnace", "The Ajaba regains Rage when taking damage and can spend Rage without losing it. (Changing Breeds, p. 52)")
                    ],
                    5: [
                        ("Bone Cracker", "The Ajaba's bite can shatter bones and cause crippling damage. (Changing Breeds, p. 52)"),
                        ("Strength of Will", "The Ajaba becomes a pillar of indomitable will, sharing it with allies. (Changing Breeds, p. 52)")
                    ]
                },
                "Midnight": {
                    1: [
                        ("Beast Speech", "The Ajaba can communicate with animals in their own languages. (Changing Breeds, p. 52)"),
                        ("Burning the Vision", "The Ajaba can see visions of the future in flames. (Changing Breeds, p. 52)"),
                        ("Mindspeak", "The Ajaba can communicate telepathically with others. (Changing Breeds, p. 52)"),
                        ("Mother's Touch", "The Ajaba can heal wounds by touch, restoring health to themselves or others. (Changing Breeds, p. 52)"),
                        ("Perfect Recall", "The Ajaba can remember events with perfect clarity, never forgetting details. (Changing Breeds, p. 52)"),
                        ("Persuasion", "The Ajaba can convince others through peaceful means. (Changing Breeds, p. 52)"),
                        ("Tears of the Heavens", "The Ajaba can call upon the rains to wash away corruption. (Changing Breeds, p. 52)")
                    ],
                    2: [
                        ("Bless the Rains", "The Ajaba can call upon blessed rains to heal and restore. (Changing Breeds, p. 52)"),
                        ("Distractions", "The Ajaba can make distracting sounds to divert attention. (Changing Breeds, p. 52)"),
                        ("Dreamspeak", "The Ajaba can walk among another's dreams and affect their course. (Changing Breeds, p. 52)"),
                        ("Scavenge", "The Ajaba can find useful items and resources in unlikely places. (Changing Breeds, p. 52)"),
                        ("Shadows of the Serengeti", "The Ajaba can blend into the shadows of the savanna. (Changing Breeds, p. 52)")
                    ],
                    3: [
                        ("Calling the Eshu", "The Ajaba can call upon trickster spirits for aid. (Changing Breeds, p. 52)"),
                        ("Exorcism", "The Ajaba can eject spirits from places, objects, or people. (Changing Breeds, p. 52)"),
                        ("Song of Heroes", "The Ajaba conjures the spirit of fallen heroes, infusing listeners with power. (Changing Breeds, p. 52)"),
                        ("Wisdom of the Ancient Ways", "The Ajaba can tap into ancestral memories to remember ancient lore. (Changing Breeds, p. 52)")
                    ],
                    4: [
                        ("Bitter Tears", "The Ajaba's tears can cause despair and sorrow in enemies. (Changing Breeds, p. 52)"),
                        ("Gift of Dreams", "The Ajaba can craft and breathe dreams into sleeping individuals. (Changing Breeds, p. 52)"),
                        ("Phantasm", "The Ajaba creates realistic illusions with multiple sensory elements. (Changing Breeds, p. 52)")
                    ],
                    5: [
                        ("Fabric of the Mind", "The Ajaba can bring the products of their imagination to life. (Changing Breeds, p. 52)"),
                        ("Rain of Doom", "The Ajaba can call down a devastating rain that harms enemies. (Changing Breeds, p. 52)")
                    ]
                },
                "Dusk": {
                    1: [
                        ("Blur of the Milky Eye", "The Ajaba can become partially invisible or blur their form to avoid detection. (Changing Breeds, p. 54)"),
                        ("Fatal Flaw", "The Ajaba can perceive and exploit the weaknesses of others. (Changing Breeds, p. 54)"),
                        ("Laughter in the Night", "The Ajaba's laughter can cause terror and confusion in enemies. (Changing Breeds, p. 54)"),
                        ("Open Seal", "The Ajaba can unlock doors, break seals, and open any barrier. (Changing Breeds, p. 54)"),
                        ("Scent of Running Water", "The Ajaba can mask their scent, making them harder to track. (Changing Breeds, p. 54)"),
                        ("Spirit Snare", "The Ajaba can trap and bind spirits. (Changing Breeds, p. 54)"),
                        ("Spirit Speech", "The Ajaba can communicate with spirits in their own language. (Changing Breeds, p. 54)"),
                        ("Whispers in the Grass", "The Ajaba can communicate secretly through natural sounds. (Changing Breeds, p. 54)")
                    ],
                    2: [
                        ("Ambush", "The Ajaba can set up perfect ambushes, gaining surprise bonuses. (Changing Breeds, p. 54)"),
                        ("Blissful Ignorance", "The Ajaba can become completely invisible to all senses by remaining still. (Changing Breeds, p. 54)"),
                        ("Luna's Armor", "The Ajaba gains protection from moonlight, adding dice to soak pools. (Changing Breeds, p. 54)"),
                        ("Sight From Beyond", "The Ajaba becomes an oracle, prone to prophetic dreams and visions. (Changing Breeds, p. 54)"),
                        ("Taking the Forgotten", "The Ajaba can steal something and make the victim forget they ever possessed it. (Changing Breeds, p. 54)")
                    ],
                    3: [
                        ("Paralyzing Stare", "The Ajaba's stare can freeze enemies in place. (Changing Breeds, p. 54)"),
                        ("Pulse of the Invisible", "The Ajaba gains constant awareness of the spirit world. (Changing Breeds, p. 54)"),
                        ("Smoky Passage", "The Ajaba can pass through smoke and shadows. (Changing Breeds, p. 54)"),
                        ("Umbral Strike", "The Ajaba can attack from the Umbra. (Changing Breeds, p. 54)")
                    ],
                    4: [
                        ("Becoming the Night Jester", "The Ajaba becomes a master of shadows and trickery. (Changing Breeds, p. 54)"),
                        ("Echoes of the Asamando", "The Ajaba can call upon the dead for aid. (Changing Breeds, p. 54)"),
                        ("Open Wounds", "The Ajaba can cause old wounds to reopen and bleed. (Changing Breeds, p. 54)")
                    ],
                    5: [
                        ("Reach the Umbra", "The Ajaba may step in and out of the Umbra at will. (Changing Breeds, p. 54)"),
                        ("Shadow Pack", "The Ajaba can create shadow duplicates of themselves. (Changing Breeds, p. 54)")
                    ]
                }
            },
            "tribe": {},
            "general": {
                1: [
                    ("Eye of the Hunter", "The Ajaba can track prey with supernatural accuracy. (Changing Breeds, p. 51)"),
                    ("Feral Grin", "The Ajaba's grin can cause fear and intimidation. (Changing Breeds, p. 51)"),
                    ("Gift of Terror", "The Ajaba can inspire supernatural fear in their enemies. (Changing Breeds, p. 51)"),
                    ("Infectious Laughter", "The Ajaba can cause others to laugh uncontrollably, disrupting their concentration. (Changing Breeds, p. 51)"),
                    ("Primal Anger", "The Ajaba can channel their inner rage to become more powerful in combat. (Changing Breeds, p. 51)"),
                    ("Sense Prey", "The Ajaba can track and locate prey with supernatural accuracy. (Changing Breeds, p. 51)")
                ],
                2: [
                    ("Crushing Jaws", "The Ajaba's bite becomes incredibly powerful, capable of crushing bone. (Changing Breeds, p. 51)"),
                    ("Curse of Hatred", "The Ajaba can layer hate into their words, causing opponents to lose Willpower and Rage. (Changing Breeds, p. 51)"),
                    ("Gender Shift", "The Ajaba can temporarily change their apparent gender. (Changing Breeds, p. 51)"),
                    ("Odious Aroma", "The Ajaba can amplify their musk to incapacitate foes. (Changing Breeds, p. 51)"),
                    ("Pulse of the Prey", "The Ajaba can track any target they know anything about, anywhere. (Changing Breeds, p. 51)")
                ],
                3: [
                    ("Clenched Jaw", "The Ajaba's bite locks onto a target and won't release until they choose. (Changing Breeds, p. 51)"),
                    ("Gift of the Skunk", "The Ajaba can spray musk like a skunk. (Changing Breeds, p. 51)"),
                    ("Laugh of the Hyena", "The Ajaba's laugh can cause confusion and disorientation. (Changing Breeds, p. 51)"),
                    ("Laughter of the Soul", "The Ajaba's laughter can heal and restore allies. (Changing Breeds, p. 51)")
                ],
                4: [
                    ("Culling the Weak", "The Ajaba can identify and target the weakest enemies. (Changing Breeds, p. 51)"),
                    ("Gnaw", "The Ajaba's jaws can chew through nearly anything and inflict extra damage. (Changing Breeds, p. 51)"),
                    ("Gorge", "The Ajaba can store extra Rage, Gnosis, or Willpower beyond their permanent rating. (Changing Breeds, p. 51)"),
                    ("Strength of Kilimanjaro", "The Ajaba gains incredible strength and endurance. (Changing Breeds, p. 51)"),
                    ("Survivor", "The Ajaba can survive in the harshest conditions. (Changing Breeds, p. 51)")
                ],
                5: [
                    ("Withering Stare", "The Ajaba's stare can cause enemies to wither and weaken. (Changing Breeds, p. 51)")
                ]
            }
        }
    },
    "Ananasi": {
        "display_name": "Ananasi (Werespider)",
        "breeds": {
            "Homid": {
                "description": "Born to human mothers, internal organs altered for blood processing.",
                "initial_gnosis": 1,
                "initial_willpower": 3,
                "initial_blood_pool": 10,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Arachnid": {
                "description": "Born a spider, closest to the Web.",
                "initial_gnosis": 3,
                "initial_willpower": 2,
                "initial_blood_pool": 10,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {
            "Tenere": {
                "description": "Weaver aspect - focus on order and structure.",
                "initial_rage": 0,  # Ananasi use Blood Pool, not Rage
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Hatar": {
                "description": "Wyrm aspect - focus on corruption and destruction.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Kumoti": {
                "description": "Wyld aspect - focus on chaos and change.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            }
        },
        "tribes": {
            "Myrmidon": {
                "description": "Warrior faction.",
                "initial_willpower": 0,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Viskr": {
                "description": "Wizard faction.",
                "initial_willpower": 0,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Wyrsta": {
                "description": "Questioner faction.",
                "initial_willpower": 0,
                "beginning_gifts": [],
                "restrictions": {}
            }
        },
        "forms": {
            "Homid": {
                "description": "Human appearance, but internal organs altered for blood processing, venom glands and vestigial fangs present.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Venom glands and vestigial fangs present"
            },
            "Lilian": {
                "description": "Spider/human hybrid, terrifying, 50% larger than human.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 3, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -1, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "50% larger than human",
                "special": "Invokes full Delirium"
            },
            "Pithus": {
                "description": "Giant spider form, 500-700 lbs.",
                "statistics_adjustment": {
                    "Strength": 4, "Dexterity": 1, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "500-700 lbs",
                "special": "Invokes full Delirium, can spin steel-strong webs"
            },
            "Crawlerling": {
                "description": "Breaks into hundreds/thousands of normal-sized spiders.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 5, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Hundreds/thousands of normal-sized spiders",
                "special": "Transformation invokes Delirium"
            }
        },
        "renown_types": ["Glory", "Honor", "Wisdom"],  # May need adjustment
        "starting_traits": {
            "rage": 0,  # Ananasi use Blood Pool instead
            "gnosis": "by_breed",
            "willpower": "by_breed",
            "blood_pool": 10  # All Ananasi start with 10
        },
        "gifts": {
            "breed": {},
            "auspice": {
                "Tenere": {
                    1: [
                        ("Groom", "The Ananasi can clean and maintain themselves and others. (Changing Breeds, p. 66)"),
                        ("Patience of Ananasa", "The Ananasi gains incredible patience and focus. (Changing Breeds, p. 66)"),
                        ("Beneath Notice", "The Ananasi can become nearly invisible to detection. (Changing Breeds, p. 66)")
                    ],
                    2: [
                        ("Breath of Ananasa", "The Ananasi can breathe life into inanimate objects. (Changing Breeds, p. 66)"),
                        ("Mother's Look", "The Ananasi can see through deception and lies. (Changing Breeds, p. 66)")
                    ],
                    3: [
                        ("Reshape Object", "The Ananasi can transform once-living material into other objects instantly. (Changing Breeds, p. 66)"),
                        ("Understanding the Tapestry", "The Ananasi can understand the patterns of the Weaver. (Changing Breeds, p. 66)")
                    ],
                    4: [
                        ("Web Sheet", "The Ananasi can create protective webs. (Changing Breeds, p. 66)")
                    ],
                    5: [
                        ("Thieving Touch of Spiders", "The Ananasi can steal powers and abilities from others. (Changing Breeds, p. 66)")
                    ]
                },
                "Hatar": {
                    1: [
                        ("Blood of Pain", "The Ananasi's blood causes pain to those who touch it. (Changing Breeds, p. 66)"),
                        ("Wyrmling Kinship", "The Ananasi can communicate with Wyrm creatures. (Changing Breeds, p. 66)")
                    ],
                    2: [
                        ("Blood of Illusion", "The Ananasi can create illusions with their blood. (Changing Breeds, p. 66)"),
                        ("Call of the Wyrm", "The Ananasi can attract creatures of the Wyrm. (Changing Breeds, p. 66)")
                    ],
                    3: [
                        ("Corrupt", "The Ananasi can corrupt objects and places. (Changing Breeds, p. 66)"),
                        ("Pulse of the Invisible", "The Ananasi gains constant awareness of the spirit world. (Changing Breeds, p. 66)")
                    ],
                    4: [
                        ("Ill Winds", "The Ananasi can call upon corrupting winds. (Changing Breeds, p. 66)"),
                        ("Still Blood", "The Ananasi can stop their blood flow to prevent bleeding. (Changing Breeds, p. 66)")
                    ],
                    5: [
                        ("Burning Blood", "The Ananasi's blood becomes acidic and burns enemies. (Changing Breeds, p. 66)")
                    ]
                },
                "Kumoti": {
                    1: [
                        ("Inspire", "The Ananasi can inspire others to greatness. (Changing Breeds, p. 67)"),
                        ("Mother's Touch", "The Ananasi can heal wounds by touch. (Changing Breeds, p. 67)")
                    ],
                    2: [
                        ("Arachnophobia", "The Ananasi can cause intense fear of spiders. (Changing Breeds, p. 67)"),
                        ("Insight of the Mother", "The Ananasi gains deep insights into situations. (Changing Breeds, p. 67)")
                    ],
                    3: [
                        ("Alter Lilian", "The Ananasi can change their Lilian form appearance. (Changing Breeds, p. 67)"),
                        ("Sense Motion", "The Ananasi can sense all motion in an area. (Changing Breeds, p. 67)")
                    ],
                    4: [
                        ("Mindblock", "The Ananasi fortifies their will against mystical influences. (Changing Breeds, p. 67)"),
                        ("Nature of the Beast", "The Ananasi can understand the true nature of things. (Changing Breeds, p. 67)")
                    ],
                    5: [
                        ("Assimilation", "The Ananasi can blend into any culture or environment. (Changing Breeds, p. 67)")
                    ]
                }
            },
            "tribe": {
                "Myrmidon": {
                    1: [
                        ("Illusion of Size", "The Ananasi can appear larger or smaller than they are. (Changing Breeds, p. 67)"),
                        ("Open Seal", "The Ananasi can unlock doors, break seals, and open any barrier. (Changing Breeds, p. 67)")
                    ],
                    2: [
                        ("Hydraulic Strength", "The Ananasi gains incredible strength through hydraulic pressure. (Changing Breeds, p. 67)"),
                        ("True Fear", "The Ananasi can inspire supernatural fear in their enemies. (Changing Breeds, p. 67)")
                    ],
                    3: [
                        ("Scorpion Tail", "The Ananasi can manifest a scorpion's stinging tail. (Changing Breeds, p. 67)"),
                        ("Weak Arm", "The Ananasi can evaluate an opponent's fighting style and exploit weaknesses. (Changing Breeds, p. 67)")
                    ],
                    4: [
                        ("Blood Hunt", "The Ananasi can track targets by their blood. (Changing Breeds, p. 67)"),
                        ("Drying Bite", "The Ananasi's bite can drain moisture from targets. (Changing Breeds, p. 67)")
                    ],
                    5: [
                        ("Image of the Great Mother", "The Ananasi can appear as a terrifying spider goddess. (Changing Breeds, p. 67)")
                    ]
                },
                "Viskr": {
                    1: [
                        ("Curse of the Great Web", "The Ananasi can curse targets through the Web. (Changing Breeds, p. 67)"),
                        ("Shroud", "The Ananasi can hide their presence from detection. (Changing Breeds, p. 67)")
                    ],
                    2: [
                        ("Mindspeak", "The Ananasi can communicate telepathically with others. (Changing Breeds, p. 67)"),
                        ("Minor Unweaving", "The Ananasi can unravel minor magical effects. (Changing Breeds, p. 67)")
                    ],
                    3: [
                        ("Calcify", "The Ananasi can turn targets to stone. (Changing Breeds, p. 67)"),
                        ("Cocoon", "The Ananasi can wrap targets in protective cocoons. (Changing Breeds, p. 67)")
                    ],
                    4: [
                        ("Attunement", "The Ananasi can commune with spirits for information. (Changing Breeds, p. 67)"),
                        ("Brethren Call", "The Ananasi can call upon other Ananasi for aid. (Changing Breeds, p. 67)")
                    ],
                    5: [
                        ("Shattering", "The Ananasi can shatter objects and barriers with a touch. (Changing Breeds, p. 67)")
                    ]
                },
                "Wyrsta": {
                    1: [
                        ("Alter Mood", "The Ananasi can change the emotional state of others. (Changing Breeds, p. 68)"),
                        ("Beastmind", "The Ananasi can reduce a victim's mental faculties to that of an animal. (Changing Breeds, p. 68)")
                    ],
                    2: [
                        ("Blinding Spit", "The Ananasi can spit venom that blinds targets. (Changing Breeds, p. 68)"),
                        ("Visceral Agony", "The Ananasi's attacks inflict crippling pain. (Changing Breeds, p. 68)")
                    ],
                    3: [
                        ("Tick Body", "The Ananasi can become incredibly resilient to damage. (Changing Breeds, p. 68)"),
                        ("Blades of the Mantis", "The Ananasi can manifest mantis-like blades. (Changing Breeds, p. 68)")
                    ],
                    4: [
                        ("Wither Limb", "The Ananasi can cause a target's limb to wither and become useless. (Changing Breeds, p. 68)"),
                        ("Razor Webs", "The Ananasi can create webs that cut like razors. (Changing Breeds, p. 68)")
                    ],
                    5: [
                        ("Summon Net-Spider", "The Ananasi can summon a Net-Spider for control over computer systems. (Changing Breeds, p. 68)")
                    ]
                }
            },
            "general": {
                1: [
                    ("Balance", "The Ananasi can maintain perfect balance and equilibrium. (Changing Breeds, p. 65)"),
                    ("Cling", "The Ananasi can cling to any surface. (Changing Breeds, p. 65)"),
                    ("Many Eyes", "The Ananasi gains multiple points of vision. (Changing Breeds, p. 65)"),
                    ("Resist Pain", "The Ananasi can ignore pain and continue fighting. (Changing Breeds, p. 65)"),
                    ("Resist Toxin", "The Ananasi can resist poisons, drugs, and toxins. (Changing Breeds, p. 65)"),
                    ("Stolen Moments", "The Ananasi can steal moments of time. (Changing Breeds, p. 65)")
                ],
                2: [
                    ("Hand Fangs", "The Ananasi can manifest fangs in their hands. (Changing Breeds, p. 65)"),
                    ("Man-Spider Form", "The Ananasi can shift between human and spider forms. (Changing Breeds, p. 65)"),
                    ("Replenishment of the Flesh", "The Ananasi can heal using blood. (Changing Breeds, p. 65)"),
                    ("Spines", "The Ananasi can manifest sharp spines. (Changing Breeds, p. 65)")
                ],
                3: [
                    ("Blood Pump", "The Ananasi can increase their blood pool capacity. (Changing Breeds, p. 65)"),
                    ("Jump", "The Ananasi can leap great distances. (Changing Breeds, p. 65)"),
                    ("Spider's Grace", "The Ananasi gains incredible agility and grace. (Changing Breeds, p. 65)")
                ],
                4: [
                    ("Entropic Bite", "The Ananasi's bite causes entropy and decay. (Changing Breeds, p. 65)"),
                    ("Hydraulic Strength", "The Ananasi gains incredible strength through hydraulic pressure. (Changing Breeds, p. 65)")
                ],
                5: [
                    ("Carapace", "The Ananasi can create a protective carapace. (Changing Breeds, p. 65)"),
                    ("Survivor", "The Ananasi can survive in the harshest conditions. (Changing Breeds, p. 65)")
                ]
            }
        }
    },
    "Bastet": {
        "display_name": "Bastet (Werecat)",
        "breeds": {
            "Homid": {
                "description": "Born to human mothers, raised among humans.",
                "initial_gnosis": 1,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Metis": {
                "description": "Born to two Bastet who broke the Litany.",
                "initial_gnosis": 3,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Feline": {
                "description": "Born a cat, closest to nature.",
                "initial_gnosis": 5,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {
            "Daylight": {
                "description": "First Change during daylight hours. Warriors and leaders.",
                "initial_rage": 0,  # Varies by tribe
                "initial_gnosis": 0,
                "initial_willpower": 0,  # Varies by tribe
                "beginning_gifts": []
            },
            "Twilight": {
                "description": "First Change during twilight. Mediators and judges.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Night": {
                "description": "First Change during night. Tricksters and scouts.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            }
        },
        "tribes": {
            "Bagheera": {
                "description": "Black panthers, guardians of the jungle.",
                "initial_rage": 2,
                "initial_willpower": 3,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Balam": {
                "description": "Jaguars, warriors of the rainforest.",
                "initial_rage": 4,
                "initial_willpower": 2,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Bubasti": {
                "description": "Serval cats, mystics and seers.",
                "initial_rage": 1,
                "initial_willpower": 4,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Ceilican": {
                "description": "Wildcats, tricksters and rogues.",
                "initial_rage": 2,
                "initial_willpower": 3,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Khan": {
                "description": "Tigers, proud warriors.",
                "initial_rage": 5,
                "initial_willpower": 2,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Pumonca": {
                "description": "Cougars, solitary hunters.",
                "initial_rage": 3,
                "initial_willpower": 3,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Qualmi": {
                "description": "Lynx, watchers and guardians.",
                "initial_rage": 2,
                "initial_willpower": 3,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Simba": {
                "description": "Lions, kings of the savanna.",
                "initial_rage": 4,
                "initial_willpower": 3,
                "beginning_gifts": [],
                "restrictions": {}
            },
            "Swara": {
                "description": "Cheetahs, speed and grace.",
                "initial_rage": 1,
                "initial_willpower": 4,
                "beginning_gifts": [],
                "restrictions": {}
            }
        },
        "forms": {
            "Homid": {
                "description": "Human form.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Normal human appearance"
            },
            "Sokto": {
                "description": "Near-human form (like Glabro). Statistics vary by tribe.",
                "statistics_adjustment": {
                    "Strength": 1, "Dexterity": 1, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -1, "Appearance": -1,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Larger than human",
                "special": "Statistics vary by tribe"
            },
            "Crinos": {
                "description": "War form, invokes Delirium. Statistics vary by tribe.",
                "statistics_adjustment": {
                    "Strength": 3, "Dexterity": 2, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Large war form",
                "special": "Invokes Delirium (reduced by 2 ranks). Statistics vary by tribe"
            },
            "Chatro": {
                "description": "Hybrid form between Crinos and Feline. Statistics vary by tribe.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 3, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -3, "Appearance": -2,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Hybrid size",
                "special": "Delirium at full strength, canines 3-5 inches, +1 die bite damage. Statistics vary by tribe"
            },
            "Feline": {
                "description": "Full cat form. Statistics vary by tribe.",
                "statistics_adjustment": {
                    "Strength": 1, "Dexterity": 3, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal cat size",
                "special": "Statistics vary by tribe"
            }
        },
        "renown_types": ["Cunning", "Ferocity", "Honor"],
        "starting_traits": {
            "rage": "by_tribe",
            "gnosis": "by_breed",
            "willpower": "by_tribe"
        },
        "gifts": {
            "breed": {
                "Homid": {
                    1: [
                        ("Cat's Cunning", "The Bastet gains increased intelligence. (Changing Breeds, p. 86)"),
                        ("Smell of Man", "The Bastet can blend into human society. (Changing Breeds, p. 86)")
                    ]
                },
                "Metis": {
                    1: [
                        ("Metis Power", "The Bastet gains power from their metis nature. (Changing Breeds, p. 87)"),
                        ("Cat's Strength", "The Bastet gains increased physical power. (Changing Breeds, p. 87)")
                    ]
                },
                "Feline": {
                    1: [
                        ("Cat's Grace", "The Bastet gains incredible agility. (Changing Breeds, p. 87)"),
                        ("Sense Prey", "The Bastet can track and locate prey. (Changing Breeds, p. 87)")
                    ]
                }
            },
            "auspice": {
                "Daylight": {
                    1: [
                        ("Daylight's Power", "The Bastet gains power during daylight. (Changing Breeds, p. 85)"),
                        ("Sun's Blessing", "The Bastet gains blessings from the sun. (Changing Breeds, p. 85)")
                    ],
                    2: [
                        ("Daylight's Mastery", "The Bastet gains mastery during daylight. (Changing Breeds, p. 85)"),
                        ("Sun's Wrath", "The Bastet can unleash the sun's fury. (Changing Breeds, p. 85)")
                    ],
                    3: [
                        ("Perfect Daylight", "The Bastet can create perfect daylight. (Changing Breeds, p. 85)"),
                        ("Sun's Dominion", "The Bastet gains dominion over the sun. (Changing Breeds, p. 85)")
                    ]
                },
                "Twilight": {
                    1: [
                        ("Twilight's Power", "The Bastet gains power during twilight. (Changing Breeds, p. 85)"),
                        ("Dusk's Blessing", "The Bastet gains blessings from dusk. (Changing Breeds, p. 85)")
                    ],
                    2: [
                        ("Twilight's Mastery", "The Bastet gains mastery during twilight. (Changing Breeds, p. 85)"),
                        ("Dusk's Wrath", "The Bastet can unleash dusk's fury. (Changing Breeds, p. 85)")
                    ],
                    3: [
                        ("Perfect Twilight", "The Bastet can create perfect twilight. (Changing Breeds, p. 85)"),
                        ("Dusk's Dominion", "The Bastet gains dominion over dusk. (Changing Breeds, p. 85)")
                    ]
                },
                "Night": {
                    1: [
                        ("Night's Power", "The Bastet gains power during night. (Changing Breeds, p. 85)"),
                        ("Moon's Blessing", "The Bastet gains blessings from the moon. (Changing Breeds, p. 85)")
                    ],
                    2: [
                        ("Night's Mastery", "The Bastet gains mastery during night. (Changing Breeds, p. 85)"),
                        ("Moon's Wrath", "The Bastet can unleash the moon's fury. (Changing Breeds, p. 85)")
                    ],
                    3: [
                        ("Perfect Night", "The Bastet can create perfect night. (Changing Breeds, p. 85)"),
                        ("Moon's Dominion", "The Bastet gains dominion over the moon. (Changing Breeds, p. 85)")
                    ]
                }
            },
            "tribe": {
                "Bagheera": {
                    1: [
                        ("Jungle's Power", "The Bastet gains power in jungles. (Changing Breeds, p. 87)"),
                        ("Panther's Grace", "The Bastet gains incredible grace. (Changing Breeds, p. 87)")
                    ],
                    2: [
                        ("Jungle's Mastery", "The Bastet gains mastery of jungles. (Changing Breeds, p. 87)"),
                        ("Panther's Wrath", "The Bastet can unleash panther's fury. (Changing Breeds, p. 87)")
                    ],
                    3: [
                        ("Perfect Jungle", "The Bastet can create perfect jungles. (Changing Breeds, p. 87)"),
                        ("Panther's Dominion", "The Bastet gains dominion over panthers. (Changing Breeds, p. 87)")
                    ]
                },
                "Balam": {
                    1: [
                        ("Rainforest's Power", "The Bastet gains power in rainforests. (Changing Breeds, p. 88)"),
                        ("Jaguar's Strength", "The Bastet gains incredible strength. (Changing Breeds, p. 88)")
                    ],
                    2: [
                        ("Rainforest's Mastery", "The Bastet gains mastery of rainforests. (Changing Breeds, p. 88)"),
                        ("Jaguar's Wrath", "The Bastet can unleash jaguar's fury. (Changing Breeds, p. 88)")
                    ],
                    3: [
                        ("Perfect Rainforest", "The Bastet can create perfect rainforests. (Changing Breeds, p. 88)"),
                        ("Jaguar's Dominion", "The Bastet gains dominion over jaguars. (Changing Breeds, p. 88)")
                    ]
                },
                "Bubasti": {
                    1: [
                        ("Mystic's Power", "The Bastet gains power from mysticism. (Changing Breeds, p. 88)"),
                        ("Serval's Grace", "The Bastet gains incredible grace. (Changing Breeds, p. 88)")
                    ],
                    2: [
                        ("Mystic's Mastery", "The Bastet gains mastery of mysticism. (Changing Breeds, p. 88)"),
                        ("Serval's Wrath", "The Bastet can unleash serval's fury. (Changing Breeds, p. 88)")
                    ],
                    3: [
                        ("Perfect Mystic", "The Bastet can create perfect mysticism. (Changing Breeds, p. 88)"),
                        ("Serval's Dominion", "The Bastet gains dominion over servals. (Changing Breeds, p. 88)")
                    ]
                },
                "Ceilican": {
                    1: [
                        ("Trickster's Power", "The Bastet gains power from trickery. (Changing Breeds, p. 88)"),
                        ("Wildcat's Cunning", "The Bastet gains incredible cunning. (Changing Breeds, p. 88)")
                    ],
                    2: [
                        ("Trickster's Mastery", "The Bastet gains mastery of trickery. (Changing Breeds, p. 88)"),
                        ("Wildcat's Wrath", "The Bastet can unleash wildcat's fury. (Changing Breeds, p. 88)")
                    ],
                    3: [
                        ("Perfect Trickster", "The Bastet can create perfect trickery. (Changing Breeds, p. 88)"),
                        ("Wildcat's Dominion", "The Bastet gains dominion over wildcats. (Changing Breeds, p. 88)")
                    ]
                },
                "Khan": {
                    1: [
                        ("Tiger's Power", "The Bastet gains power from tigers. (Changing Breeds, p. 88)"),
                        ("Tiger's Strength", "The Bastet gains incredible strength. (Changing Breeds, p. 88)")
                    ],
                    2: [
                        ("Tiger's Mastery", "The Bastet gains mastery of tigers. (Changing Breeds, p. 88)"),
                        ("Tiger's Wrath", "The Bastet can unleash tiger's fury. (Changing Breeds, p. 88)")
                    ],
                    3: [
                        ("Perfect Tiger", "The Bastet can create perfect tigers. (Changing Breeds, p. 88)"),
                        ("Tiger's Dominion", "The Bastet gains dominion over tigers. (Changing Breeds, p. 88)")
                    ]
                },
                "Pumonca": {
                    1: [
                        ("Cougar's Power", "The Bastet gains power from cougars. (Changing Breeds, p. 89)"),
                        ("Cougar's Grace", "The Bastet gains incredible grace. (Changing Breeds, p. 89)")
                    ],
                    2: [
                        ("Cougar's Mastery", "The Bastet gains mastery of cougars. (Changing Breeds, p. 89)"),
                        ("Cougar's Wrath", "The Bastet can unleash cougar's fury. (Changing Breeds, p. 89)")
                    ],
                    3: [
                        ("Perfect Cougar", "The Bastet can create perfect cougars. (Changing Breeds, p. 89)"),
                        ("Cougar's Dominion", "The Bastet gains dominion over cougars. (Changing Breeds, p. 89)")
                    ]
                },
                "Qualmi": {
                    1: [
                        ("Lynx's Power", "The Bastet gains power from lynxes. (Changing Breeds, p. 89)"),
                        ("Lynx's Sight", "The Bastet gains incredible sight. (Changing Breeds, p. 89)")
                    ],
                    2: [
                        ("Lynx's Mastery", "The Bastet gains mastery of lynxes. (Changing Breeds, p. 89)"),
                        ("Lynx's Wrath", "The Bastet can unleash lynx's fury. (Changing Breeds, p. 89)")
                    ],
                    3: [
                        ("Perfect Lynx", "The Bastet can create perfect lynxes. (Changing Breeds, p. 89)"),
                        ("Lynx's Dominion", "The Bastet gains dominion over lynxes. (Changing Breeds, p. 89)")
                    ]
                },
                "Simba": {
                    1: [
                        ("Lion's Power", "The Bastet gains power from lions. (Changing Breeds, p. 90)"),
                        ("Lion's Roar", "The Bastet can roar like a lion. (Changing Breeds, p. 90)")
                    ],
                    2: [
                        ("Lion's Mastery", "The Bastet gains mastery of lions. (Changing Breeds, p. 90)"),
                        ("Lion's Wrath", "The Bastet can unleash lion's fury. (Changing Breeds, p. 90)")
                    ],
                    3: [
                        ("Perfect Lion", "The Bastet can create perfect lions. (Changing Breeds, p. 90)"),
                        ("Lion's Dominion", "The Bastet gains dominion over lions. (Changing Breeds, p. 90)")
                    ]
                },
                "Swara": {
                    1: [
                        ("Cheetah's Power", "The Bastet gains power from cheetahs. (Changing Breeds, p. 90)"),
                        ("Cheetah's Speed", "The Bastet gains incredible speed. (Changing Breeds, p. 90)")
                    ],
                    2: [
                        ("Cheetah's Mastery", "The Bastet gains mastery of cheetahs. (Changing Breeds, p. 90)"),
                        ("Cheetah's Wrath", "The Bastet can unleash cheetah's fury. (Changing Breeds, p. 90)")
                    ],
                    3: [
                        ("Perfect Cheetah", "The Bastet can create perfect cheetahs. (Changing Breeds, p. 90)"),
                        ("Cheetah's Dominion", "The Bastet gains dominion over cheetahs. (Changing Breeds, p. 90)")
                    ]
                }
            },
            "general": {
                1: [
                    ("Cat's Grace", "The Bastet gains incredible agility. (Changing Breeds, p. 85)"),
                    ("Heightened Senses", "The Bastet's senses become incredibly acute. (Changing Breeds, p. 85)"),
                    ("Sense Prey", "The Bastet can track and locate prey. (Changing Breeds, p. 85)")
                ],
                2: [
                    ("Cat's Cunning", "The Bastet gains increased intelligence. (Changing Breeds, p. 85)"),
                    ("Perfect Balance", "The Bastet can maintain perfect balance. (Changing Breeds, p. 85)")
                ],
                3: [
                    ("Cat's Power", "The Bastet gains power from cats. (Changing Breeds, p. 85)"),
                    ("Perfect Cat", "The Bastet can become a perfect cat. (Changing Breeds, p. 85)")
                ],
                4: [
                    ("Cat's Dominion", "The Bastet gains dominion over cats. (Changing Breeds, p. 85)"),
                    ("Great Cat's Call", "The Bastet can call upon great cats. (Changing Breeds, p. 85)")
                ],
                5: [
                    ("Perfect Bastet", "The Bastet becomes the perfect werecat. (Changing Breeds, p. 85)")
                ]
            }
        }
    },
    "Corax": {
        "display_name": "Corax (Wereraven)",
        "breeds": {
            "Homid": {
                "description": "Created via Rite of the Fetish Egg. Black hair, black eyes, thin build.",
                "initial_gnosis": 6,
                "initial_rage": 1,
                "initial_willpower": 3,
                "beginning_gifts": [],
                "restrictions": []
            }
        },
        "auspices": {},  # Corax don't have auspices
        "tribes": {},  # Corax don't have tribes
        "forms": {
            "Homid": {
                "description": "Human form, black hair, black eyes, thin build, ring fingers longer than middle fingers.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Ring fingers longer than middle fingers"
            },
            "Corvid": {
                "description": "Large raven form.",
                "statistics_adjustment": {
                    "Strength": -1, "Dexterity": 1, "Stamina": 0,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 4, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Large raven",
                "special": "Vulnerable to gold"
            },
            "Crinos": {
                "description": "Hybrid form with feathers, beak, wings instead of arms, clawed fingers.",
                "statistics_adjustment": {
                    "Strength": 1, "Dexterity": 1, "Stamina": 1,
                    "Charisma": 0, "Manipulation": -2, "Appearance": 0,
                    "Perception": 3, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Hybrid form",
                "special": "Can claw for aggravated damage. Vulnerable to gold"
            }
        },
        "renown_types": ["Glory", "Honor", "Wisdom"],
        "starting_traits": {
            "rage": 1,  # Fixed for all Corax
            "gnosis": 6,  # Fixed for all Corax
            "willpower": 3  # Fixed for all Corax
        },
        "gifts": {
            "breed": {},
            "auspice": {},
            "tribe": {},
            "general": {
                1: [
                    ("Enemy Ways", "The Corax can understand the weaknesses and tactics of their enemies. (Changing Breeds, p. 99)"),
                    ("Morse", "The Corax can communicate through coded messages. (Changing Breeds, p. 99)"),
                    ("Open Seal", "The Corax can unlock doors, break seals, and open any barrier. (Changing Breeds, p. 99)"),
                    ("Persuasion", "The Corax can convince others through logical argument and moral authority. (Changing Breeds, p. 99)"),
                    ("Raven's Gleaning", "The Corax can find valuable information and objects. (Changing Breeds, p. 99)"),
                    ("Scent of the True Form", "The Corax can see through illusions and disguises to perceive the true nature of things. (Changing Breeds, p. 99)"),
                    ("Spirit Speech", "The Corax can communicate with spirits in their own language. (Changing Breeds, p. 99)"),
                    ("Truth of Gaia", "The Corax can compel others to speak the truth. (Changing Breeds, p. 99)"),
                    ("Voice of the Mimic", "The Corax can perfectly mimic any voice or sound. (Changing Breeds, p. 99)"),
                    ("Word Beyond", "The Corax can send messages across great distances. (Changing Breeds, p. 99)")
                ],
                2: [
                    ("Carrion's Call", "The Corax can call upon carrion birds for aid. (Changing Breeds, p. 99)"),
                    ("Messenger's Fortitude", "The Corax can run at full speed for extended periods without rest. (Changing Breeds, p. 99)"),
                    ("Razor Feathers", "The Corax's feathers become sharp weapons. (Changing Breeds, p. 99)"),
                    ("Sky's Beneficence", "The Corax gains bonuses when flying or in the air. (Changing Breeds, p. 99)"),
                    ("Speech of the World", "The Corax can speak and understand any human language. (Changing Breeds, p. 99)"),
                    ("Swallow's Return", "The Corax can always find their way home. (Changing Breeds, p. 99)"),
                    ("Taking the Forgotten", "The Corax can steal something and make the victim forget they ever possessed it. (Changing Breeds, p. 99)"),
                    ("Whisper Catching", "The Corax can overhear conversations from great distances. (Changing Breeds, p. 99)"),
                    ("Wire Sitter", "The Corax can balance on impossibly thin surfaces. (Changing Breeds, p. 99)")
                ],
                3: [
                    ("Dead Talk", "The Corax can communicate with the dead. (Changing Breeds, p. 99)"),
                    ("Eyes of the Eagle", "The Corax can see over impossibly long distances. (Changing Breeds, p. 99)"),
                    ("Hummingbird Dart", "The Corax can move with incredible speed. (Changing Breeds, p. 99)"),
                    ("Mynah's Touch", "The Corax can perfectly copy any action they witness. (Changing Breeds, p. 99)"),
                    ("Scrying", "The Corax may view events elsewhere by staring into a reflective surface. (Changing Breeds, p. 99)"),
                    ("Sense the Unnatural", "The Corax can sense any supernatural presence and determine its type. (Changing Breeds, p. 99)"),
                    ("Sun's Guard", "The Corax gains protection from sunlight and fire. (Changing Breeds, p. 99)")
                ],
                4: [
                    ("Attunement", "The Corax can commune with spirits for information. (Changing Breeds, p. 99)"),
                    ("Airt Sense", "The Corax can sense changes in the weather and air currents. (Changing Breeds, p. 99)"),
                    ("Bloody Feather Storm", "The Corax can launch a storm of razor-sharp feathers. (Changing Breeds, p. 99)"),
                    ("Flight of Separation", "The Corax can split into multiple ravens. (Changing Breeds, p. 99)"),
                    ("Gauntlet Runner", "The Corax can easily step sideways into the Umbra. (Changing Breeds, p. 99)"),
                    ("Kiss of Helios", "The Corax gains immunity to flame and can ignite portions of their body. (Changing Breeds, p. 99)")
                ],
                5: [
                    ("Deceptive Demise", "The Corax can fake their own death. (Changing Breeds, p. 99)"),
                    ("Portents", "The Corax can see visions of the future. (Changing Breeds, p. 99)"),
                    ("Theft of Stars", "The Corax can steal light and create darkness. (Changing Breeds, p. 99)"),
                    ("Thieving Talons of the Magpie", "The Corax can steal the powers of others and use them. (Changing Breeds, p. 99)")
                ]
            }
        }
    },
    "Gurahl": {
        "display_name": "Gurahl (Werebear)",
        "breeds": {
            "Homid": {
                "description": "Born to human mothers, raised among humans.",
                "initial_gnosis": 1,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Ursine": {
                "description": "Born a bear, closest to nature.",
                "initial_gnosis": 5,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {
            "Arcas": {
                "description": "Cub stage - young and learning.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 6,
                "beginning_gifts": []
            },
            "Uzmati": {
                "description": "Adolescent stage - growing in power.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 6,
                "beginning_gifts": []
            },
            "Kojubat": {
                "description": "Adult stage - full maturity.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 6,
                "beginning_gifts": []
            },
            "Kieh": {
                "description": "Elder stage - wise and powerful.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 6,
                "beginning_gifts": []
            },
            "Rishi": {
                "description": "Ancient stage - legendary beings.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 6,
                "beginning_gifts": []
            }
        },
        "tribes": {},  # Gurahl don't have tribes
        "forms": {
            "Homid": {
                "description": "Human form, above average height/musculature.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Above average height/musculature",
                "special": "Normal human appearance"
            },
            "Arthren": {
                "description": "Near-man form (like Glabro), tall and burly.",
                "statistics_adjustment": {
                    "Strength": 3, "Dexterity": 0, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -2, "Appearance": -2,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Tall and burly",
                "special": "Near-human form"
            },
            "Crinos": {
                "description": "Fighting form, 14-16 feet tall, over 1 ton.",
                "statistics_adjustment": {
                    "Strength": 5, "Dexterity": -1, "Stamina": 5,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "14-16 feet tall, over 1 ton",
                "special": "Invokes Delirium, can only speak in harsh monosyllables"
            },
            "Bjornen": {
                "description": "Cave-bear form, four-footed.",
                "statistics_adjustment": {
                    "Strength": 4, "Dexterity": -2, "Stamina": 4,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Cave-bear size",
                "special": "Four-footed form"
            },
            "Ursus": {
                "description": "Normal bear form.",
                "statistics_adjustment": {
                    "Strength": 3, "Dexterity": 0, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal bear size",
                "special": "Normal bear form"
            }
        },
        "renown_types": ["Honor", "Succor", "Wisdom"],
        "starting_traits": {
            "rage": 0,  # Varies
            "gnosis": "by_breed",
            "willpower": 6  # Fixed for all Gurahl
        },
        "gifts": {
            "breed": {
                "Homid": {
                    1: [
                        ("Persuasion", "The Gurahl can convince others through peaceful means. (Changing Breeds, p. 116)"),
                        ("Resist Pain", "The Gurahl can ignore pain and continue fighting. (Changing Breeds, p. 116)")
                    ]
                },
                "Ursine": {
                    1: [
                        ("Heightened Senses", "The Gurahl's senses become incredibly acute. (Changing Breeds, p. 116)"),
                        ("Sense Prey", "The Gurahl can track and locate prey with supernatural accuracy. (Changing Breeds, p. 116)")
                    ]
                }
            },
            "auspice": {
                "Arcas": {
                    1: [
                        ("Cub's Play", "The Gurahl can appear harmless and innocent. (Changing Breeds, p. 116)"),
                        ("Mother's Touch", "The Gurahl can heal wounds by touch. (Changing Breeds, p. 116)")
                    ]
                },
                "Uzmati": {
                    1: [
                        ("Growing Strength", "The Gurahl gains increased physical power. (Changing Breeds, p. 117)"),
                        ("Youth's Vigor", "The Gurahl can recover from exhaustion quickly. (Changing Breeds, p. 117)")
                    ]
                },
                "Kojubat": {
                    1: [
                        ("Bear's Strength", "The Gurahl gains incredible physical might. (Changing Breeds, p. 117)"),
                        ("Protector's Duty", "The Gurahl can sense when those they protect are in danger. (Changing Breeds, p. 117)")
                    ]
                },
                "Kieh": {
                    1: [
                        ("Elder's Wisdom", "The Gurahl gains access to ancient knowledge. (Changing Breeds, p. 118)"),
                        ("Guardian's Resolve", "The Gurahl becomes unshakeable in defense. (Changing Breeds, p. 118)")
                    ]
                },
                "Rishi": {
                    1: [
                        ("Ancient Power", "The Gurahl can channel the power of ancient bears. (Changing Breeds, p. 118)"),
                        ("Legend's Might", "The Gurahl becomes a force of nature. (Changing Breeds, p. 118)")
                    ]
                }
            },
            "tribe": {},
            "general": {
                1: [
                    ("Bear's Embrace", "The Gurahl can crush enemies in a powerful hug. (Changing Breeds, p. 114)"),
                    ("Hibernation", "The Gurahl can enter a deep sleep to heal and recover. (Changing Breeds, p. 114)"),
                    ("Resist Pain", "The Gurahl can ignore pain and continue fighting. (Changing Breeds, p. 114)"),
                    ("Sense Wyrm", "The Gurahl can sense nearby manifestations of the Wyrm. (Changing Breeds, p. 114)")
                ],
                2: [
                    ("Bear's Roar", "The Gurahl's roar can stun and terrify enemies. (Changing Breeds, p. 114)"),
                    ("Mountain's Endurance", "The Gurahl gains incredible stamina. (Changing Breeds, p. 114)")
                ],
                3: [
                    ("Earth's Strength", "The Gurahl can draw power from the earth. (Changing Breeds, p. 114)"),
                    ("Guardian's Shield", "The Gurahl can protect others from harm. (Changing Breeds, p. 114)")
                ],
                4: [
                    ("Bear's Wrath", "The Gurahl becomes an unstoppable force in combat. (Changing Breeds, p. 114)"),
                    ("Mountain's Heart", "The Gurahl becomes as unshakeable as a mountain. (Changing Breeds, p. 114)")
                ],
                5: [
                    ("Great Bear's Call", "The Gurahl can summon the power of the Great Bear. (Changing Breeds, p. 114)")
                ]
            }
        }
    },
    "Kitsune": {
        "display_name": "Kitsune (Werefox)",
        "breeds": {
            "Kojin": {
                "description": "Born to human mothers, raised among humans.",
                "initial_gnosis": 1,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Roko": {
                "description": "Born a fox, closest to nature.",
                "initial_gnosis": 5,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {
            "Doshi": {
                "description": "Sorcerer path - chosen at first rank.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Eji": {
                "description": "Warrior path - chosen at first rank.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Shinju": {
                "description": "Pure Breed path - chosen at first rank.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Gukutsushi": {
                "description": "Dreamweaver path - chosen at first rank.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Kataribe": {
                "description": "Poet path - chosen at first rank.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            }
        },
        "tribes": {},  # Kitsune don't have tribes
        "forms": {
            "Hitogata": {
                "description": "Human form (Homid).",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Normal human appearance"
            },
            "Sambuhenge": {
                "description": "Near-human form (like Glabro).",
                "statistics_adjustment": {
                    "Strength": 1, "Dexterity": 1, "Stamina": 1,
                    "Charisma": 0, "Manipulation": -1, "Appearance": -1,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Larger than human",
                "special": "Shows one tail"
            },
            "Koto": {
                "description": "War form (like Crinos). Does NOT invoke Delirium.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 2, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -2, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "War form size",
                "special": "Does NOT invoke Delirium. Teeth do aggravated damage"
            },
            "Juko": {
                "description": "Large fox form (like Hispo).",
                "statistics_adjustment": {
                    "Strength": 1, "Dexterity": 3, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Large fox",
                "special": "Teeth do aggravated damage"
            },
            "Kyubi": {
                "description": "Normal fox form.",
                "statistics_adjustment": {
                    "Strength": -1, "Dexterity": 3, "Stamina": 1,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal fox size",
                "special": "Normal fox form"
            }
        },
        "renown_types": ["Chie", "Toku", "Kagayaki"],
        "starting_traits": {
            "rage": 0,  # Varies
            "gnosis": "by_breed",
            "willpower": 0  # Varies
        },
        "gifts": {
            "breed": {
                "Kojin": {
                    1: [
                        ("Fox's Cunning", "The Kitsune gains increased intelligence and wit. (Changing Breeds, p. 131)"),
                        ("Smell of Man", "The Kitsune can blend into human society. (Changing Breeds, p. 131)")
                    ]
                },
                "Roko": {
                    1: [
                        ("Fox's Grace", "The Kitsune gains incredible agility. (Changing Breeds, p. 131)"),
                        ("Sense Prey", "The Kitsune can track and locate prey with supernatural accuracy. (Changing Breeds, p. 131)")
                    ]
                }
            },
            "auspice": {
                "Doshi": {
                    1: [
                        ("Elemental Gift", "The Kitsune can command elemental forces. (Changing Breeds, p. 132)"),
                        ("Spirit Speech", "The Kitsune can communicate with spirits. (Changing Breeds, p. 132)")
                    ],
                    2: [
                        ("Spirit Ward", "The Kitsune can protect themselves from spirits. (Changing Breeds, p. 132)"),
                        ("Umbral Tether", "The Kitsune can create connections to the Umbra. (Changing Breeds, p. 132)")
                    ],
                    3: [
                        ("Command Spirit", "The Kitsune can give commands to spirits. (Changing Breeds, p. 132)"),
                        ("Exorcism", "The Kitsune can eject spirits from places or people. (Changing Breeds, p. 132)")
                    ],
                    4: [
                        ("Spirit Drain", "The Kitsune can drain power from spirits. (Changing Breeds, p. 132)"),
                        ("Summon Elemental", "The Kitsune can call upon elementals for aid. (Changing Breeds, p. 132)")
                    ],
                    5: [
                        ("Master of Elements", "The Kitsune gains mastery over all elements. (Changing Breeds, p. 132)")
                    ]
                },
                "Eji": {
                    1: [
                        ("Falling Touch", "The Kitsune's touch can cause enemies to fall. (Changing Breeds, p. 133)"),
                        ("Razor Claws", "The Kitsune's claws become incredibly sharp. (Changing Breeds, p. 133)")
                    ],
                    2: [
                        ("Pack Tactics", "The Kitsune can coordinate pack attacks. (Changing Breeds, p. 133)"),
                        ("True Fear", "The Kitsune can inspire supernatural fear. (Changing Breeds, p. 133)")
                    ],
                    3: [
                        ("Combat Healing", "The Kitsune can mend injuries in combat. (Changing Breeds, p. 133)"),
                        ("Silver Claws", "The Kitsune's claws transform into silver. (Changing Breeds, p. 133)")
                    ],
                    4: [
                        ("Body Shift", "The Kitsune can shift physical Attribute dots. (Changing Breeds, p. 133)"),
                        ("Stoking Fury's Furnace", "The Kitsune regains Rage when taking damage. (Changing Breeds, p. 133)")
                    ],
                    5: [
                        ("Unstoppable Warrior", "The Kitsune becomes an unstoppable force. (Changing Breeds, p. 133)")
                    ]
                },
                "Shinju": {
                    1: [
                        ("Pure Breed", "The Kitsune gains bonuses from their pure lineage. (Changing Breeds, p. 132)"),
                        ("Ancestral Memory", "The Kitsune can access memories of their ancestors. (Changing Breeds, p. 132)")
                    ],
                    2: [
                        ("Lineage's Power", "The Kitsune can channel their bloodline's power. (Changing Breeds, p. 132)"),
                        ("Noble Bearing", "The Kitsune radiates authority and nobility. (Changing Breeds, p. 132)")
                    ],
                    3: [
                        ("Ancestral Guidance", "The Kitsune can call upon ancestors for aid. (Changing Breeds, p. 132)"),
                        ("Bloodline's Blessing", "The Kitsune gains power from their lineage. (Changing Breeds, p. 132)")
                    ],
                    4: [
                        ("Great Ancestor's Call", "The Kitsune can summon a great ancestor. (Changing Breeds, p. 132)"),
                        ("Perfect Lineage", "The Kitsune becomes the embodiment of their bloodline. (Changing Breeds, p. 132)")
                    ],
                    5: [
                        ("Divine Ancestry", "The Kitsune can channel divine power. (Changing Breeds, p. 132)")
                    ]
                },
                "Gukutsushi": {
                    1: [
                        ("Dreamspeak", "The Kitsune can walk among another's dreams. (Changing Breeds, p. 134)"),
                        ("Gift of Dreams", "The Kitsune can craft and breathe dreams. (Changing Breeds, p. 134)")
                    ],
                    2: [
                        ("Dream Walker", "The Kitsune can travel through dreams. (Changing Breeds, p. 134)"),
                        ("Nightmare's Touch", "The Kitsune can create nightmares. (Changing Breeds, p. 134)")
                    ],
                    3: [
                        ("Dream Mastery", "The Kitsune gains control over dreams. (Changing Breeds, p. 134)"),
                        ("Reality's Veil", "The Kitsune can blur the line between dream and reality. (Changing Breeds, p. 134)")
                    ],
                    4: [
                        ("Dream Realm", "The Kitsune can create a realm of dreams. (Changing Breeds, p. 134)"),
                        ("Eternal Dream", "The Kitsune can trap others in eternal dreams. (Changing Breeds, p. 134)")
                    ],
                    5: [
                        ("Master of Dreams", "The Kitsune becomes a master of the dream realm. (Changing Breeds, p. 134)")
                    ]
                },
                "Kataribe": {
                    1: [
                        ("Call of the Wyld", "The Kitsune can inspire others through song and story. (Changing Breeds, p. 134)"),
                        ("Perfect Recall", "The Kitsune can remember events with perfect clarity. (Changing Breeds, p. 134)")
                    ],
                    2: [
                        ("Song of Heroes", "The Kitsune conjures the spirit of fallen heroes. (Changing Breeds, p. 134)"),
                        ("Storyteller's Gift", "The Kitsune can make stories come to life. (Changing Breeds, p. 134)")
                    ],
                    3: [
                        ("Epic Tale", "The Kitsune can create epic stories that inspire. (Changing Breeds, p. 134)"),
                        ("Legend's Voice", "The Kitsune can speak with the voice of legends. (Changing Breeds, p. 134)")
                    ],
                    4: [
                        ("Myth's Power", "The Kitsune can channel the power of myths. (Changing Breeds, p. 134)"),
                        ("Saga's End", "The Kitsune can end stories with powerful conclusions. (Changing Breeds, p. 134)")
                    ],
                    5: [
                        ("Master Storyteller", "The Kitsune becomes a master of stories and legends. (Changing Breeds, p. 134)")
                    ]
                }
            },
            "tribe": {},
            "general": {
                1: [
                    ("Balance", "The Kitsune can maintain perfect balance. (Changing Breeds, p. 130)"),
                    ("Blur of the Milky Eye", "The Kitsune can become partially invisible. (Changing Breeds, p. 130)"),
                    ("Heightened Senses", "The Kitsune's senses become incredibly acute. (Changing Breeds, p. 130)"),
                    ("Open Seal", "The Kitsune can unlock doors and break seals. (Changing Breeds, p. 130)")
                ],
                2: [
                    ("Fox's Cunning", "The Kitsune gains increased intelligence and wit. (Changing Breeds, p. 130)"),
                    ("Scent of Running Water", "The Kitsune can mask their scent. (Changing Breeds, p. 130)")
                ],
                3: [
                    ("Thousand Forms", "The Kitsune can change into any animal. (Changing Breeds, p. 130)"),
                    ("Wisdom of the Ancient", "The Kitsune can access ancient knowledge. (Changing Breeds, p. 130)")
                ],
                4: [
                    ("Fox's Illusion", "The Kitsune can create powerful illusions. (Changing Breeds, p. 130)"),
                    ("Nine-Tailed Power", "The Kitsune can manifest additional tails for power. (Changing Breeds, p. 130)")
                ],
                5: [
                    ("Divine Fox", "The Kitsune becomes a divine being. (Changing Breeds, p. 130)")
                ]
            }
        }
    },
    "Mokolé": {
        "display_name": "Mokolé (Werelizard)",
        "breeds": {
            "Homid": {
                "description": "Born to human mothers, raised among humans.",
                "initial_gnosis": 1,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Suchid": {
                "description": "Born a reptile, closest to nature.",
                "initial_gnosis": 5,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {
            "Rising Sun": {
                "description": "Striking auspice - warriors and hunters.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Noonday Sun": {
                "description": "Unshading auspice - judges and mediators.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Setting Sun": {
                "description": "Warding auspice - protectors and guardians.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Midnight Sun": {
                "description": "Shining auspice - mystics and seers.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Shrouded Sun": {
                "description": "Concealing auspice - tricksters and scouts.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Decorated Sun": {
                "description": "Gathering auspice - storytellers and leaders.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Eclipsed Sun": {
                "description": "Crowning auspice - elders and legends.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            }
        },
        "tribes": {},  # Mokolé don't have tribes, they have streams/varnas
        "forms": {
            "Homid": {
                "description": "Human form.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Normal human appearance"
            },
            "Archid": {
                "description": "Draconic form. Causes Delirium, bite/claw for aggravated (Str +2).",
                "statistics_adjustment": {
                    "Strength": 4, "Dexterity": -1, "Stamina": 4,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Draconic size",
                "special": "Causes Delirium, bite/claw for aggravated (Str +2). Can purchase Archid Characteristics equal to Gnosis"
            },
            "Suchid": {
                "description": "Reptilian form. Statistics vary by varna/stream.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 1, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -2, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Reptilian size",
                "special": "Statistics vary by varna/stream"
            }
        },
        "renown_types": ["Glory", "Honor", "Wisdom"],  # Varies by stream
        "starting_traits": {
            "rage": 0,
            "gnosis": "by_breed",
            "willpower": 0
        },
        "gifts": {
            "breed": {
                "Homid": {
                    1: [
                        ("Sun's Touch", "The Mokolé can channel solar power. (Changing Breeds, p. 148)"),
                        ("Resist Pain", "The Mokolé can ignore pain. (Changing Breeds, p. 148)")
                    ]
                },
                "Suchid": {
                    1: [
                        ("Reptile's Cunning", "The Mokolé gains increased intelligence. (Changing Breeds, p. 148)"),
                        ("Scale Armor", "The Mokolé's scales provide protection. (Changing Breeds, p. 148)")
                    ]
                }
            },
            "auspice": {
                "Rising Sun": {
                    1: [
                        ("Striking Blow", "The Mokolé can deliver devastating attacks. (Changing Breeds, p. 148)"),
                        ("Dawn's Power", "The Mokolé gains power at sunrise. (Changing Breeds, p. 148)")
                    ],
                    2: [
                        ("Solar Strike", "The Mokolé can channel solar energy in attacks. (Changing Breeds, p. 148)"),
                        ("Rising Strength", "The Mokolé gains strength as the sun rises. (Changing Breeds, p. 148)")
                    ],
                    3: [
                        ("Sun's Wrath", "The Mokolé can unleash solar fury. (Changing Breeds, p. 148)"),
                        ("Dawn's Champion", "The Mokolé becomes a champion of the dawn. (Changing Breeds, p. 148)")
                    ],
                    4: [
                        ("Solar Mastery", "The Mokolé gains mastery over solar power. (Changing Breeds, p. 148)"),
                        ("Rising God", "The Mokolé becomes a god of the rising sun. (Changing Breeds, p. 148)")
                    ],
                    5: [
                        ("Perfect Dawn", "The Mokolé becomes the embodiment of dawn. (Changing Breeds, p. 148)")
                    ]
                },
                "Noonday Sun": {
                    1: [
                        ("Unshading Truth", "The Mokolé can see through all lies. (Changing Breeds, p. 149)"),
                        ("Noon's Clarity", "The Mokolé gains perfect clarity. (Changing Breeds, p. 149)")
                    ],
                    2: [
                        ("Solar Judgment", "The Mokolé can judge with solar authority. (Changing Breeds, p. 149)"),
                        ("Noon's Power", "The Mokolé gains power at noon. (Changing Breeds, p. 149)")
                    ],
                    3: [
                        ("Perfect Truth", "The Mokolé can reveal absolute truth. (Changing Breeds, p. 149)"),
                        ("Noon's Mastery", "The Mokolé gains mastery at noon. (Changing Breeds, p. 149)")
                    ],
                    4: [
                        ("Solar Authority", "The Mokolé gains absolute authority. (Changing Breeds, p. 149)"),
                        ("Noon's God", "The Mokolé becomes a god of noon. (Changing Breeds, p. 149)")
                    ],
                    5: [
                        ("Perfect Noon", "The Mokolé becomes the embodiment of noon. (Changing Breeds, p. 149)")
                    ]
                },
                "Setting Sun": {
                    1: [
                        ("Warding Shield", "The Mokolé can create protective barriers. (Changing Breeds, p. 149)"),
                        ("Dusk's Protection", "The Mokolé gains protection at sunset. (Changing Breeds, p. 149)")
                    ],
                    2: [
                        ("Solar Ward", "The Mokolé can ward against enemies. (Changing Breeds, p. 149)"),
                        ("Setting Power", "The Mokolé gains power at sunset. (Changing Breeds, p. 149)")
                    ],
                    3: [
                        ("Perfect Ward", "The Mokolé can create perfect defenses. (Changing Breeds, p. 149)"),
                        ("Dusk's Mastery", "The Mokolé gains mastery at sunset. (Changing Breeds, p. 149)")
                    ],
                    4: [
                        ("Solar Fortress", "The Mokolé can create impenetrable defenses. (Changing Breeds, p. 149)"),
                        ("Setting God", "The Mokolé becomes a god of sunset. (Changing Breeds, p. 149)")
                    ],
                    5: [
                        ("Perfect Dusk", "The Mokolé becomes the embodiment of dusk. (Changing Breeds, p. 149)")
                    ]
                },
                "Midnight Sun": {
                    1: [
                        ("Shining Light", "The Mokolé can create brilliant light. (Changing Breeds, p. 149)"),
                        ("Midnight's Power", "The Mokolé gains power at midnight. (Changing Breeds, p. 149)")
                    ],
                    2: [
                        ("Solar Radiance", "The Mokolé radiates solar energy. (Changing Breeds, p. 149)"),
                        ("Shining Mastery", "The Mokolé gains mastery of light. (Changing Breeds, p. 149)")
                    ],
                    3: [
                        ("Perfect Light", "The Mokolé can create perfect illumination. (Changing Breeds, p. 149)"),
                        ("Midnight's Mastery", "The Mokolé gains mastery at midnight. (Changing Breeds, p. 149)")
                    ],
                    4: [
                        ("Solar Brilliance", "The Mokolé becomes a source of brilliant light. (Changing Breeds, p. 149)"),
                        ("Shining God", "The Mokolé becomes a god of light. (Changing Breeds, p. 149)")
                    ],
                    5: [
                        ("Perfect Midnight", "The Mokolé becomes the embodiment of midnight sun. (Changing Breeds, p. 149)")
                    ]
                },
                "Shrouded Sun": {
                    1: [
                        ("Concealing Shadow", "The Mokolé can hide in shadows. (Changing Breeds, p. 150)"),
                        ("Shrouded Power", "The Mokolé gains power from concealment. (Changing Breeds, p. 150)")
                    ],
                    2: [
                        ("Solar Stealth", "The Mokolé can move unseen. (Changing Breeds, p. 150)"),
                        ("Shadow Mastery", "The Mokolé gains mastery of shadows. (Changing Breeds, p. 150)")
                    ],
                    3: [
                        ("Perfect Concealment", "The Mokolé can become completely invisible. (Changing Breeds, p. 150)"),
                        ("Shrouded Mastery", "The Mokolé gains mastery of concealment. (Changing Breeds, p. 150)")
                    ],
                    4: [
                        ("Solar Shadow", "The Mokolé can create shadows of solar power. (Changing Breeds, p. 150)"),
                        ("Shrouded God", "The Mokolé becomes a god of concealment. (Changing Breeds, p. 150)")
                    ],
                    5: [
                        ("Perfect Shroud", "The Mokolé becomes the embodiment of concealment. (Changing Breeds, p. 150)")
                    ]
                },
                "Decorated Sun": {
                    1: [
                        ("Gathering Call", "The Mokolé can call others to gather. (Changing Breeds, p. 150)"),
                        ("Decorated Power", "The Mokolé gains power from gatherings. (Changing Breeds, p. 150)")
                    ],
                    2: [
                        ("Solar Gathering", "The Mokolé can gather allies with solar power. (Changing Breeds, p. 150)"),
                        ("Gathering Mastery", "The Mokolé gains mastery of gatherings. (Changing Breeds, p. 150)")
                    ],
                    3: [
                        ("Perfect Gathering", "The Mokolé can create perfect gatherings. (Changing Breeds, p. 150)"),
                        ("Decorated Mastery", "The Mokolé gains mastery of decoration. (Changing Breeds, p. 150)")
                    ],
                    4: [
                        ("Solar Assembly", "The Mokolé can assemble great gatherings. (Changing Breeds, p. 150)"),
                        ("Decorated God", "The Mokolé becomes a god of gatherings. (Changing Breeds, p. 150)")
                    ],
                    5: [
                        ("Perfect Decoration", "The Mokolé becomes the embodiment of gatherings. (Changing Breeds, p. 150)")
                    ]
                },
                "Eclipsed Sun": {
                    1: [
                        ("Crowning Authority", "The Mokolé gains authority over others. (Changing Breeds, p. 151)"),
                        ("Eclipse Power", "The Mokolé gains power during eclipses. (Changing Breeds, p. 151)")
                    ],
                    2: [
                        ("Solar Crown", "The Mokolé can crown themselves with solar power. (Changing Breeds, p. 151)"),
                        ("Crowning Mastery", "The Mokolé gains mastery of authority. (Changing Breeds, p. 151)")
                    ],
                    3: [
                        ("Perfect Crown", "The Mokolé can create perfect authority. (Changing Breeds, p. 151)"),
                        ("Eclipse Mastery", "The Mokolé gains mastery during eclipses. (Changing Breeds, p. 151)")
                    ],
                    4: [
                        ("Solar Dominion", "The Mokolé gains dominion over all. (Changing Breeds, p. 151)"),
                        ("Eclipsed God", "The Mokolé becomes a god of eclipses. (Changing Breeds, p. 151)")
                    ],
                    5: [
                        ("Perfect Eclipse", "The Mokolé becomes the embodiment of eclipses. (Changing Breeds, p. 151)")
                    ]
                }
            },
            "tribe": {},
            "general": {
                1: [
                    ("Dragon's Breath", "The Mokolé can breathe fire or other elements. (Changing Breeds, p. 148)"),
                    ("Scale Armor", "The Mokolé's scales provide protection. (Changing Breeds, p. 148)"),
                    ("Sense Wyrm", "The Mokolé can sense nearby manifestations of the Wyrm. (Changing Breeds, p. 148)")
                ],
                2: [
                    ("Dragon's Claw", "The Mokolé's claws become incredibly sharp. (Changing Breeds, p. 148)"),
                    ("Reptile's Cunning", "The Mokolé gains increased intelligence. (Changing Breeds, p. 148)")
                ],
                3: [
                    ("Dragon's Roar", "The Mokolé's roar can stun enemies. (Changing Breeds, p. 148)"),
                    ("Scale Shield", "The Mokolé can create protective scales. (Changing Breeds, p. 148)")
                ],
                4: [
                    ("Dragon's Flight", "The Mokolé can fly. (Changing Breeds, p. 148)"),
                    ("Great Dragon's Power", "The Mokolé can channel the power of great dragons. (Changing Breeds, p. 148)")
                ],
                5: [
                    ("Perfect Dragon", "The Mokolé becomes a perfect dragon. (Changing Breeds, p. 148)")
                ]
            }
        }
    },
    "Nagah": {
        "display_name": "Nagah (Weresnake)",
        "breeds": {
            "Balaram": {
                "description": "Born to human mothers, raised among humans.",
                "initial_gnosis": 1,
                "initial_willpower": 4,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Ahi": {
                "description": "Metis Nagah, born in Azhi Dahaka form, cannot shapeshift for first few years.",
                "initial_gnosis": 3,
                "initial_willpower": 4,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Vasuki": {
                "description": "Born a snake, closest to nature.",
                "initial_gnosis": 5,
                "initial_willpower": 4,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {
            "Kamakshi": {
                "description": "Spring auspice - determined by season of First Change.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 4,
                "beginning_gifts": []
            },
            "Kartikeya": {
                "description": "Summer auspice - determined by season of First Change.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 4,
                "beginning_gifts": []
            },
            "Kamsa": {
                "description": "Autumn auspice - determined by season of First Change.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 4,
                "beginning_gifts": []
            },
            "Kali": {
                "description": "Winter auspice - determined by season of First Change.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 4,
                "beginning_gifts": []
            }
        },
        "tribes": {},  # Nagah don't have tribes
        "forms": {
            "Balaram": {
                "description": "Human form.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Normal human appearance"
            },
            "Silkaram": {
                "description": "Scaled humanoid form.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 0, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -2, "Appearance": -2,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Scaled humanoid",
                "special": "Claws do Str +0 lethal damage"
            },
            "Azhi Dahaka": {
                "description": "Serpentine battle form, up to 25 feet, upright posture.",
                "statistics_adjustment": {
                    "Strength": 3, "Dexterity": 2, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Up to 25 feet",
                "special": "Flexible arms with clawed hands (Str +1 aggravated). Can manifest hood like cobras"
            },
            "Kali Dahaka": {
                "description": "Huge snake form, up to 30 feet.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 2, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Up to 30 feet",
                "special": "Has gills, can breathe water"
            },
            "Vasuki": {
                "description": "Large poisonous snake form.",
                "statistics_adjustment": {
                    "Strength": -1, "Dexterity": 2, "Stamina": 1,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Large snake",
                "special": "Poisonous snake form"
            }
        },
        "renown_types": ["Glory", "Honor", "Wisdom"],  # Determined by Sesha
        "starting_traits": {
            "rage": 0,
            "gnosis": "by_breed",
            "willpower": 4  # Fixed for all Nagah
        },
        "gifts": {
            "breed": {
                "Balaram": {
                    1: [
                        ("Serpent's Cunning", "The Nagah gains increased intelligence. (Changing Breeds, p. 160)"),
                        ("Smell of Man", "The Nagah can blend into human society. (Changing Breeds, p. 160)")
                    ]
                },
                "Ahi": {
                    1: [
                        ("Metis Power", "The Nagah gains power from their metis nature. (Changing Breeds, p. 161)"),
                        ("Serpent's Strength", "The Nagah gains increased physical power. (Changing Breeds, p. 161)")
                    ]
                },
                "Vasuki": {
                    1: [
                        ("Serpent's Grace", "The Nagah gains incredible agility. (Changing Breeds, p. 161)"),
                        ("Venom's Touch", "The Nagah can inject venom. (Changing Breeds, p. 161)")
                    ]
                }
            },
            "auspice": {
                "Kamakshi": {
                    1: [
                        ("Spring's Renewal", "The Nagah can heal and restore. (Changing Breeds, p. 162)"),
                        ("Growth's Power", "The Nagah gains power from growth. (Changing Breeds, p. 162)")
                    ],
                    2: [
                        ("Spring's Blessing", "The Nagah can bless with spring's power. (Changing Breeds, p. 162)"),
                        ("Renewal's Mastery", "The Nagah gains mastery of renewal. (Changing Breeds, p. 162)")
                    ],
                    3: [
                        ("Perfect Renewal", "The Nagah can perfectly renew. (Changing Breeds, p. 162)"),
                        ("Spring's Mastery", "The Nagah gains mastery of spring. (Changing Breeds, p. 162)")
                    ],
                    4: [
                        ("Spring's Dominion", "The Nagah gains dominion over spring. (Changing Breeds, p. 162)"),
                        ("Renewal's God", "The Nagah becomes a god of renewal. (Changing Breeds, p. 162)")
                    ],
                    5: [
                        ("Perfect Spring", "The Nagah becomes the embodiment of spring. (Changing Breeds, p. 162)")
                    ]
                },
                "Kartikeya": {
                    1: [
                        ("Summer's Fire", "The Nagah can channel summer's heat. (Changing Breeds, p. 163)"),
                        ("Growth's Power", "The Nagah gains power from summer growth. (Changing Breeds, p. 163)")
                    ],
                    2: [
                        ("Summer's Wrath", "The Nagah can unleash summer's fury. (Changing Breeds, p. 163)"),
                        ("Fire's Mastery", "The Nagah gains mastery of fire. (Changing Breeds, p. 163)")
                    ],
                    3: [
                        ("Perfect Summer", "The Nagah can create perfect summer. (Changing Breeds, p. 163)"),
                        ("Summer's Mastery", "The Nagah gains mastery of summer. (Changing Breeds, p. 163)")
                    ],
                    4: [
                        ("Summer's Dominion", "The Nagah gains dominion over summer. (Changing Breeds, p. 163)"),
                        ("Fire's God", "The Nagah becomes a god of fire. (Changing Breeds, p. 163)")
                    ],
                    5: [
                        ("Perfect Summer", "The Nagah becomes the embodiment of summer. (Changing Breeds, p. 163)")
                    ]
                },
                "Kamsa": {
                    1: [
                        ("Autumn's Harvest", "The Nagah can harvest power. (Changing Breeds, p. 163)"),
                        ("Decay's Power", "The Nagah gains power from decay. (Changing Breeds, p. 163)")
                    ],
                    2: [
                        ("Autumn's Bounty", "The Nagah can create abundance. (Changing Breeds, p. 163)"),
                        ("Harvest's Mastery", "The Nagah gains mastery of harvest. (Changing Breeds, p. 163)")
                    ],
                    3: [
                        ("Perfect Harvest", "The Nagah can create perfect harvests. (Changing Breeds, p. 163)"),
                        ("Autumn's Mastery", "The Nagah gains mastery of autumn. (Changing Breeds, p. 163)")
                    ],
                    4: [
                        ("Autumn's Dominion", "The Nagah gains dominion over autumn. (Changing Breeds, p. 163)"),
                        ("Harvest's God", "The Nagah becomes a god of harvest. (Changing Breeds, p. 163)")
                    ],
                    5: [
                        ("Perfect Autumn", "The Nagah becomes the embodiment of autumn. (Changing Breeds, p. 163)")
                    ]
                },
                "Kali": {
                    1: [
                        ("Winter's Cold", "The Nagah can channel winter's chill. (Changing Breeds, p. 163)"),
                        ("Death's Power", "The Nagah gains power from death. (Changing Breeds, p. 163)")
                    ],
                    2: [
                        ("Winter's Wrath", "The Nagah can unleash winter's fury. (Changing Breeds, p. 163)"),
                        ("Cold's Mastery", "The Nagah gains mastery of cold. (Changing Breeds, p. 163)")
                    ],
                    3: [
                        ("Perfect Winter", "The Nagah can create perfect winter. (Changing Breeds, p. 163)"),
                        ("Winter's Mastery", "The Nagah gains mastery of winter. (Changing Breeds, p. 163)")
                    ],
                    4: [
                        ("Winter's Dominion", "The Nagah gains dominion over winter. (Changing Breeds, p. 163)"),
                        ("Death's God", "The Nagah becomes a god of death. (Changing Breeds, p. 163)")
                    ],
                    5: [
                        ("Perfect Winter", "The Nagah becomes the embodiment of winter. (Changing Breeds, p. 163)")
                    ]
                }
            },
            "tribe": {},
            "general": {
                1: [
                    ("Serpent's Bite", "The Nagah's bite becomes incredibly deadly. (Changing Breeds, p. 160)"),
                    ("Venom's Touch", "The Nagah can inject deadly venom. (Changing Breeds, p. 160)"),
                    ("Sense Wyrm", "The Nagah can sense nearby manifestations of the Wyrm. (Changing Breeds, p. 160)")
                ],
                2: [
                    ("Serpent's Coil", "The Nagah can constrict enemies. (Changing Breeds, p. 160)"),
                    ("Venom's Mastery", "The Nagah gains mastery of venom. (Changing Breeds, p. 160)")
                ],
                3: [
                    ("Serpent's Hypnosis", "The Nagah can hypnotize enemies. (Changing Breeds, p. 160)"),
                    ("Perfect Venom", "The Nagah can create perfect venom. (Changing Breeds, p. 160)")
                ],
                4: [
                    ("Serpent's Dominion", "The Nagah gains dominion over serpents. (Changing Breeds, p. 160)"),
                    ("Venom's God", "The Nagah becomes a god of venom. (Changing Breeds, p. 160)")
                ],
                5: [
                    ("Perfect Serpent", "The Nagah becomes the perfect serpent. (Changing Breeds, p. 160)")
                ]
            }
        }
    },
    "Nuwisha": {
        "display_name": "Nuwisha (Werecoyote)",
        "breeds": {
            "Homid": {
                "description": "Born to human mothers, raised among humans.",
                "initial_gnosis": 1,
                "initial_willpower": 4,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Latrani": {
                "description": "Born a coyote, closest to nature.",
                "initial_gnosis": 5,
                "initial_willpower": 4,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {},  # Nuwisha don't have auspices (Luna sees them all as Ragabash)
        "tribes": {},  # Nuwisha don't have tribes
        "forms": {
            "Homid": {
                "description": "Human form, often scrawny and trail-worn.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Often scrawny and trail-worn"
            },
            "Tsitsu": {
                "description": "Near-man form (like Glabro).",
                "statistics_adjustment": {
                    "Strength": 1, "Dexterity": 1, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -1, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Larger than human",
                "special": "Near-human form"
            },
            "Manabozho": {
                "description": "War form (like Crinos). Almost 8 feet tall, 2.5x Homid mass.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 3, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -2, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Almost 8 feet tall, 2.5x Homid mass",
                "special": "Reduced Delirium (treat Willpower as +2 higher)"
            },
            "Sendeh": {
                "description": "Red wolf-like form.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 3, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Red wolf size",
                "special": "Cannot speak but can mimic sounds"
            },
            "Latrani": {
                "description": "Normal coyote form.",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 3, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal coyote size",
                "special": "Normal coyote form"
            }
        },
        "renown_types": ["Glory", "Wisdom", "Humor"],
        "starting_traits": {
            "rage": 0,  # Nuwisha normally have NO Rage
            "gnosis": "by_breed",
            "willpower": 4  # Fixed for all Nuwisha
        },
        "gifts": {
            "breed": {
                "Homid": {
                    1: [
                        ("Coyote's Cunning", "The Nuwisha gains increased intelligence and wit. (Changing Breeds, p. 172)"),
                        ("Trickster's Gift", "The Nuwisha can play tricks on others. (Changing Breeds, p. 172)")
                    ]
                },
                "Latrani": {
                    1: [
                        ("Coyote's Grace", "The Nuwisha gains incredible agility. (Changing Breeds, p. 172)"),
                        ("Pack Tactics", "The Nuwisha can coordinate pack attacks. (Changing Breeds, p. 172)")
                    ]
                }
            },
            "auspice": {},
            "tribe": {},
            "general": {
                1: [
                    ("Blur of the Milky Eye", "The Nuwisha can become partially invisible. (Changing Breeds, p. 171)"),
                    ("Infectious Laughter", "The Nuwisha can cause others to laugh uncontrollably. (Changing Breeds, p. 171)"),
                    ("Open Seal", "The Nuwisha can unlock doors and break seals. (Changing Breeds, p. 171)"),
                    ("Scent of Running Water", "The Nuwisha can mask their scent. (Changing Breeds, p. 171)")
                ],
                2: [
                    ("Blissful Ignorance", "The Nuwisha can become completely invisible. (Changing Breeds, p. 171)"),
                    ("Pulse of the Prey", "The Nuwisha can track any target. (Changing Breeds, p. 171)"),
                    ("Taking the Forgotten", "The Nuwisha can steal and make victims forget. (Changing Breeds, p. 171)")
                ],
                3: [
                    ("Gremlins", "The Nuwisha can cause technology to malfunction. (Changing Breeds, p. 171)"),
                    ("Liar's Craft", "The Nuwisha can tell outrageous lies. (Changing Breeds, p. 171)"),
                    ("Pathfinder", "The Nuwisha can find the fastest routes. (Changing Breeds, p. 171)")
                ],
                4: [
                    ("Luna's Blessing", "The Nuwisha gains protection from silver. (Changing Breeds, p. 171)"),
                    ("Umbral Dodge", "The Nuwisha can dodge by entering the Umbra. (Changing Breeds, p. 171)")
                ],
                5: [
                    ("Thieving Talons of the Magpie", "The Nuwisha can steal powers from others. (Changing Breeds, p. 171)"),
                    ("Thousand Forms", "The Nuwisha can change into any animal. (Changing Breeds, p. 171)")
                ],
                6: [
                    ("Firebringer", "The Nuwisha can steal powers and bestow them. (Changing Breeds, p. 171)")
                ]
            },
            "umbral_danser": {
                1: [
                    ("Umbral Dance", "The Nuwisha can dance through the Umbra. (Changing Breeds, p. 173)"),
                    ("Spirit's Call", "The Nuwisha can call upon spirits. (Changing Breeds, p. 173)")
                ],
                2: [
                    ("Umbral Mastery", "The Nuwisha gains mastery of the Umbra. (Changing Breeds, p. 173)"),
                    ("Spirit's Power", "The Nuwisha can channel spirit power. (Changing Breeds, p. 173)")
                ],
                3: [
                    ("Perfect Dance", "The Nuwisha can create perfect dances. (Changing Breeds, p. 173)"),
                    ("Umbral God", "The Nuwisha becomes a god of the Umbra. (Changing Breeds, p. 173)")
                ]
            }
        }
    },
    "Ratkin": {
        "display_name": "Ratkin (Wererat)",
        "breeds": {
            "Homid": {
                "description": "Born to human mothers, raised among humans.",
                "initial_gnosis": 1,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Metis": {
                "description": "Born to two Ratkin who broke the Litany.",
                "initial_gnosis": 3,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Rodens": {
                "description": "Born a rat, closest to the tunnels.",
                "initial_gnosis": 5,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {
            "Tunnel Runner": {
                "description": "Scouts and messengers.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Shadow Seer": {
                "description": "Mystics and seers.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Knife Skulker": {
                "description": "Assassins and killers.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Blade Slave": {
                "description": "Warriors and fighters.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Ratkin Engineer": {
                "description": "Builders and technicians.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Plague Lord": {
                "description": "Disease carriers and spreaders.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Munchmausen": {
                "description": "Tricksters and liars.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            },
            "Twitcher": {
                "description": "Mad and unstable.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 0,
                "beginning_gifts": []
            }
        },
        "tribes": {},  # Ratkin don't have tribes
        "forms": {
            "Homid": {
                "description": "Human form, often dirty/unkempt/scarred.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Often dirty/unkempt/scarred"
            },
            "Crinos": {
                "description": "Humanoid rat, 15% larger, few inches taller.",
                "statistics_adjustment": {
                    "Strength": 1, "Dexterity": 4, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -2, "Appearance": -1,
                    "Perception": 1, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "15% larger, few inches taller",
                "special": "Bite does aggravated, claws do lethal. Can use prehensile tail. Reduced Delirium (treat Willpower as +2 higher)"
            },
            "Rodens": {
                "description": "Rat form, slightly larger to housecat-sized.",
                "statistics_adjustment": {
                    "Strength": -1, "Dexterity": 2, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -3, "Appearance": 0,
                    "Perception": 3, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Slightly larger to housecat-sized",
                "special": "Front paws have opposable thumbs"
            }
        },
        "renown_types": ["Infamy", "Obligation", "Cunning"],
        "starting_traits": {
            "rage": 0,
            "gnosis": "by_breed",
            "willpower": 0
        },
        "gifts": {
            "breed": {
                "Homid": {
                    1: [
                        ("Rat's Cunning", "The Ratkin gains increased intelligence. (Changing Breeds, p. 186)"),
                        ("Smell of Man", "The Ratkin can blend into human society. (Changing Breeds, p. 186)")
                    ]
                },
                "Metis": {
                    1: [
                        ("Metis Power", "The Ratkin gains power from their metis nature. (Changing Breeds, p. 187)"),
                        ("Rat's Strength", "The Ratkin gains increased physical power. (Changing Breeds, p. 187)")
                    ]
                },
                "Rodens": {
                    1: [
                        ("Rat's Grace", "The Ratkin gains incredible agility. (Changing Breeds, p. 187)"),
                        ("Tunnel Sense", "The Ratkin can navigate tunnels perfectly. (Changing Breeds, p. 187)")
                    ]
                }
            },
            "auspice": {
                "Tunnel Runner": {
                    1: [
                        ("Tunnel Mastery", "The Ratkin gains mastery of tunnels. (Changing Breeds, p. 188)"),
                        ("Underground Speed", "The Ratkin can move quickly underground. (Changing Breeds, p. 188)")
                    ],
                    2: [
                        ("Perfect Tunnel", "The Ratkin can create perfect tunnels. (Changing Breeds, p. 188)"),
                        ("Tunnel's Power", "The Ratkin gains power in tunnels. (Changing Breeds, p. 188)")
                    ],
                    3: [
                        ("Tunnel's Dominion", "The Ratkin gains dominion over tunnels. (Changing Breeds, p. 188)"),
                        ("Underground Mastery", "The Ratkin gains mastery underground. (Changing Breeds, p. 188)")
                    ]
                },
                "Shadow Seer": {
                    1: [
                        ("Shadow Sight", "The Ratkin can see in shadows. (Changing Breeds, p. 188)"),
                        ("Spirit Vision", "The Ratkin can see spirits. (Changing Breeds, p. 188)")
                    ],
                    2: [
                        ("Perfect Vision", "The Ratkin can see perfectly. (Changing Breeds, p. 188)"),
                        ("Shadow's Power", "The Ratkin gains power from shadows. (Changing Breeds, p. 188)")
                    ],
                    3: [
                        ("Shadow's Dominion", "The Ratkin gains dominion over shadows. (Changing Breeds, p. 188)"),
                        ("Vision's Mastery", "The Ratkin gains mastery of vision. (Changing Breeds, p. 188)")
                    ]
                },
                "Knife Skulker": {
                    1: [
                        ("Knife Mastery", "The Ratkin gains mastery of knives. (Changing Breeds, p. 188)"),
                        ("Stealth's Power", "The Ratkin gains power from stealth. (Changing Breeds, p. 188)")
                    ],
                    2: [
                        ("Perfect Knife", "The Ratkin can use knives perfectly. (Changing Breeds, p. 188)"),
                        ("Skulker's Mastery", "The Ratkin gains mastery of skulking. (Changing Breeds, p. 188)")
                    ],
                    3: [
                        ("Knife's Dominion", "The Ratkin gains dominion over knives. (Changing Breeds, p. 188)"),
                        ("Stealth's God", "The Ratkin becomes a god of stealth. (Changing Breeds, p. 188)")
                    ]
                },
                "Blade Slave": {
                    1: [
                        ("Blade Mastery", "The Ratkin gains mastery of blades. (Changing Breeds, p. 189)"),
                        ("Combat's Power", "The Ratkin gains power in combat. (Changing Breeds, p. 189)")
                    ],
                    2: [
                        ("Perfect Blade", "The Ratkin can use blades perfectly. (Changing Breeds, p. 189)"),
                        ("Slave's Mastery", "The Ratkin gains mastery of combat. (Changing Breeds, p. 189)")
                    ],
                    3: [
                        ("Blade's Dominion", "The Ratkin gains dominion over blades. (Changing Breeds, p. 189)"),
                        ("Combat's God", "The Ratkin becomes a god of combat. (Changing Breeds, p. 189)")
                    ]
                },
                "Ratkin Engineer": {
                    1: [
                        ("Engineering Mastery", "The Ratkin gains mastery of engineering. (Changing Breeds, p. 189)"),
                        ("Technology's Power", "The Ratkin gains power from technology. (Changing Breeds, p. 189)")
                    ],
                    2: [
                        ("Perfect Engineering", "The Ratkin can engineer perfectly. (Changing Breeds, p. 189)"),
                        ("Engineer's Mastery", "The Ratkin gains mastery of engineering. (Changing Breeds, p. 189)")
                    ],
                    3: [
                        ("Engineering's Dominion", "The Ratkin gains dominion over engineering. (Changing Breeds, p. 189)"),
                        ("Technology's God", "The Ratkin becomes a god of technology. (Changing Breeds, p. 189)")
                    ]
                },
                "Plague Lord": {
                    1: [
                        ("Plague Mastery", "The Ratkin gains mastery of plagues. (Changing Breeds, p. 189)"),
                        ("Disease's Power", "The Ratkin gains power from disease. (Changing Breeds, p. 189)")
                    ],
                    2: [
                        ("Perfect Plague", "The Ratkin can create perfect plagues. (Changing Breeds, p. 189)"),
                        ("Plague's Mastery", "The Ratkin gains mastery of plagues. (Changing Breeds, p. 189)")
                    ],
                    3: [
                        ("Plague's Dominion", "The Ratkin gains dominion over plagues. (Changing Breeds, p. 189)"),
                        ("Disease's God", "The Ratkin becomes a god of disease. (Changing Breeds, p. 189)")
                    ]
                },
                "Munchmausen": {
                    1: [
                        ("Lie Mastery", "The Ratkin gains mastery of lies. (Changing Breeds, p. 190)"),
                        ("Deception's Power", "The Ratkin gains power from deception. (Changing Breeds, p. 190)")
                    ],
                    2: [
                        ("Perfect Lie", "The Ratkin can tell perfect lies. (Changing Breeds, p. 190)"),
                        ("Munchmausen's Mastery", "The Ratkin gains mastery of deception. (Changing Breeds, p. 190)")
                    ],
                    3: [
                        ("Lie's Dominion", "The Ratkin gains dominion over lies. (Changing Breeds, p. 190)"),
                        ("Deception's God", "The Ratkin becomes a god of deception. (Changing Breeds, p. 190)")
                    ]
                },
                "Twitcher": {
                    1: [
                        ("Madness Mastery", "The Ratkin gains mastery of madness. (Changing Breeds, p. 190)"),
                        ("Chaos's Power", "The Ratkin gains power from chaos. (Changing Breeds, p. 190)")
                    ],
                    2: [
                        ("Perfect Madness", "The Ratkin can create perfect madness. (Changing Breeds, p. 190)"),
                        ("Twitcher's Mastery", "The Ratkin gains mastery of chaos. (Changing Breeds, p. 190)")
                    ],
                    3: [
                        ("Madness's Dominion", "The Ratkin gains dominion over madness. (Changing Breeds, p. 190)"),
                        ("Chaos's God", "The Ratkin becomes a god of chaos. (Changing Breeds, p. 190)")
                    ]
                }
            },
            "tribe": {},
            "general": {
                1: [
                    ("Rat's Bite", "The Ratkin's bite becomes incredibly deadly. (Changing Breeds, p. 186)"),
                    ("Tunnel Sense", "The Ratkin can navigate tunnels perfectly. (Changing Breeds, p. 186)"),
                    ("Sense Wyrm", "The Ratkin can sense nearby manifestations of the Wyrm. (Changing Breeds, p. 186)")
                ],
                2: [
                    ("Rat's Cunning", "The Ratkin gains increased intelligence. (Changing Breeds, p. 186)"),
                    ("Pack Tactics", "The Ratkin can coordinate pack attacks. (Changing Breeds, p. 186)")
                ],
                3: [
                    ("Rat's Swarm", "The Ratkin can call upon a swarm of rats. (Changing Breeds, p. 186)"),
                    ("Perfect Tunnel", "The Ratkin can create perfect tunnels. (Changing Breeds, p. 186)")
                ],
                4: [
                    ("Rat's Dominion", "The Ratkin gains dominion over rats. (Changing Breeds, p. 186)"),
                    ("Swarm's God", "The Ratkin becomes a god of swarms. (Changing Breeds, p. 186)")
                ],
                5: [
                    ("Perfect Rat", "The Ratkin becomes the perfect rat. (Changing Breeds, p. 186)")
                ]
            }
        }
    },
    "Rokea": {
        "display_name": "Rokea (Wereshark)",
        "breeds": {
            "Homid": {
                "description": "Born to human mothers (rare, mostly Same-Bito).",
                "initial_gnosis": 1,
                "initial_willpower": 4,
                "beginning_gifts": [],
                "restrictions": []
            },
            "Squamus": {
                "description": "Shark-born, most common.",
                "initial_gnosis": 5,
                "initial_willpower": 4,
                "beginning_gifts": [],
                "restrictions": {
                    "skills": ["Crafts", "Drive", "Etiquette", "Firearms", "Larceny"],
                    "knowledges": ["Academics", "Computer", "Law", "Science", "Technology"]
                }
            }
        },
        "auspices": {
            "Brightwater": {
                "description": "First Change on sunny day or full moon.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 4,
                "beginning_gifts": []
            },
            "Dimwater": {
                "description": "First Change on cloudy day or night except new/full moon.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 4,
                "beginning_gifts": []
            },
            "Darkwater": {
                "description": "First Change during eclipse or new moon.",
                "initial_rage": 0,
                "initial_gnosis": 0,
                "initial_willpower": 4,
                "beginning_gifts": []
            }
        },
        "tribes": {},  # Rokea don't have tribes
        "forms": {
            "Homid": {
                "description": "Human form (Long Fins), squat and coarse-featured.",
                "statistics_adjustment": {
                    "Strength": 0, "Dexterity": 0, "Stamina": 0,
                    "Charisma": 0, "Manipulation": 0, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal human size",
                "special": "Squat and coarse-featured"
            },
            "Glabrus": {
                "description": "Near-man form (Round Back).",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 0, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -2, "Appearance": -2,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Larger than human",
                "special": "Reduced Delirium (Willpower +2). Bite: difficulty 5, lethal damage (Strength). +1 Dex in water"
            },
            "Gladius": {
                "description": "War form (Standing Jaws), 10+ feet tall.",
                "statistics_adjustment": {
                    "Strength": 3, "Dexterity": -1, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -4, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "10+ feet tall",
                "special": "Full Delirium. Bite: Str +1 aggravated. +2 Dex in water"
            },
            "Chasmus": {
                "description": "Huge shark form (Fighting Jaws).",
                "statistics_adjustment": {
                    "Strength": 4, "Dexterity": 0, "Stamina": 3,
                    "Charisma": 0, "Manipulation": -4, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Half-again normal length",
                "special": "Full Delirium. Bite: Str +2 aggravated. +1 Dex in water"
            },
            "Squamus": {
                "description": "Normal shark form (Swimming Jaws).",
                "statistics_adjustment": {
                    "Strength": 2, "Dexterity": 0, "Stamina": 2,
                    "Charisma": 0, "Manipulation": -4, "Appearance": 0,
                    "Perception": 0, "Intelligence": 0, "Wits": 0
                },
                "shift_difficulty": 6,
                "size": "Normal shark size",
                "special": "+3 Dex in water"
            }
        },
        "renown_types": ["Valor", "Harmony", "Innovation"],
        "starting_traits": {
            "rage": 0,
            "gnosis": "by_breed",
            "willpower": 4  # Fixed for all Rokea
        },
        "gifts": {
            "breed": {
                "Homid": {
                    1: [
                        ("Shark's Cunning", "The Rokea gains increased intelligence. (Changing Breeds, p. 202)"),
                        ("Smell of Man", "The Rokea can blend into human society. (Changing Breeds, p. 202)")
                    ]
                },
                "Squamus": {
                    1: [
                        ("Shark's Grace", "The Rokea gains incredible agility in water. (Changing Breeds, p. 202)"),
                        ("Water Sense", "The Rokea can sense everything in the water. (Changing Breeds, p. 202)")
                    ]
                }
            },
            "auspice": {
                "Brightwater": {
                    1: [
                        ("Brightwater's Power", "The Rokea gains power in bright water. (Changing Breeds, p. 202)"),
                        ("Sun's Blessing", "The Rokea gains blessings from the sun. (Changing Breeds, p. 202)")
                    ],
                    2: [
                        ("Brightwater's Mastery", "The Rokea gains mastery of bright water. (Changing Breeds, p. 202)"),
                        ("Sun's Wrath", "The Rokea can unleash the sun's fury. (Changing Breeds, p. 202)")
                    ],
                    3: [
                        ("Perfect Brightwater", "The Rokea can create perfect bright water. (Changing Breeds, p. 202)"),
                        ("Sun's Dominion", "The Rokea gains dominion over the sun. (Changing Breeds, p. 202)")
                    ]
                },
                "Dimwater": {
                    1: [
                        ("Dimwater's Power", "The Rokea gains power in dim water. (Changing Breeds, p. 203)"),
                        ("Cloud's Blessing", "The Rokea gains blessings from clouds. (Changing Breeds, p. 203)")
                    ],
                    2: [
                        ("Dimwater's Mastery", "The Rokea gains mastery of dim water. (Changing Breeds, p. 203)"),
                        ("Cloud's Wrath", "The Rokea can unleash the cloud's fury. (Changing Breeds, p. 203)")
                    ],
                    3: [
                        ("Perfect Dimwater", "The Rokea can create perfect dim water. (Changing Breeds, p. 203)"),
                        ("Cloud's Dominion", "The Rokea gains dominion over clouds. (Changing Breeds, p. 203)")
                    ]
                },
                "Darkwater": {
                    1: [
                        ("Darkwater's Power", "The Rokea gains power in dark water. (Changing Breeds, p. 204)"),
                        ("Eclipse's Blessing", "The Rokea gains blessings from eclipses. (Changing Breeds, p. 204)")
                    ],
                    2: [
                        ("Darkwater's Mastery", "The Rokea gains mastery of dark water. (Changing Breeds, p. 204)"),
                        ("Eclipse's Wrath", "The Rokea can unleash the eclipse's fury. (Changing Breeds, p. 204)")
                    ],
                    3: [
                        ("Perfect Darkwater", "The Rokea can create perfect dark water. (Changing Breeds, p. 204)"),
                        ("Eclipse's Dominion", "The Rokea gains dominion over eclipses. (Changing Breeds, p. 204)")
                    ]
                }
            },
            "tribe": {},
            "general": {
                1: [
                    ("Shark's Bite", "The Rokea's bite becomes incredibly deadly. (Changing Breeds, p. 202)"),
                    ("Water Mastery", "The Rokea gains mastery of water. (Changing Breeds, p. 202)"),
                    ("Sense Prey", "The Rokea can track and locate prey in water. (Changing Breeds, p. 202)")
                ],
                2: [
                    ("Shark's Speed", "The Rokea can move incredibly fast in water. (Changing Breeds, p. 202)"),
                    ("Water's Power", "The Rokea gains power from water. (Changing Breeds, p. 202)")
                ],
                3: [
                    ("Shark's Frenzy", "The Rokea can enter a feeding frenzy. (Changing Breeds, p. 202)"),
                    ("Perfect Water", "The Rokea can create perfect water. (Changing Breeds, p. 202)")
                ],
                4: [
                    ("Shark's Dominion", "The Rokea gains dominion over sharks. (Changing Breeds, p. 202)"),
                    ("Water's God", "The Rokea becomes a god of water. (Changing Breeds, p. 202)")
                ],
                5: [
                    ("Perfect Shark", "The Rokea becomes the perfect shark. (Changing Breeds, p. 202)")
                ]
            }
        }
    }
}

