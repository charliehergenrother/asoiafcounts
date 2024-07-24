#!/usr/bin/env python3

#gotta do something about King's Landing
#and castle black
#make young wolf = Robb Stark
#red keep, king's landing, storm's end
import sys

real_words = ["We", "The", "Do", "He", "Dead", "Are", "What", "If", "My", "Never", "There", "His", \
        "Eight", "And", "It", "Ser", "I", "She", "You", "A", "They", "No", "When", "That", "Her",
        "This", "Winterfell", "I’m", "As", "Wall", "I’ll", "Your", "Why", "In", "How", "For", "Watch",
        "So", "Yet", "Yes", "Then", "Even", "All", "Night", "Is", "Oh", "Landing", "Riverrun", "Now",
        "But", "One", "Not", "Eyrie", "By", "Perhaps", "At", "Tell", "Let", "Seven", "Kingdoms",
        "Only", "I’d", "Vale", "I’ve", "Where", "Kingsguard", "Some", "To", "Come", "Well",
        "Casterly Rock", "Who", "Here", "Gods", "On", "Trident", "Did", "Their", "You’re", "After",
        "Or", "Please", "Don’t", "Look", "Take", "Once", "From", "Tower", "With", "Go", "Have",
        "Others", "Three", "Would", "Vaes", "Dothrak", "Needle", "Can", "Another", "Most", "Two", 
        "Behind", "Finally", "Dragonstone", "You’ll", "First", "Men", "House", "Iron", "Throne",
        "Give", "Our", "Every", "Free", "Cities", "Still", "These", "Was", "Pentos", "Just",
        "Valyrian", "Nothing", "Those", "Remember", "Whatever", "North", "Good", "Ah", "Thank",
        "Castle", "Damn", "Bring", "Neck", "Make", "Seven", "Nor", "Ice", "Maybe", "An", "Sometimes",
        "Inside", "End", "He’d", "More", "Twins", "Mountains", "Something", "We’ll", "Be", "Beyond",
        "Highgarden", "Myr", "Too", "Stop", "We’re", "Asshai", "Harrenhal", "They’re", "Other",
        "Winter", "May", "Very", "See", "Crows", "Leave", "Fear", "Get", "None", "Suddenly",
        "Send", "Before", "Outside", "Does", "Common", "Across", "Its", "Kings", "Dorne", "Someone",
        "Until", "Everyone", "Best", "Gate", "Braavos", "Many", "Afterward", "Had", "Corn", "Kill",
        "Under", "Each", "Andals", "Realm", "Put", "Lys", "Last", "Enough", "Any", "Quiet",
        "Lannisters", "Starks", "Red Keep", "Castle Black", "Blood", "Small", "Tullys", "Great Hall",
        "Tongue", "Shadow", "Arryns", "City", "Freys", "Burned", "Both", "Moon", "Better", "West",
        "Help", "Drink", "Such", "Up", "Down", "Targaryens", "Six", "Between", "Lords",
        "Surely", "Might", "Of", "Later", "You’ve", "Fingers", "Could", "Street", "Try", "Green Fork",
        "Moon Brothers", "Four", "Soon", "Over", "Name", "Red Fork", "Valyria", "Beneath",
        "Summer Isles", "Tears", "Since", "Honor", "Shall", "White Harbor", "M’lord", "Eastwatch",
        "Myrish", "Moat Cailin", "She’d", "He’ll", "Unless", "Save", "Lamb", "Can’t", "Far", "Promise",
        "East", "Boy", "Has", "Like", "Fire", "Tooth", "Great Sept", "Lannisport", "They’ll", "Pray",
        "Mole", "Town", "Out", "High Hall", "Bloody", "Holdfast", "Sworn Brother", "We’ve", "Which",
        "Moonlight", "Besides", "Wait", "Close", "Sit", "Open", "Stay", "Somehow", "People", "Below",
        "Steel", "Forgive", "Fool", "Know", "Must", "Show", "Sky", "Today", "Somewhere", "Mallisters",
        "Listen", "Again", "Faces", "Jade Sea", "Tyrosh", "Qohor", "Dragons", "Lands", "Slowly",
        "Bear Island", "Five", "Above", "Silence", "Beside", "Pain", "They’d", "Women", "Age", "Truly",
        "White Swords", "Western Market", "Golden Tooth", "Black Ears", "Water", "Longclaw",
        "Tumblestone", "Nine", "Ever", "Everything", "Rhoynar", "Me", "Whenever",
        "Nonetheless", "Home", "Always", "Next", "Am", "Often", "Burn", "Death", "Call", "Dark",
        "Dawn", "Life", "Past", "Thick", "Say", "Sisters", "Almost", "Twenty", "Spare", "Think",
        "Should", "Citadel", "Back", "Tomorrow", "Wine", "Horn Hill", "Children", "Heroes",
        "Brackens", "While", "Calm", "Off", "Gold", "Arbor", "Mummer", "Ride", "Die", "Flea Bottom",
        "Whispering Wood", "Pale", "Answer", "Worse", "She’ll", "Isle", "Light", "Port", "Instead",
        "Ibben", "Instead", "Fifteen", "Laughter", "Otherwise", "Indeed", "Live", "Duty", "War",
        "Part", "Dragon", "Mormonts", "Alas", "Ask", "Wordlessly", "They’ve", "Huge", "Though", "Liar",
        "Because", "Blackwater Rush", "Cold", "Oldtown", "Doubtless", "Small Hall", "Wherever",
        "Mud", "Around", "Mind", "Riders", "Seagard", "Aye", "Less", "Horse", "Quick", "Swift",
        "Fierce", "Giant", "Lance", "Gates", "Isn’t", "Moon Door", "Without", "Little", "Ford",
        "Rise", "Sleep", "Wind Witch", "Womb", "World", "HEar", "Glovers", "Hornwoods", "Broken",
        "Peace", "Pact", "Despite", "Guard", "Reluctantly", "Dance", "Done", "Easy", "Faith", "Family",
        "Doom", "Westeros", "Ours", "Turn", "Boys", "Ten", "Likely", "Late", "Shadows", "Dragonlords",
        "Against", "Wardens", "Dogs", "Sorry", "Shouldn’t", "You’d", "Fourteen", "Mothers", "Bad",
        "Food", "Yours", "Blessed", "Sworn Brothers", "Reach", "Near", "Want", "Hold", "Ofttimes",
        "Pick", "Shut", "Fly", "Bite", "Storm Dancer", "Cruel", "Blackwater", "Were", "Keep",
        "Brothers", "Prince Aemon", "Rock", "Golden", "Sherrer", "Whoever", "Poor", "Been", "Shy",
        "Wed", "Lie", "Having", "Speaking", "Farewell", "Wary", "Different", "Trust", "Nervously",
        "Praying", "Lightly", "Treachery", "Resigned", "Sullen", "Frustrated", "Anxious", "Find",
        "Look", "Centuries", "Barley", "Forty", "Ninety", "Instruct", "Apart", "However", "Steal",
        "Everybody", "Swinging", "Hurt", "Smaller", "Summon", "Gently", "Thrice", "Madness",
        "Stop", "This", "Curiosity", "Particularly", "Whereas", "Inform", "Vertigo", "Tired",
        "Whether", "Ahead", "Drops", "Holding", "Deserters", "Message", "Summon", "Useful",
        "Murder", "Throwing", "Aren’t", "Set", "Aged", "Scum", "Ahhhh", "Grease", "Thirteen",
        "Burning", "Sending", "Paynes", "Descriptions", "Thirty", "Hurriedly", "Stinks", "Certainly",
        "Strike", "Shocking", "Seat", "Wed", "Smiling", "Excellent", "Esteemed", "Ow", "Opening",
        "Grasping", "Unlatching", "Mourning", "MAtters", "Sudden", "Bass", "Plainly", "Use",
        "One-armed", "Queer", "Gagging", "Gnawed", "Spinning", "Boltons", "Baratheons", "Folk",
        "Lorath", "Qartheen", "Cakes", "Smokeberry", "Drifting", "Thin", "Bosom", "Glaring",
        "Idle", "Cracks", "Martells", "Calmly", "Sixteen", "Fine", "Doves", "Ai", "Meereen", "Slaver",
        "Bay", "Faint", "Maddened", "Fumbling", "Dazed", "Blue Fork", "Heedless", "Trembling",
        "Ashamed", "Louder", "Dreams", "Dragonglass", "Forged", "Male", "Memory", "Remembering",
        "Curse", "Rank", "Uncouth", "Walls", "Pushing", "Ransoms", "Rivulets", "Whores", "Wear",
        "Guards", "Chased", "Concerning", "Washing", "Lengthen", "Sweat", "Wrong", "Hunting",
        "Sneaking", "Cupping", "Twelve", "Someday", "Command", "Sickly", "Houses", "Buried", "Grief",
        "Valor", "Flour", "Dimly", "Numb", "Parry", "Horror-struck", "Careful", "Obsidian", "Curious",
        "Tottering", "Soot", "Dates", "Time", "Alive", "O", "Leaves", "Fetch", "Ravens", "Taken", "Yi Ti",
        "Qarth", "Jade Sea", "Fewer", "Casterly", "Half", "Morning", "Crossing", "Hear", "Sunset", "Rush",
        "Hall", "Arm", "Door", "Wendish", "Sworn", "Norvos", "Crown", "Hardin", "Duel", "Much", "Already",
        "Farther", "Few", "Whose", "Among", "Truth", "Faster", "Poison", "Frowning", "Through", "Cut",
        "Talk", "Heartsbane", "Knights", "Rides", "Redwynes", "Dying", "Craven", "Flames", "Fifty",
        "Eastern Market", "Yield", "Someday", "Rakh", "Bells", "Goose", "Away", "Low", "Treason",
        "Dreadfort", "Andal", "Gatehouse", "Heat", "Strength", "Flour", "Wheel", "Fallen", "Lead",
        "Swords", "Lying", "Direwolves", "Worship", "Tonight", "Volantis", "Years", "Stand", "Anger",
        "Dornishmen", "Nodding", "Battle", "Oil", "Absurd", "Blind", "Hungry", "Also", "Standing", "Pride",
        "Clearly", "Power", "Rhoyne", "Bastards", "Girls", "Gladly", "Guards", "Unlike", "Guest", "During",
        "Leaving", "Stick", "Run", "Slaves", "Hesitantly", "Dragonbone", "Field", "Things", "Sad", "Sobbing",
        "Rest", "Begging", "White Knife", "Anyway", "Alone", "Choose", "Wings", "Dragonpit", "About",
        "Careful", "Words", "Lacking", "Older", "Shattered", "Wise", "Speak", "Follow", "Bits",
        "Great Summer", "Mine", "Grieve", "Day", "Hit", "Angry", "Thousands", "Sunset Sea", "Escort",
        "Scarcely", "Tyrells", "Silent", "Tarlys", "South", "Hours", "Stout", "Lineages", "Histories",
        "Great Houses", "Noble Ladies", "Watchmen", "Singers", "Distantly", "Anything", "Marches", "Neither",
        "Quite", "Pretty", "Piss", "Dornish Marches", "Steam", "Logs", "Move", "Traitor", "Walk", "Startled",
        "Smooth", "Loose", "Delay", "Monsters", "Mercy", "Kiss", "True", "Toward", "Fresh", "Laughing",
        "Torches", "Arrogance", "Hers", "Moving", "Whores", "Love", "Riding", "Rivulets", "Ugly", "Allow",
        "Spying", "Didn’t", "Smoking Log", "Looking", "Wolves", "Groaning", "Rainbows", "Metal", "Monkey",
        "Wake", "Time", "Kindly", "Underneath", "Naked", "Caravan", "Groggy", "Fires", "Servants",
        "Ought", "Write", "Heavy", "Rangers", "Houses", "Bend", "Watching", "Taste", "Child", "Karstarks",
        "Karhold", "Cerwyns", "Drunkard", "Grim", "Either", "Splendid", "Lastly", "Weak", "Pity", "We’d",
        "Wounded", "Heh", "Claw", "Crow", "Quickly", "Trout", "Ravens", "Fetch", "Woman", "Bottom",
        "Stupid", "Dimly", "Eye", "Spit", "Anyone", "Stone Hedge", "Sell", "Especially", "Mounted", "Bet",
        "Heavy-looking", "Frostfallen", "Peaceful", "Weeping", "Bright", "Twilight", "Trees", "Jewels",
        "Bears", "Branches", "Tall", "Shivering", "Ass", "Race", "Wrapped", "Trouble", "Half-buried",
        "Born", "Halfway", "Freehold", "Filled", "Damnation", "Dread", "Touch", "Caress", "Straighten",
        "Rhaesh Andali", "Braavosian", "Regal", "Gemstones", "Insolent", "Third",
        "Anointed", "Anxiously", "Smile", "Islands", "Bogs", "Flickering", "Fostering", "Laws", "Summerwine",
        "Notable", "Nice", "Dwarfs", "Generations", "Armor", "Honors", "Pardons", "Lighting", "Teach",
        "Summer Sea", "Starfall", "Preparations", "Naturally", "Master-at-arms", "Beat", "Fingernails",
        "Screaming", "Engines", "Patiently", "Spirits", "Breaking", "Bread", "Good-bye", "Wagons",
        "Honey", "Theirs", "Drums", "Silver", "Custom", "Taking", "Unspeakable", "Troubled", "Killing",
        "Scarce", "Rapers", "Farms", "Unchanged", "Abashed", "Rubies", "Dense", "Cradled", "Tenderly",
        "Perchance", "Sooner", "Shortly", "Buried", "Bending", "Forget", "Warm", "Teaching", "Look", "Down",
        "Deepwater", "Sixty", "Eel", "Alley", "Comes", "Ofttimes", "Thankfully", "Enter", "Methodically",
        "Chunks", "Stupidly", "Stop", "S", "Sea", "Makes", "Crippled", "Read", "Rather", "Wispy", "Garnets",
        "Fools", "Bank", "Painfully", "Accuse", "Roars", "Chip", "Stableboys", "Bundled", "Halt", "Hello",
        "Friend", "Saddle", "Forest", "Rage", "Crack", "Everywhere", "Magic", "Brave", "Stories", "Visitors",
        "Nonsense", "Sunlight", "Higher", "Wouldn’t", "Iced", "Minds", "Unnatural", "Second", "Fortunate",
        "Fifth", "Notice", "Distrusting", "Southron", "Rat", "Dressed", "Frustrate", "Chainmail", "Facing",
        "Horn", "Nobody", "Goldengrove", "Drinking", "Talking", "Hire", "Clever", "Carrots", "River",
        "Elsewhere", "Apples", "Visit", "Journeymen", "Turnips", "Describe", "Shadowcats", "Blackwoods",
        "Darrys", "Rygers", "Mootons", "Innkeep", "Double", "Younger", "Tables", "Salads", "Snails",
        "Gallant", "Drunken", "Ointments", "Arise", "Slain", "Plain", "Squires", "Cousins", "Sons", "Wood",
        "Cheers", "Cats", "Yard", "Law", "Amidst", "Wheels", "Asking", "Meat", "Tastes", "Strangers",
        "Trying", "Force", "Nearby", "Rough", "Pebbles", "Milk", "Pretend", "Arrows", "Odd", "Mauls",
        "Gather", "Catching", "Quickly", "Panic", "Oof", "Slippery", "Dropping", "Grossly", "Blinded",
        "Twice", "Made", "Rode", "Sellswords", "Rely", "Sadly", "Kinder", "Waiting", "Desperately",
        "Defiance", "Lamprey", "Titles", "Resolute", "Hearing", "Waynwoods", "Wheat", "Looming", "Courage",
        "Chains", "Farm", "Mules", "Keeper", "Redforts", "Sure", "Directly", "Shorter", "Brothels",
        "Eyes", "Dragonkings", "Lithe", "Fury", "Share", "Murdered", "Side", "Lost", "Straps", "Folly",
        "Hack", "Submission", "Nightmare", "Turnkey", "Making", "Dangling", "Suspicion", "Fortunately",
        "Writing", "Guardsmen", "Behold", "Torch", "Singer", "Proud", "Woe", "Charged", "Abductions",
        "Wear", "Confused", "Gulltown", "Going", "Pitchers", "Behead", "Ignoring", "Whirling", "Trial",
        "Large", "Falcon", "Fight", "Oak", "Staggered", "Deep", "Finish", "Yelling", "Start", "Animals",
        "Travel", "Happily", "Land", "Seasons", "Lowborn", "Massive", "Lions", "Lances", "Mail", "Brigands",
        "Hares", "Vengeance", "Gladden", "Foolish", "Somebody", "Washing", "Inflamed", "Freeriders", "Given",
        "Royces", "Aside", "Lengthen", "Exile", "Stolen", "Alongside", "Cook", "Within", "Missed", "Drove",
        "Wrong", "Paper", "Protect", "Serve", "Apple", "Eat", "Hunting", "Release", "Round", "Builders",
        "Present", "Canvas", "Pardon", "Supported", "Crimson", "Lunge", "Smell", "Feel", "Bald", "Frothy",
        "Shoving", "Sneaking", "Cupping", "Matters", "Us", "Mere", "Bid", "Squatting", "Belike", "Blossoms",
        "Untouched", "Unbidden", "Holdfasts", "Curiously", "Vain", "Spirit", "Stew", "Crouching", "Keeping",
        "Shouting", "Finger", "Frost", "Staggering", "Tallharts", "Cursing", "Giants", "Lordling",
        "Uncomfortably", "Savage", "Wooden", "Coarse", "Hummocks", "Enjoy", "Delighted", "Turning", "Whites",
        "Andalish", "Pour", "Empty", "Cradling", "Living", "Outriders", "Immense", "Standards", "Remind",
        "Concern", "Greywater", "Marching", "Command", "Moat", "Lowland", "Grinning", "Distant", "Presters",
        "Provided", "Kind", "Roar", "Raventree", "Pipers", "Ordinarily", "Savages", "Shield", "Horses",
        "Return", "Joy", "Freedom", "Sickly", "Vainly", "Butterflies", "Failing", "Proud", "Melt", "Buried",
        "Grunts", "Dregs", "Questions", "Offer", "Ponder", "Expect", "Defending", "Healing", "Grief",
        "Awkwardly", "Carefully", "Eastwatch-by-the-sea", "Valor", "Toss", "Feathers", "Strings", "Choosing",
        "Headless", "Ships", "Godswife", "Sheepskins", "Harm", "Ferocious", "Dusk", "Fireflies", "Suckling",
        "Definitely", "Into", "Softly", "Wisps", "Hurry", "Several", "Quivers", "Spears", "Chips",
        "Reining", "True", "Patience", "Eons", "Raid", "Clumsily", "Furious", "Admit", "Deftly", "Weep",
        "Days", "Kicks", "Weasels", "Braziers", "Rein", "Tents", "Compared", "Mostly", "Flocks", "Sept",
        "Forcing", "Sliding", "Clustered", "Taunts", "Beloved", "Immediately", "Bodies", "Sour", "Numb",
        "Hope", "Bones", "Parry", "Block", "Stubborn", "Soot", "Tottering", "Pads", "Waking", "Dress",
        "Hollow", "Wipe", "Ghosts", "Flakes", "Flying", "Dragondew", "Dates", "Shell", "Scales", "Monstrous",
        "Twisted", "Darkness", "Saved", "Remain", "Commands", "Unleash", "Telling", "Rule", "Spikes",
        "Heads", "Scattered", "Leaves", "Pull", "Gorge", "Thoughts", "Boats", "Him", "Taken", "Marry",
        "Word", "March", "Noble", "My", "Bound", "Fewer", "Stretching", "Queensguard", "Bloodred", "Tiny",
        "Unafraid", "Wordless"
        ]

