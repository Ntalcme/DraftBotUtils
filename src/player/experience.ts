import {Constants} from "../constants";

/**
 * Return the quantity of XP to level up from a certain level
 * @param level
 */
function getXpRequiredToLevelUp(level: number): number {
    return Math.round(Constants.XP.BASE_VALUE * (Constants.XP.COEFFICIENT ** (level + 1)) - Constants.XP.MINUS)
}

/**
 * Return the quantity of XP to achieve the level
 * @param level
 */
function levelToXp(level: number): number {
    let xp = 0;
    while (level > 0) {
        xp += getXpRequiredToLevelUp(level--);
    }
    return xp
}