# HW16 - Searching for an Offense
#
"""
We have stats on 99 quarterbacks from the NCAA website (more detail on Blackboard)
about the name, school, games played, pass attempts, pass completions, pass
touchdowns, and pass yards for each.

The file is already sorted alphabetically by name. Fill in the undone methods on
the Player methods and the other functions, then complete the tasks.
"""

class Player:
    def __init__(self, name, school, games, attempts, completions, touchdowns, yards):
        self.name = name
        self.school = school
        self.games = games
        self.attempts = attempts
        self.completions = completions
        self.touchdowns = touchdowns
        self.yards = yards

    def completion_pct(self):
        """Return completions divided by attempts, as a percentage.
        Ex: 105 completions on 149 attempts -> 70.47..."""
        # return 100 * (self.completions / self.attempts)
        pass

    def yards_per_game(self):
        """Return passing yards divided by games played."""
        
        pass

    def display(self):
        """Print one line. Show percentages and per-game yards to 1 decimal place.
        Ex: Aaron Philo (Florida): 1341 yds, 9 TD, 70.5% comp, 223.5 yds/game"""
        pass

def sequential_search(players, target_name):
    """Check each player in order, starting at index 0, until one's
    name matches target_name. Keep track of the comparisons made.
    Print the number of comparisons made, then return the index of the
    match, or -1 if there isn't a match.
    Ex output:   Sequential search: 7 comparisons"""
    pass


def binary_search(players, target_name):
    """Binary search the list (which must be sorted by name) for target_name.
    IMPORTANT: compare the LOWERCASE versions of the names, using .lower()
    on both the target and each player's name (see Question 3).
    Keep track of the number of comparisons. Print the number of comparisons made, 
    then return the index of the match, or -1 if not found.
    Ex output:   Binary search: 6 comparisons"""
    pass


def selection_sort_by_yards(players):
    """Sort the list using selection sort, from MOST passing yards
    to FEWEST. Compare the players' yards attributes, but swap the
    Quarterback objects themselves. Return the list of players sorted"""
    pass


def bubble_sort_by_completion(players):
    """Sort the list using bubble sort, from HIGHEST completion
    percentage to LOWEST. Compare the values returned by completion_pct().
    Return the list of players sorted."""
    pass


# ---- Main program ----

# TASK 1: Load the data.
#   Open qb_stats.csv and skip the header line. For each remaining line,
#   create a Quarterback object (convert the five numbers to int) and add it
#   to a list called qbs. Print how many quarterbacks were loaded.

# TASK 2: Look up players.
#   For each name in the list below, call sequential_search() AND
#   binary_search(). Then display the player, or print "Not found".
lookups = ["Aaron Philo", "Arch Manning", "LaNorris Sellers",
           "Cj Carr", "Will Hammond", "Tim Tebow"]

# TASK 3: Top 10 by passing yards.
#   Sort the players by passing yards using the selection sort.
#   Print the top 10 players by passing yards (using display)

# TASK 4: Top 10 by completion percentage.
#   Sort the players by completion percentage using the bubble sort.
#   Print the top 10 players by completion percentage (using display)

# TASK 5: Find every quarterback with at least 15 touchdowns AND a
#   completion percentage of at least 70%. Display each one, then print
#   how many were found.