name_translations = {
        "Mance": "Mance Rayder",
        "Janos": "Janos Slynt",
        "Jared": "Jared Frey",
        "Tyrion": "Tyrion Lannister", #axe for AFFC
        "Arya": "Arya Stark", #ASOS
        "Catelyn": "Catelyn Stark", #ADWD
        "Sansa": "Sansa Stark",
        "Dany": "Daenerys Targaryen",
        "Robb": "Robb Stark",
        "Littlefinger": "Petyr Baelish",
        "Jorah": "Jorah Mormont", #ACOK
        "Lord Tywin": "Tywin Lannister",
        "Drogo": "Khal Drogo",
        "Viserys": "Viserys Targaryen", #AFFC
        "Jaime": "Jaime Lannister",
        "Lord Eddard": "Eddard Stark",
        "Lysa Anyn": "Lysa Arryn",
        "Lysa": "Lysa Arryn",
        "Jory": "Jory Cassel", #ADWD
        "Sam": "Samwell Tarly",
        "Cersei": "Cersei Lannister", #ASOS
        "Rickon": "Rickon Stark",
        "Hound": "Sandor Clegane",
        "Lord Renly": "Renly Baratheon",
        "Gregor": "Gregor Clegane",
        "Barristan": "Barristan Selmy",
        "Illyrio": "Illyrio Mopatis",
        "Alliser": "Alliser Thorne",
        "Old Bear": "Jeor Mormont",
        "Vardis": "Vardis Egen",
        "Kingslayer": "Jaime Lannister",
        "Prince Joffrey": "Joffrey Baratheon",
        "King Robert": "Robert Baratheon",
        "Imp": "Tyrion Lannister",
        "Edmure": "Edmure Tully",
        "Grand Maester Pycelle": "Maester Pycelle",
        "Pycelle": "Maester Pycelle",
        "Stannis": "Stannis Baratheon", #ACOK
        "Renly": "Renly Baratheon",
        "Brynden": "Brynden Tully", #AFFC
        "Daenerys": "Daenerys Targaryen", #ADWD
        "Rhaegar": "Rhaegar Targaryen", #AFFC
        "Lord Stannis": "Stannis Baratheon",
        "Lyanna": "Lyanna Stark", #ADWD
        "Theon": "Theon Greyjoy", #ACOK
        "Theon Greyioy": "Theon Greyjoy",
        "Syrio": "Syrio Forel",
        "Kevan": "Kevan Lannister",
        "Magister Illyrio": "Illyrio Mopatis",
        "Greatjon": "Greatjon Umber",
        "Ned Stark": "Eddard Stark",
        "Lord Baelish": "Petyr Baelish",
        "Loras": "Loras Tyrell",
        "Lord Walder": "Walder Frey",
        "Lord Varys": "Varys",
        "Usurper": "Robert Baratheon",
        "Luwin": "Maester Luwin",
        "Meryn": "Meryn Trant",
        "Petyr": "Petyr Baelish", #ACOK
        "Cat": "Catelyn Stark",
        "Lady Lysa": "Lysa Arryn",
        "Mya": "Mya Stone",
        "Boros": "Boros Blount",
        "Ilyn": "Ilyn Payne",
        "Jaremy": "Jaremy Rykker",
        "Lord Mormont": "Jeor Mormont",
        "Lord Beric": "Beric Dondarrion",
        "Mountain": "Gregor Clegane",
        "Joff": "Joffrey Baratheon",
        "Lord Petyr": "Petyr Baelish",
        "Fat Tom": "Tomard",
        "Lord Hoster": "Hoster Tully",
        "Waymar": "Waymar Royce",
        "Lord Eddard Stark": "Eddard Stark",
        "Myrcella": "Myrcella Baratheon",
        "Lord Frey": "Walder Frey",
        "Tommen": "Tommen Baratheon", #ASOS
        "Lady Catelyn": "Catelyn Stark",
        "Lord Snow": "Jon Snow",
        "Aerys": "Aerys II Targaryen", #ADWD
        "Lord Tywin Lannister": "Tywin Lannister",
        "Princess Myrcella": "Myrcella Baratheon",
        "Queen Cersei": "Cersei Lannister",
        "Uncle Benjen": "Benjen Stark",
        "Lady Arryn": "Lysa Arryn",
        "Maegor": "Maegor I Targaryen",
        "King Joffrey": "Joffrey Baratheon",
        "Blackfish": "Brynden Tully",
        "Prince Tommen": "Tommen Baratheon",
        "Ben Stark": "Benjen Stark",
        "Aerys Targaryen": "Aerys II Targaryen",
        "Stevron": "Stevron Frey",
        "Hal Mollen": "Hallis Mollen",
        "Lord Nestor": "Nestor Royce",
        "Mirri": "Mirri Maz Duur",
        "Spider": "Varys",
        "Lord Commander Mormont": "Jeor Mormont",
        "Willis": "Willis Wode",
        "Haider": "Halder",
        "Tywin": "Tywin Lannister", #AFFC
        "Wendel": "Wendel Manderly",
        "Lord Lefford": "Leo Lefford",
        "Lord Hoster Tully": "Hoster Tully",
        "Dragonknight": "Aemon the Dragonknight",
        "Aemon Maester": "Maester Aemon",
        "Catelyn Tully": "Catelyn Stark",
        "Sandor": "Sandor Clegane",
        "Lord Petyr Baelish": "Petyr Baelish",
        "Lord Randyll": "Randyll Tarly",
        "Lord Jason Mallister": "Jason Mallister",
        "Perwyn": "Perwyn Frey",
        "King Aerys": "Aerys II Targaryen",
        "Lady Catelyn Stark": "Catelyn Stark",
        "Brynden Blackfish": "Brynden Tully",
        "Lady Mormont": "Maege Mormont",
        "King-beyond-the-wall": "Mance Rayder",
        "Daenerys Stormborn": "Daenerys Targaryen",
        "White Bull": "Gerold Hightower",
        "Aron": "Aron Santagar",
        "Aurochs": "Grenn",
        "Lady Sansa": "Sansa Stark",
        "Dickon": "Dickon Tarly", #ASOS
        "Danwell": "Danwell Frey",
        "Lord Walder Frey": "Walder Frey",
        "Lady Tanda": "Tanda Stokeworth",
        "Mychel": "Mychel Redfort",
        "Karyl": "Karyl Vance",
        "Sam Tarly": "Samwell Tarly",
        "Silver Lady": "Daenerys Targaryen",
        "Great Rider": "Khal Drogo",
        "Pod": "Podrick Payne",
        "Halfman": "Tyrion Lannister",
        "King Renly": "Renly Baratheon",
        "Jofftey": "Joffrey Baratheon",
        "Pypar": "Pyp",
        "Piggy": "Samwell Tarly",
        "Lord Jason": "Jason Mallister",
        "Lord Beric Dondarrion": "Beric Dondarrion",
        "Lancel": "Lancel Lannister",
        "Lord Bracken": "Jonos Bracken",
        "Lord Nestor Royce": "Nestor Royce",
        "Khal Raggat": "Viserys Targaryen",
        "Lord Jonos Bracken": "Jonos Bracken",
        "Princess Elia": "Elia Martell",
        "Princess Daenerys": "Daenerys Targaryen",
        "Elia": "Elia Martell",
        "Prince Joff": "Joffrey Baratheon",
        "Arya Horseface": "Arya Stark",
        "Uncle Ben": "Benjen Stark",
        "Catelyn Tully Stark": "Catelyn Stark",
        "Lord Tyrell": "Mace Tyrell",
        "Arya Underfoot": "Arya Stark",
        "Nan": "Old Nan",
        "Lord Randyll Tarly": "Randyll Tarly",
        "Lord Renly Baratheon": "Renly Baratheon",
        "Tobho": "Tobho Mott",
        "Master Mott": "Tobho Mott",
        "Lord Bryce Caron": "Bryce Caron",
        "Bronze Yohn": "Yohn Royce",
        "Uncle Brynden": "Brynden Tully",
        "Sorefoot King": "Viserys Targaryen",
        "Cart King": "Viserys Targaryen",
        "Lord Stannis Baratheon": "Stannis Baratheon",
        "Bronze Yohn Royce": "Yohn Royce",
        "Arys": "Arys Oakheart",
        "Lord Wyman": "Wyman Manderly",
        "Lord Tytos Blackwood": "Tytos Blackwood",
        "Prince Rhaegar": "Rhaegar Targaryen",
        "Lord Rickard Karstark": "Rickard Karstark",
        "Lady Ashara Dayne": "Ashara Dayne",
        "Margaery": "Margaery Tyrell",
        "Lord Yohn Royce": "Yohn Royce",
        "Bran": "Bran Stark",
        "Shaggy": "Shaggydog",
        "Maege": "Maege Mormont",
        "Lady Maege": "Maege Mormont",
        "Horas": "Horas Redwyne",
        "Hobber": "Hobber Redywne",
        "Queen Naerys": "Naerys Targaryen",
        "Lyn": "Lyn Corbray",
        "Lady Lysa Arryn": "Lysa Arryn",
        "Galbart": "Galbart Glover",
        "Dontos": "Dontos Hollard",
        "Harrion": "Harrion Karstark",
        "Podrick": "Podrick Payne",
        "Young Wolf": "Robb Stark"
        }

