def getGuildExpRequiredToLevelUp(guildLevel:int) -> int:
    """
    Get the required experience for the guild to level up from its current level.
    
    Args:
        guildLevel (int) : Current level of the guild. Must be between 0 and 149 included
    
    Returns:
        int: The required exp for the guild to level up

    Raises:
        ValueError: If guildLevel is not between 0 and 149 included
    """
    if not (0 <= guildLevel <= 149):
        raise ValueError("guildLevel must be between 0 and 149.")

    XP_BASE_VALUE = 325
    XP_COEFFICIENT = 1.041
    XP_MINUS = 188

    return round(XP_BASE_VALUE * (XP_COEFFICIENT ** (guildLevel + 1)) - XP_MINUS)

def guildExpToGuildLevel(guildExp:int) -> int:
    """Return the guild level from its total experience.
    
    Args:
        guildExp (int) : The total experience of the guild. Must be superior or equal to 0.
        
    Returns:
        int: The guild level
    
    Raises:
        ValueError: If guildExp is negative
    
    """
    if guildExp < 0:
        raise ValueError("guildLevel must be a positive value.")
    guildLevel = 0

    while guildExp >= getGuildExpRequiredToLevelUp(guildLevel) and guildLevel < 150:
        guildExp -= getGuildExpRequiredToLevelUp(guildLevel)
        guildLevel += 1
    return guildLevel

def guildLevelToGuildExp(guildLevel:int) -> int:
    """
    Return the total required experience for the guild to achieve its level.
    
    Args:
        guildLevel (int) : The level of the guild. Must be superior to 0, inferior or equal to 150.
        
    Returns:
        int: The total required guild exp to achieve its level
        
    Raises:
        ValueError: If guildLevel is not between 0 and 150 included
    """
    if not (0 <= guildLevel <= 159):
        raise ValueError("guildLevel must be between 0 and 150 included.")
    
    guildExp = 0
    i = 0
    
    while guildLevel > 0:
        guildLevel -= 1
        guildExp += getGuildExpRequiredToLevelUp(i)
        i += 1
    return guildExp
