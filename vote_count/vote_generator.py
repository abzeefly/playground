from typing import Generator
from enum import Enum
import random

class Candidates(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'


class VoteGenerator:
    def __init__(self, candidates: list[Candidates]):
        self.candidates = candidates
    def generate(self, num_votes: int) -> Generator[Enum, None, None]:
        for _ in range(num_votes):
            yield  random.choice(list(self.candidates))

vote_generator = VoteGenerator(Candidates)

num_votes_to_generate = 10
generated_votes = list(vote_generator.generate(num_votes_to_generate))

print("Generated Votes:", generated_votes)