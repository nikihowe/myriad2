from dataclasses import dataclass
from enum import Enum


class DynamicsType(Enum):
  CARTPOLE = "CARTPOLE"
  VANDERPOL = "VANDERPOL"
  SEIR="SEIR"


class SolutionType(Enum):
  COLLOCATION = "COLLOCATION"


# Hyperparameters which change experiment results
@dataclass(eq=True, frozen=True)
class HParams:
  seed: int = 2020
  dynamics: DynamicsType = DynamicsType.CARTPOLE
  solution: SolutionType = SolutionType.COLLOCATION
  slsqp_maxiter: int = 1000
  collocation_segments: int = 25


# Secondary configurations which do not change experiment results
@dataclass(eq=True, frozen=True)
class Config():
  verbose: bool = True
  plot_results: bool = True
