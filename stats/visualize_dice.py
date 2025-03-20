#!/usr/bin/env python3
"""
Visualize Monopoly dice statistics from CSV data.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (14, 8)

def load_dice_data():
    """Load dice statistics from CSV file."""
    csv_path = os.path.join("data", "dice_stats.csv")
    if not os.path.exists(csv_path):
        print(f"Error: Could not find {csv_path}")
        return None
    
    return pd.read_csv(csv_path)

def visualize_dice_combinations(df):
    """Create a heatmap of dice combinations."""
    # Create a pivot table for the dice combinations
    dice_matrix = np.zeros((6, 6))
    
    # Group by dice1 and dice2 and calculate the mean count
    for _, row in df.iterrows():
        dice1 = int(row['dice1']) - 1  # Adjust for 0-indexing
        dice2 = int(row['dice2']) - 1  # Adjust for 0-indexing
        dice_matrix[dice1, dice2] = row['count']
    
    # Create the heatmap
    plt.figure(figsize=(12, 10))
    ax = sns.heatmap(dice_matrix, annot=True, fmt=".1f", cmap="YlOrRd", 
                     linewidths=.5, cbar_kws={'label': 'Frequency'})
    
    # Add labels
    ax.set_xticklabels([1, 2, 3, 4, 5, 6])
    ax.set_yticklabels([1, 2, 3, 4, 5, 6])
    plt.xlabel('Second Die', fontsize=14)
    plt.ylabel('First Die', fontsize=14)
    plt.title('Frequency of Dice Combinations', fontsize=18)
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join("data", "dice_combinations.png"))
    plt.close()
    
    print(f"Saved dice combinations visualization to data/dice_combinations.png")

def visualize_dice_sums(df):
    """Create a bar plot of dice sum frequencies."""
    # Group by sum and calculate the mean count
    sum_counts = df.groupby('sum')['count'].mean().reset_index()
    
    # Create the plot
    plt.figure(figsize=(14, 8))
    ax = sns.barplot(x='sum', y='count', data=sum_counts, palette='viridis')
    
    # Add labels and title
    plt.title('Average Frequency of Dice Sums', fontsize=18)
    plt.xlabel('Dice Sum', fontsize=14)
    plt.ylabel('Average Frequency', fontsize=14)
    
    # Add count values above each bar
    for i, v in enumerate(sum_counts['count']):
        ax.text(i, v + 1, f"{v:.1f}", ha='center')
    
    # Add theoretical probability line
    theoretical_probs = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    
    # Calculate the expected count based on the total rolls
    total_avg_rolls = sum_counts['count'].sum()
    expected_counts = [theoretical_probs[i] * total_avg_rolls for i in range(2, 13)]
    
    # Add the expected line
    plt.plot(range(len(expected_counts)), expected_counts, 'r--', label='Theoretical Probability')
    plt.legend()
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join("data", "dice_sums.png"))
    plt.close()
    
    print(f"Saved dice sums visualization to data/dice_sums.png")

def visualize_doubles_percentage(df):
    """Create a pie chart showing the percentage of doubles rolled."""
    # Add a column to identify doubles
    df['is_double'] = df['dice1'] == df['dice2']
    
    # Group by game (timestamp, rounds, players) and calculate doubles percentage
    game_stats = df.groupby(['timestamp', 'rounds', 'players']).apply(
        lambda x: pd.Series({
            'total_rolls': x['count'].sum(),
            'doubles_count': x[x['is_double']]['count'].sum(),
        })
    ).reset_index()
    
    game_stats['doubles_percentage'] = (game_stats['doubles_count'] / game_stats['total_rolls']) * 100
    
    # Calculate the average doubles percentage
    avg_doubles_pct = game_stats['doubles_percentage'].mean()
    
    # Create the pie chart
    plt.figure(figsize=(10, 10))
    plt.pie([avg_doubles_pct, 100 - avg_doubles_pct], 
            labels=['Doubles', 'Non-Doubles'],
            autopct='%1.2f%%',
            colors=['#ff9999','#66b3ff'],
            startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('Average Percentage of Doubles Rolled', fontsize=18)
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join("data", "doubles_percentage.png"))
    plt.close()
    
    print(f"Saved doubles percentage visualization to data/doubles_percentage.png")
    
    # Create a histogram of doubles percentages across games
    plt.figure(figsize=(12, 8))
    sns.histplot(game_stats['doubles_percentage'], kde=True, bins=10)
    plt.axvline(x=16.67, color='r', linestyle='--', label='Expected (16.67%)')
    plt.title('Distribution of Doubles Percentages Across Games', fontsize=18)
    plt.xlabel('Doubles Percentage', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend()
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join("data", "doubles_percentage_distribution.png"))
    plt.close()
    
    print(f"Saved doubles percentage distribution to data/doubles_percentage_distribution.png")

def main():
    """Main function to run all visualizations."""
    # Create the data directory if it doesn't exist
    os.makedirs(os.path.join("data"), exist_ok=True)
    
    # Load the data
    df = load_dice_data()
    if df is None:
        return
    
    # Run visualizations
    visualize_dice_combinations(df)
    visualize_dice_sums(df)
    visualize_doubles_percentage(df)
    
    print("All dice visualizations complete!")

if __name__ == "__main__":
    main()
