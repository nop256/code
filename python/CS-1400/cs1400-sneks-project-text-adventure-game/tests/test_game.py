import ast
import io
import unittest
import unittest.mock

import asttest

test_worlds = [
        {
            "player": {"location": "A", "inventory": []},
            "map": {
                "A": {"neighbors": ["B"], "stuff": ["Z", "X"]},
                "B": {"neighbors": ["A"], "stuff": []}
            }
        },
        {
            "player": {"location": "asdf", "inventory": []},
            "map": {
                "asdf": {"neighbors": ["qwerty", "dvorak"], "stuff": ["foo", "bar"]},
                "qwerty": {"neighbors": ["asdf"], "stuff": []}
            }
        },
        ]

class TestGame(asttest.ASTTest):

    def setUp(self):
        super().setUp("game.py")

    def test_paths(self):
        import paths
        for path_name in ["WIN_PATH", "LOSE_PATH"]:
            with self.subTest(path=path_name):
                self.assertIn(path_name, dir(paths), "Do not remove the {} "
                        "variable from paths.py.".format(path_name))
                path = getattr(paths, path_name)
                self.assertGreater(len(path), 0, "You should add a {} to the {} "
                        "assignment statement in paths.py."
                        .format(path_name.lower().replace("_", " "), path_name))

                with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout, \
                        unittest.mock.patch("builtins.input", side_effect=path):
                    import game
                    try:
                        game.main()
                    except StopIteration:
                        self.fail("I got stuck while trying to execute your "
                                "{0}. This usually means that the path "
                                "contains a command that is not available at "
                                "the location the player ended up at after "
                                "entering the preceding commands. Make sure "
                                "you test out your {0} manually before "
                                "submitting.".format(path_name))
                    printed = mock_stdout.getvalue()
                    expected_result = path_name.lower().split('_')[0]
                    self.assertPassesTests(printed)
                    self.assertIn(expected_result, printed.lower(), "I did "
                            "not {0} when using the commands in your {1}. Either "
                            "your {1} is wrong or your game isn't quite right."
                            .format(expected_result, path_name))

        self.assertGreaterEqual(len(paths.WIN_PATH), 5, "Your game should be "
                "complex enough so that it takes at least 5 commands to win "
                "the game.")
        self.assertGreaterEqual(len(set(paths.WIN_PATH)), 2, "All of your "
                "commands in your win path should not be the same.")
        self.assertTrue(any([not cmd.lower().startswith("go") for cmd in paths.WIN_PATH]),
                "Your win path should have extra logic in it other than moving"
                " around the map. For example, you may require the play to "
                "pick up and use items to win the game.")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_get_options(self, mock_stdout):
        func = self.match_signature("get_options", 1)
        self.assertIsNotNone(func, "Do not change the def statement for the "
                "get_options function. You should only change its body")
        self.assertGreater(len(self.find_all(ast.List, func)), 0, "In the "
                "get_options function you should set up a list of "
                "commands/options for the user to eventually choose from.")
        self.assertGreater(len(self.find_all(ast.Return, func)), 0, "In the "
                "get_options function you should return a list of "
                "commands/options for the user to eventually choose from.")

        # 2. unit test (make sure "quit" is always in result)
        from game import get_options
        self.assertPassesTests(mock_stdout.getvalue())
        for world in test_worlds:
            # quit
            commands = get_options(world)
            self.assertHasCommand("quit", commands, "Your get_options() "
                    "function did not return the quit command.")
            # goto neighbors
            location = world["player"]["location"]
            for neighbor in world["map"][location]["neighbors"]:
                self.assertHasCommand(neighbor, commands, "Your "
                    "get_options() function does not allow me to freely move "
                    "around the map. It did not return a command to allow me "
                    "to move to each neighbor.")
            # extra logic
            """
            # Doesn't account for one-off commands using if statements
            for item in world["map"][location]["stuff"]:
                self.assertHasCommand(item, commands, "Your get_options() "
                        "function does not add enough extra logic. It did not "
                        "return any commands that allow me to interact with "
                        "the following item: " + item)
            """

    def assertHasCommand(self, cmd, cmds, msg):
        found = False
        for c in cmds:
            if cmd.lower() in c.lower():
                found = True
        self.assertTrue(found, msg)

    def test_update(self):
        func = self.match_signature("update", 2)
        self.assertIsNotNone(func, "Do not change the def statement for the "
                "update function. You should only change its body")
        self.assertGreater(len(self.find_all(ast.If, func)), 0, "In the "
                "update function you should use if statements to dynamically "
                "update the world in different ways depending on the command "
                "the user typed.")
        self.assertGreater(len(self.find_all(ast.Return, func)), 0, "In the "
                "update function you should return a status message "
                "that explains the result of performing a certain command.")


    def test_print_input(self):
        for func in self.find_all(ast.FunctionDef):
            if func.name in ["choose", "main"]:
                continue
            for call in self.find_all(ast.Call, func):
                if isinstance(call.func, ast.Name) and call.func.id in ["print", "input"]:
                    self.fail("You should not call the {} function in any "
                            "function besides choose() and main()."
                            .format(call.func.id))

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_world(self, mock_stdout):
        func = self.match_signature("create_world", 0)
        self.assertIsNotNone(func, "Do not change the def statement for the "
                "create_world function. You should only change its body")

        from game import create_world
        self.assertPassesTests(mock_stdout.getvalue())
        world = create_world()
        self.assertIsInstance(world, dict, "Your world should be a dictionary.")
        self.assertIn("map", world, "Your world should contain the map.")
        self.assertGreater(len(world["map"]), 4, "Your world map should be "
                "large enough to make the game interesting. This might mean "
                "having five or more locations in the map. Anything else "
                "should be approved by your instructor.")
        for place in world["map"]:
            self.assertGreater(len(world["map"][place]), 2, "Each location in "
                    "your map should have enough details (e.g., neighbors, "
                    "about, stuff) to make your game interesting. This might "
                    "mean having three or more different categories of details."
                    "Anything else should be approved by your instructor.")

    def test_imports(self):
        all_imports = self.find_all(ast.Import) + self.find_all(ast.ImportFrom)
        for import_ in all_imports:
            d = ast.dump(import_)
            if "cisc108" not in d and "random" not in d:
                self.fail("You should not import any external libraries to use"
                        " in the implementation of your game. Any exceptions "
                        "should be approved by your instructor."+ d)


    def assertPassesTests(self, printed):
        # Not sure why this assertion isn't failing in the other tests, so I
        # just put it everytime I import the file.
        self.assertNotIn("FAILURE - [line", printed,
                "You have failing unit tests.")

if __name__ == "__main__":
    unittest.main()
