import string
alphabet = "X7?#Y5$*QWE9R_T@U!IOPASDF8G&HJKLZCVBNM123460% "

common_words = ["THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", 
                "CAN", "HIS", "HER", "WAS", "WITH", "ON", "AS", "BY", 
                "AT", "FROM", "THIS", "THAT", "OR", "BE", "THEY", "I", 
                "MY", "ME", "OF", "IN", "IS", "IT", "TO", "A", "AM",
                "WAS", "WERE", "HAD", "DO", "DID", "SO", "FOR", "UP", "DOWN",
                "LEFT", "RIGHT", "OVER", "UNDER", "BEHIND", "IN FRONT OF",
                "ABOVE", "BELOW", "NEAR", "FAR", "BETWEEN", "AMONG", "THROUGH",
                "ACROSS", "AROUND", "TOWARDS", "AWAY FROM", "OUT OF", "INTO",
                "ONTO", "OFF", "OVER", "UNDER", "BEHIND", "IN FRONT OF",
                "LORD", "GOD", "KING", "QUEEN", "PRINCE", "PRINCESS", "DUKE", "DUCHESS",
                "SIR", "LADY", "MR", "MRS", "MS", "DR", "PROFESSOR", "DOCTOR", "CAPTAIN", "SERGEANT", "PRIVATE",
                "POLICE", "FIRE", "EMT", "TEACHER", "STUDENT", "WORKER", "BOSS", "EMPLOYEE",
                "FRIEND", "FAMILY", "LOVER", "ENEMY", "NEIGHBOR", "COLLEAGUE", "STRANGER",
                "ANIMAL", "PET", "DOG", "CAT", "BIRD", "FISH", "HORSE", "COW", "SHEEP", "PIG",
                "ALEX", "PROGRAMMER", "PYTHON", "IS", "NOT", "FLY","AWAY", "NOW",
                "LATER", "SOON", "NEVER", "ALWAYS", "SOMETIMES", "OFTEN", "RARELY", "USUALLY",
                "HAPPY", "SAD", "ANGRY", "EXCITED", "BORED", "TIRED", "SCARED", "CONFUSED", "SURPRISED", "DISGUSTED",
                "LOVE", "HATE", "LIKE", "DISLIKE", "ADORE", "DESPISE", "RESPECT", "FEAR", "TRUST", "ENVY",
                "SMILE", "FROWN", "LAUGH", "CRY", "SHOUT", "WHISPER", "SING", "DANCE", "RUN", "WALK"
                "HELLO", "GOODBYE", "PLEASE", "THANK", "SORRY", "YES", "NO", "MAYBE", "ALRIGHT", "OKAY"
                "DAY", "NIGHT", "MORNING", "AFTERNOON", "EVENING", "WEEK", "MONTH", "YEAR", "TIME", "HOUR"
                "SHALL", "WILL", "MUST", "CAN", "COULD", "MAY", "MIGHT", "WOULD", "SHOULD", "DID", "SUCCEDED", 
                "FAILED", "WIN", "LOSE", "VICTORY", "DEFEAT", "SUCCESS", "FAILURE", "TRIUMPH", "DISASTER", "SUCCEED"
                "LONG", "SHORT", "TALL", "SMALL", "BIG", "LARGE", "HUGE", "MINIATURE", "GIGANTIC", "TINY"
                "ENOUGH", "TOO MUCH", "TOO LITTLE", "SUFFICIENT", "INSUFFICIENT", "PLENTY", "SCARCE", "ABUNDANT", "MEAGER"
                "PERHAPS", "CERTAINLY", "DEFINITELY", "PROBABLY", "POSSIBLY", "UNLIKELY", "LIKELY", "SURELY", "DOUBTLESSLY"
                "WHAT", "WHERE", "WHEN", "WHY", "HOW", "WHICH", "WHO", "WHOM", "WHOSE", "WHATEVER"
                "NOUN", "VERB", "ADJECTIVE", "ADVERB", "PRONOUN", "PREPOSITION", "CONJUNCTION", "INTERJECTION"
                "JAB", "CROSS", "HOOK", "UPPERCUT", "SLIP", "DODGE", "BLOCK", "PARRY", "FEINT", "COMBO", "KNOCKOUT"
                "THEY'RE", "WE'RE", "YOU'RE", "IT'S", "I'M", "HE'S", "SHE'S", "THAT'S", "WHAT'S", "WHERE'S"
                "DON'T", "CAN'T", "WON'T", "SHOULDN'T", "COULDN'T", "WOULDN'T", "MUSTN'T", "HAVEN'T", "ISN'T", "AREN'T"
                "IDK", "TBH", "BRB", "GG", "I'LL", "YOU'LL", "HE'LL", "SHE'LL", "WE'LL", "THEY'LL", "I'VE", "YOU'VE", 
                "HE'S", "SHE'S", "WE'VE", "THEY'VE", "BED", "TABLE", "CHAIR", "SOFA", "LAMP", "DOOR", "WINDOW", "FLOOR", "CEILING", "WALL",
                "CAR", "BIKE", "BUS", "TRAIN", "PLANE", "BOAT", "SHIP", "SUBMARINE", "SPACESHIP", "ROCKET", "ANYONE", "EVERYONE", "SOMEONE", 
                "NO ONE", "NOBODY", "EVERYBODY", "ANYBODY", "SOMEBODY", "ANYWHERE", "EVERYWHERE"]

def count_english_matched(text):
    text = text.upper()
    matched_words = 0
    words = text.split("")
    for word in words:
        clean_word = word.strip(string.punctuation)
        if clean_word in common_words:
            matched_words += 1
    return matched_words
