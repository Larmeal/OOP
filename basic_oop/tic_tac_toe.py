class TicTacToeGame:
    def __init__(self) -> None:
        self.player_1_char = ""
        self.player_2_char = ""
        self.player_pattern = {"|x|": [], "|o|": []}
        self.player_score = {"|x|": 0, "|o|": 0}
        self.again = {"1": "YES", "2": "NO"}
        self.player_input = 0
        self.game_stage = 0
        self.board = [
            "| |",
            "| |",
            "| |",
            "\n\t    ",
            "| |",
            "| |",
            "| |",
            "\n\t    ",
            "| |",
            "| |",
            "| |",
        ]
        self.board_status = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]

    def welcome_menu(self):
        print(
            """
            ******************************
                Welcome to Tic-Tac-Toe  
            ******************************
            """
        )

    def game_interface(self):
        self.example_board = """
        Position:
            |1||2||3|
            |4||5||6|
            |7||8||9|
        """
        self.web_ui = f"""
        Board:
            {"".join(self.board)}
        """
        print(
            f"""
            {self.example_board}
            {self.web_ui}
            """
        )

    def _move_validation(self, player_input):
        if player_input > 9 or player_input < 1:
            print("The position should be less than or equal to 9 and more than 0")
        elif self.board_status[player_input - 1] == 1:
            print("This position is already taken. Please enter another one.")
            self.player_input = 0

    def _character_validation(self, player):
        character = {"1": "|x|", "2": "|o|"}
        if isinstance(player, int) and (player < 1 or player > 2):
            print("Your character not exist, please choose your character again.")
        else:
            self.player_1_char = character[str(player)]
            character.pop(str(player))
            self.player_2_char = character[list(character.keys())[0]]

    def condition_win(self, player):
        win_pattern = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (3, 5, 7),
        ]

        for pattern in win_pattern:
            if set(pattern).issubset(set(self.player_pattern[player])):
                self.game_stage = 999

    def update_player_pattern(self, player, player_input):
        self.player_pattern[player].append(player_input)

    def update_interface(self, player_input, player):
        self.board_status[player_input - 1] = 1
        self.player_input = player_input

        if player_input <= 3:
            player_input -= 1
        elif player_input > 3 and player_input <= 6:
            player_input = player_input
        else:
            player_input += 1

        self.board[player_input] = player

    def continue_the_game(self, player):
        self.player_score[player] += 1
        print(
            f"""
                Awesome. Player {self.player[1]} won the game! 🎉
                with score {self.player_score[self.player]} - {self.player_score["|o|" if self.player == "|x|" else "|x|"]}
            """
        )
        continue_stage = int(
            input("Would you like to play again? Enter 1 for 'YES' or 2 for 'NO': ")
        )
        if isinstance(continue_stage, int) and (
            continue_stage < 1 or continue_stage > 2
        ):
            print("Please choose your answer again.")
        elif continue_stage == 1:
            self.game_stage = 0
            self.board = [
                "| |",
                "| |",
                "| |",
                "\n\t    ",
                "| |",
                "| |",
                "| |",
                "\n\t    ",
                "| |",
                "| |",
                "| |",
            ]
            self.board_status = [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ]
            self.player_pattern = {"|x|": [], "|o|": []}
        else:
            self.game_stage = 999

    def start_game(self):
        self.welcome_menu()
        self.game_interface()
        while self.player_1_char == "":
            self.player = int(
                input("Please enter your character 1 for 'x' and 2 for 'o': ")
            )
            self._character_validation(self.player)

        while self.game_stage < 9:
            self.player_input = 0
            if self.game_stage % 2 == 0:
                self.player = self.player_1_char
            else:
                self.player = self.player_2_char

            while self.player_input not in (range(1, 10)):
                self.player_input = int(
                    input(f"Player: {self.player[1]}, please enter your move (1-9): ")
                )
                self._move_validation(self.player_input)

            self.update_interface(self.player_input, player=self.player)
            self.update_player_pattern(
                player=self.player, player_input=self.player_input
            )
            self.game_interface()
            if self.game_stage >= 3:
                self.condition_win(player=self.player)

            self.game_stage += 1
            if self.game_stage > 9:
                self.continue_the_game(player=self.player)


game = TicTacToeGame()
game.start_game()
