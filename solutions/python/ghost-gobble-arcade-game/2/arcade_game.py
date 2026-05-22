"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Return True if Pac-Man can eat a ghost."""
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Return True if Pac-Man scores."""
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Return True if Pac-Man loses the game."""
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Return True if Pac-Man wins the game."""
    safe_from_ghost = not touching_ghost or power_pellet_active
    return has_eaten_all_dots and safe_from_ghost