# DiceRoll
================
## Introduction
DiceRoll is a Python library designed to simulate the roll of various types of dice. It provides a simple and intuitive way to generate random numbers within a specified range, making it perfect for games, statistical analysis, and more.

## Features
- **Multi-sided dice support**: Roll dice with any number of sides, from 2 to infinity.
- **Customizable roll results**: Control the number of rolls, the type of dice, and the output format.
- **Seeding for reproducibility**: Set a seed for the random number generator to reproduce specific results.
- **Statistical analysis tools**: Calculate means, medians, modes, and standard deviations of roll results.

## Installation
To install DiceRoll, run the following command:
```bash
pip install dice-roll
```
## Usage
### Basic Example
To roll a single six-sided die:
```python
from dice_roll import DiceRoll

# Create a DiceRoll object
roller = DiceRoll()

# Roll a single six-sided die
result = roller.roll(6)

print(f"You rolled a {result}")
```
### Advanced Example
To roll multiple twenty-sided dice and calculate the mean of the results:
```python
from dice_roll import DiceRoll

# Create a DiceRoll object with a seed for reproducibility
roller = DiceRoll(seed=123)

# Roll 5 twenty-sided dice
results = roller.roll(20, num_rolls=5)

# Calculate the mean of the results
mean_result = sum(results) / len(results)

print(f"You rolled: {results}")
print(f"Mean result: {mean_result}")
```
### Using DiceRoll with Other Libraries
DiceRoll can be used in conjunction with other libraries, such as Pandas for data analysis and matplotlib for visualization.

```python
import pandas as pd
import matplotlib.pyplot as plt
from dice_roll import DiceRoll

# Create a DiceRoll object
roller = DiceRoll()

# Roll 100 six-sided dice
results = roller.roll(6, num_rolls=100)

# Create a Pandas DataFrame from the results
df = pd.DataFrame(results, columns=['Roll'])

# Calculate the mean and standard deviation of the results
mean_result = df['Roll'].mean()
std_dev = df['Roll'].std()

# Print the results
print(f"Mean result: {mean_result}")
print(f"Standard deviation: {std_dev}")

# Visualize the results with a histogram
plt.hist(results, bins=6, edgecolor='black')
plt.xlabel('Roll Value')
plt.ylabel('Frequency')
plt.title('Histogram of Roll Results')
plt.show()
```
## Statistical Analysis
DiceRoll includes tools for calculating various statistical metrics, including:

* **Mean**: The average value of a set of rolls.
* **Median**: The middle value of a set of rolls when sorted in ascending order.
* **Mode**: The most frequently occurring value in a set of rolls.
* **Standard Deviation**: A measure of the spread or dispersion of a set of rolls.

### Example Statistical Analysis
To calculate the mean, median, mode, and standard deviation of 100 six-sided dice rolls:
```python
from dice_roll import DiceRoll

# Create a DiceRoll object
roller = DiceRoll()

# Roll 100 six-sided dice
results = roller.roll(6, num_rolls=100)

# Calculate the mean
mean_result = sum(results) / len(results)

# Calculate the median
median_result = sorted(results)[len(results) // 2]

# Calculate the mode
mode_result = max(set(results), key=results.count)

# Calculate the standard deviation
std_dev = (sum((x - mean_result) ** 2 for x in results) / len(results)) ** 0.5

# Print the results
print(f"Mean result: {mean_result}")
print(f"Median result: {median_result}")
print(f"Mode result: {mode_result}")
print(f"Standard deviation: {std_dev}")
```
## Comparison to Other Libraries
The following table compares DiceRoll to other popular Python libraries for simulating dice rolls:

| Library | Features | Ease of Use | Performance |
| --- | --- | --- | --- |
| DiceRoll | Multi-sided dice, customizable roll results, seeding for reproducibility, statistical analysis tools | 9/10 | 9/10 |
| random | Basic random number generation, no dice-specific features | 5/10 | 8/10 |
| numpy.random | Advanced random number generation, no dice-specific features | 6/10 | 9/10 |
| scipy.stats | Statistical analysis tools, no dice-specific features | 7/10 | 8/10 |

### Mermaid Diagram
```mermaid
graph LR
    A[DiceRoll] -->|uses|> B[Random Number Generator]
    A -->|provides|> C[Multi-sided Dice Support]
    A -->|provides|> D[Customizable Roll Results]
    A -->|provides|> E[Seeding for Reproducibility]
    A -->|provides|> F[Statistical Analysis Tools]
    B -->|generates|> G[Random Numbers]
    C -->|simulates|> H[Dice Rolls]
    D -->|allows|> I[Custom Roll Results]
    E -->|enables|> J[Reproducible Results]
    F -->|calculates|> K[Statistical Metrics]
```
## Contributing
To contribute to DiceRoll, please fork the repository and submit a pull request with your changes. Ensure that your code is well-documented and follows the existing style.

## License
DiceRoll is licensed under the MIT License.

## Acknowledgments
DiceRoll was inspired by various online resources and libraries, including the Python `random` module and the `scipy.stats` library.

## Future Development
Future development plans for DiceRoll include:

* **Adding support for different probability distributions**: Allow users to specify the probability distribution for dice rolls.
* **Improving performance**: Optimize the random number generator for faster performance.
* **Adding more statistical analysis tools**: Include additional statistical metrics and analysis tools.

## Conclusion
DiceRoll is a powerful and flexible Python library for simulating dice rolls and analyzing the results. With its customizable roll results, seeding for reproducibility, and statistical analysis tools, it is ideal for games, statistical analysis, and more. Whether you're a seasoned developer or just starting out, DiceRoll is an excellent choice for any project that requires simulating dice rolls.