name_ambiguities = ["Ned", "Jon", "Robert", "Joffrey", "Rodrik", "Brandon",
        "Nymeria", "Eddard", "Jeyne", "Aegon", "Timett", "Benjen", "Tom", "Hal", "Samwell",
        "Donnel", "Marq", "Raymun", "Aemon", "Walder", "Robar", "Alyssa", "Torrhen", "Ben", "Hugh",
        "Tregar", "Gerold", "Addam", "Harys", "Willem", "Jaehaerys", "Oswell", "Tytos", "Wyl", "Balon",
        "Matt"]

last_names = ["Arryn", "Baratheon", "Blackwood", "Bracken", "Brax", 
        "Brune", "Clegane", "Corbray", "Crakehall", 
        "Darry", "Dondarrion", "Flint", "Flowers", "Florent", "Frey", 
        "Glover", "Greyjoy", "Hill", "Karstark",
        "Lannister", "Lefford", "Long", "Lydden", "Manderly", "Mallister",
        "Marsh", "Mormont", "Noye", "Payne", "Poole", "Pyke", "Redfort", "Redwyne", "Rowan"
        "Royce", "Rykker", "Selmy", "Slynt", "Snow", "Stark", "Stone", "Storm", "Strong", "Sweet",
        "Swyft", "Targaryen", "Tarly", "Thorne", "Tully", "Tyrell", "Waynwood"]

