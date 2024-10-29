def getExpRequiredToLevelUp(level:int) -> int:
    """
    Get the required experience to level up from the current level.
    
    Args:
        level (int) : Current level. Must be positive
    Returns:
        int: The required exp to level up

    Raises:
        ValueError: If level is not positive
    """
    if not (0 <= level):
        raise ValueError("level must be positive.")

    XP_BASE_VALUE = 325
    XP_COEFFICIENT = 1.041
    XP_MINUS = 188

    return round(XP_BASE_VALUE * (XP_COEFFICIENT ** (level + 1)) - XP_MINUS)

def expToLevel(exp:int) -> int:
    """Return the level from the total experience.
    
    Args:
        exp (int) : The total experience. Must be superior or equal to 0.
        
    Returns:
        int: The level
    
    Raises:
        ValueError: If exp is negative
    
    """
    if exp < 0:
        raise ValueError("level must be a positive value.")
    level = 0

    while exp >= getExpRequiredToLevelUp(level):
        exp -= getExpRequiredToLevelUp(level)
        level += 1
    return level

def levelToExp(level:int) -> int:
    """
    Return the total required experience to achieve this level.
    
    Args:
        level (int) : The level. Must be positive
        
    Returns:
        int: The total required exp to achieve this level
        
    Raises:
        ValueError: If level is negative
    """
    if not (0 <= level):
        raise ValueError("level must be positive.")
    
    exp = 0
    i = 0
    
    while level > 0:
        level -= 1
        exp += getExpRequiredToLevelUp(i)
        i += 1
    return exp
