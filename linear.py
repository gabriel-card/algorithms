# coding in: utf-8
from typing import List, Tuple, Callable
Coordinates = List[Tuple[int]]
X = 0
Y = 1

def linear_regression(coordinates: Coordinates) -> Callable:
  observations_length = len(coordinates)
  sum_of_x = sum([coordinate[X] for coordinate in coordinates])
  sum_of_y = sum([coordinate[Y] for coordinate in coordinates])
  sum_of_xy = sum([coordinate[X] * coordinate[Y] for coordinate in coordinates])
  sum_of_x_power2 = sum([coordinate[X] ** 2 for coordinate in coordinates])

  slope = ((observations_length * sum_of_xy) - (sum_of_x * sum_of_y)) / ((observations_length * sum_of_x_power2) - sum_of_x ** 2)

  interception = (sum_of_y - (slope * sum_of_x)) / observations_length

  def predict(x: int) -> float:
    return (slope * x) + interception
  return predict


print(linear_regression([(1,10), (2,20), (3,30), (4,40)])(100))