titles = ["Hand", "Dothraki", "Father", "Grace", "Mother", "Lord", "Lord Commander", "Khaleesi", "Lady",
        "Lady Stark", "Lord Arryn", "Lord Stark", "Knight", "Princess", "Protector", "Lord Jon",
        "Lord Karstark", "Warden", "Tyroshi", "King", "Black", "Lion", "Uncle", "Grand Maester",
        "Lord Robert", "Brandon Stark", "Lord Hunter", "Conqueror", "Maester", "Lord Rickard",
        "Commander", "Lord Steward", "Bastard", "Sword", "Lysene", "Lord Blackwood", "Justice",
        "Braavosi", "Septa", "Lord Cerwyn", "Lord Umber", "Lhazareen", "Aegon Targaryen", "Lord Hand",
        "Summer", "Pentoshi", "Sister", "Brother", "Unsullied"]

def increment_name(names, name, line):
    if not name or name in real_words:
        return
    if name in name_ambiguities:
        response = input("Which " + name + '? "' + line + '"\n')
        if response:
            name += " " + response.capitalize()
        else:
            return
    if name in last_names:
        response = input("Which " + name + '? "' + line + '"\n')
        if response:
            name = response.capitalize() + " " + name
        else:
            return
    if name in titles:
        response = input("Which " + name + '? "' + line + '"\n')
        if response:
            name = response.capitalize()
        else:
            return
    if name in name_translations:
        name = name_translations[name]
    print("got", name)
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

