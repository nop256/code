def render_introduction():
    '''
    Create the message to be displayed at the start of your game.

    Returns:
        str: The introductory text of your game to be displayed.
    '''

def create_world():
    '''
    Creates a new version of the world in its initial state.

    Returns:
        World: The initial state of the world
    '''

def render(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.

    Args:
        world (World): The current world to describe.

    Returns:
        str: A textual description of the world.
    '''

def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.

    Args:
        world (World): The current world to get options for.

    Returns:
        list[str]: The list of commands that the user can choose from.
    '''

def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.

    Args:
        world (World): The current world to modify.

    Returns:
        str: A message describing the change that occurred in the world.
    '''

def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.

    Args:
        world (World): The final world state to use in describing the ending.

    Returns:
        str: The ending text of your game to be displayed.
    '''

def choose(options):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.

    Note:
        Use your answer to Programming Problem #42.3

    Args:
        options (list[str]): The potential commands to select from.

    Returns:
        str: The command that was selected by the user.
    '''

############# Main Function ##############
# Do not modify anything below this line #
##########################################
def main():
    '''
    Run your game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))

if __name__ == '__main__':
    main()
