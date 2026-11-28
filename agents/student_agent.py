"""Student agent: edit ONLY this file."""
from agents.agent import Agent
from store import register_agent
from helpers import (Move, get_valid_moves, execute_move, check_winner,
                     check_endgame, random_move, copy_state, top_view)
from constants import *
import numpy as np
import time

INF = 1000000
WIN = 1000000
TIME_LIMIT = 1.6

class SearchTimeOut(Exception):
    pass

@register_agent("student_agent")          # do not change this string
class StudentAgent(Agent):
    def __init__(self):
        """Set up your agent. This runs once per game, before the first move, and must finish
        within INIT_TIME_LIMIT seconds."""
        super().__init__()
        self.name = "StudentAgent"

    def step(self, board, reserves, player, opponent):
        """Return the Move you want to play.

        Takes: board, reserves - your own copies of the current position.
               player, opponent - your player number (1 or 2) and the other one.
        Agent.step in agents/agent.py explains each argument and the time limit.
        """
        start = time.perf_counter()
        # ALLOW_MOVES and WIN_LENGTH (from constants) are the rule flags of this game.
        # helpers.get_valid_moves / check_winner already respect them; your own
        # move generator and evaluation function must too.
        # TODO: replace with your search. Keep (time.perf_counter() - start) < STEP_TIME_LIMIT - margin.
        return random_move(board, reserves, player)

    def alpha_beta():
        """
        Placeholder for now
        """
        move = None
        score = 0
        return move, score

    def iterative_deepening(self, board, reserves, player, ply, moves_order):
        """
        Search depth by depth until time runs out and keep the best move of last depth
        """
        init_time = time.perf_counter()
        best_move = moves_order[0]
        score = 0
        ply_left = MAX_PLIES - ply
        depth = 1

        while (depth <= ply_left) and (time.perf_counter()-init_time < TIME_LIMIT):
            try:
                move, score = self.alpha_beta()
            except SearchTimeOut:
                break

            best_move = move
            
            #reorder to optimize alpha beta pruning
            moves = [move]
            for m in moves_order:
                if m != move:
                    moves.append(m)
            moves_order = moves

            if abs(score) > WIN - 1000:
                break
            depth += 1

        return best_move