def main():
    filename = sys.argv[1]
    names = {}
    current_name = ""
    increment_once_done = False
    with open(filename, "r") as f:
        l = f.read().split("\n")
        for line in l:
            for word in line.split(" "):
                if not word:
                    if current_name:
                        print("adding", current_name)
                    increment_name(names, current_name, line)
                    current_name = ""
                    continue
                if not word[0].isalnum():
                    if current_name:
                        print("incrementing", current_name)
                    increment_name(names, current_name, line)
                    current_name = ""
                    while len(word) and not word[0].isalnum():
                        word = word[1:]
                if not word:
                    if current_name:
                        print("increasing", current_name)
                    increment_name(names, current_name, line)
                    current_name = ""
                    continue
                while not word[-1].isalnum():
                    increment_once_done = True
                    word = word[:-1]
                if word[-2:] == "’s":
                    increment_once_done = True
                    word = word[:-2]
                if not word[0].isupper() or word in real_words:
                    if current_name:
                        print("counting", current_name)
                    increment_name(names, current_name, line)
                    current_name = ""
                    increment_once_done = False
                    continue
                word = word.capitalize()
                if current_name:
                    current_name += " " + word
                else:
                    current_name = word
                if increment_once_done:
                    if current_name:
                        print("doing", current_name)
                    increment_name(names, current_name, line)
                    current_name = ""
                    increment_once_done = False
        for name in sorted(names, key=lambda name: names[name], reverse=True):
            print(name + ":", names[name])

if __name__ == "__main__":
    main()
