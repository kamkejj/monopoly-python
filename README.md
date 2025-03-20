# Monopoly Simulation

A comprehensive simulation of the classic Monopoly game that tracks game statistics including landing spots and dice combinations.

## Features

- Simulates multiple players moving around a Monopoly board
- Implements official Monopoly rules including:
  - Rolling doubles to get another turn
  - Going to jail after rolling 3 doubles in a row
  - Jail mechanics (getting out with doubles or after 3 turns)
- Tracks detailed statistics:
  - Landing spot frequencies for each property
  - Dice roll combinations and their frequencies
  - Percentage of doubles rolled
- Saves statistics to CSV files for further analysis
- Generates visualizations of game statistics

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Required packages for visualizations (automatically installed when running the visualization script):
  - pandas
  - matplotlib
  - seaborn
  - numpy

### Running the Simulation

1. Clone this repository or download the source code
2. Navigate to the project directory
3. Run the simulation:

```bash
python main.py
```

4. Follow the prompts to specify:
   - Number of rounds to play
   - Number of players
   - Player names

5. The simulation will run and display the results in the terminal, including:
   - Each player's moves and dice rolls
   - Landing spot statistics
   - Dice roll statistics
   - Summary statistics

### Viewing and Analyzing Statistics

After running the simulation, statistics are automatically saved to CSV files in the `stats/data` directory:
- `property_stats.csv`: Records how many times players landed on each property
- `dice_stats.csv`: Records the frequency of each dice combination

Each game's statistics are appended to these files, allowing for analysis across multiple games.

### Generating Visualizations

To generate visualizations from the collected statistics:

```bash
cd stats
python visualize_stats.py
```

This will create several visualization images in the `stats/data` directory:

#### Property Visualizations
- `property_landing_frequency.png`: Bar chart of most frequently landed-on properties
- `property_heatmap.png`: Heatmap of the Monopoly board showing landing frequencies
- `property_by_game_size.png`: Line chart comparing property frequencies across different game sizes

#### Dice Visualizations
- `dice_combinations.png`: Heatmap of dice combinations
- `dice_sums.png`: Bar chart of dice sums with theoretical probability overlay
- `doubles_percentage.png`: Pie chart showing doubles vs. non-doubles percentage
- `doubles_percentage_distribution.png`: Histogram of doubles percentages across games

## Project Structure

- `main.py`: Main entry point for the simulation
- `models/`: Contains the core game models
  - `board.py`: Defines the Monopoly board structure
  - `player.py`: Defines the Player class
- `game/`: Contains game logic
  - `game_logic.py`: Implements the Game class and core game mechanics
- `stats/`: Contains statistics tracking and visualization
  - `visualize_stats.py`: Main script for generating visualizations
  - `visualize_properties.py`: Property statistics visualizations
  - `visualize_dice.py`: Dice statistics visualizations
  - `data/`: Directory for CSV data and generated visualizations

## References

- [Official Monopoly Rules](https://www.hasbro.com/common/en_US/pdf/monopoly-2019.pdf)
- [Monopoly Rules on Wiki Books](https://en.wikibooks.org/wiki/Monopoly/Official_Rules)