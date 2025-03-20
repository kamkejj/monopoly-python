#!/usr/bin/env python3
"""
Visualize Monopoly property statistics from CSV data.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (14, 8)

def load_property_data():
    """Load property statistics from CSV file."""
    csv_path = os.path.join("data", "property_stats.csv")
    if not os.path.exists(csv_path):
        print(f"Error: Could not find {csv_path}")
        return None
    
    return pd.read_csv(csv_path)

def visualize_landing_frequency(df):
    """Create a bar plot of landing frequencies for all properties."""
    # Group by property_name and calculate the mean count
    property_avg = df.groupby('property_name')['count'].mean().reset_index()
    property_avg = property_avg.sort_values('count', ascending=False)
    
    # Create the plot
    plt.figure(figsize=(16, 10))
    ax = sns.barplot(x='count', y='property_name', data=property_avg, palette='viridis')
    
    # Add labels and title
    plt.title('Average Landing Frequency by Property', fontsize=18)
    plt.xlabel('Average Number of Landings', fontsize=14)
    plt.ylabel('Property Name', fontsize=14)
    
    # Add count values to the end of each bar
    for i, v in enumerate(property_avg['count']):
        ax.text(v + 0.5, i, f"{v:.1f}", va='center')
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join("data", "property_landing_frequency.png"))
    plt.close()
    
    print(f"Saved property landing frequency visualization to data/property_landing_frequency.png")

def visualize_property_heatmap(df):
    """Create a heatmap of the Monopoly board with landing frequencies."""
    # Define the Monopoly board layout with 11 properties on each side
    # Standard Monopoly board has 40 spaces (10 on each side with corners)
    board_layout = [
        # Bottom row (left to right)
        ["Go", "Mediteranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax", 
         "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue", "Jail"],
        # Left column (bottom to top)
        ["Boardwalk", "", "", "", "", "", "", "", "", "", "St. Charles Place"],
        ["Luxury Tax", "", "", "", "", "", "", "", "", "", "States Avenue"],
        ["Park Place", "", "", "", "", "", "", "", "", "", "Virginia Avenue"],
        ["Chance", "", "", "", "", "", "", "", "", "", "Pennsylvania Railroad"],
        ["Short Line", "", "", "", "", "", "", "", "", "", "St. James Place"],
        ["Pennsylvania Avenue", "", "", "", "", "", "", "", "", "", "Community Chest"],
        ["Community Chest", "", "", "", "", "", "", "", "", "", "Tennessee Avenue"],
        ["North Carolina Avenue", "", "", "", "", "", "", "", "", "", "New York Avenue"],
        ["Pacific Avenue", "", "", "", "", "", "", "", "", "", "Kentucky Avenue"],
        # Top row (right to left)
        ["Go To Jail", "Marvin Gardens", "Ventnor Avenue", "Atlantic Avenue", "B. & O. Railroad", 
         "Illinois Avenue", "Indiana Avenue", "Chance", "Water Works", "Free Parking", ""]
    ]
    
    # Create a matrix for the heatmap
    heatmap_data = np.zeros((11, 11))
    
    # Group by property_name and calculate the mean count
    property_avg = df.groupby('property_name')['count'].mean().to_dict()
    
    # Fill the heatmap data
    for i in range(11):
        for j in range(11):
            property_name = board_layout[i][j]
            if property_name in property_avg:
                heatmap_data[i, j] = property_avg[property_name]
    
    # Create the heatmap
    plt.figure(figsize=(16, 14))
    ax = sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", 
                     linewidths=.5, cbar_kws={'label': 'Average Landing Frequency'})
    
    # Add property names as annotations
    for i in range(11):
        for j in range(11):
            if board_layout[i][j]:
                # Adjust text position and rotation based on position on board
                if i == 0:  # Bottom row
                    ax.text(j + 0.5, i + 0.7, board_layout[i][j], 
                            ha='center', va='center', fontsize=7, 
                            color='black', rotation=45)
                elif i == 10:  # Top row
                    ax.text(j + 0.5, i + 0.3, board_layout[i][j], 
                            ha='center', va='center', fontsize=7, 
                            color='black', rotation=45)
                elif j == 0:  # Left column
                    ax.text(j + 0.7, i + 0.5, board_layout[i][j], 
                            ha='center', va='center', fontsize=7, 
                            color='black', rotation=0)
                elif j == 10:  # Right column
                    ax.text(j + 0.3, i + 0.5, board_layout[i][j], 
                            ha='center', va='center', fontsize=7, 
                            color='black', rotation=0)
    
    # Add title
    plt.title('Monopoly Board Landing Frequency Heatmap', fontsize=18)
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join("data", "property_heatmap.png"))
    plt.close()
    
    print(f"Saved property heatmap visualization to data/property_heatmap.png")

def visualize_by_game_size(df):
    """Compare landing frequencies across different game sizes."""
    # Create a new column for game size (rounds * players)
    df['game_size'] = df['rounds'] * df['players']
    
    # Group by property_name and game_size
    grouped = df.groupby(['property_name', 'game_size'])['count'].mean().reset_index()
    
    # Get the top 10 most landed on properties
    top_properties = df.groupby('property_name')['count'].mean().nlargest(10).index.tolist()
    filtered_df = grouped[grouped['property_name'].isin(top_properties)]
    
    # Create the plot
    plt.figure(figsize=(14, 8))
    sns.lineplot(x='game_size', y='count', hue='property_name', data=filtered_df, marker='o')
    
    # Add labels and title
    plt.title('Landing Frequency by Game Size for Top 10 Properties', fontsize=18)
    plt.xlabel('Game Size (Rounds × Players)', fontsize=14)
    plt.ylabel('Average Number of Landings', fontsize=14)
    plt.legend(title='Property Name', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join("data", "property_by_game_size.png"))
    plt.close()
    
    print(f"Saved property by game size visualization to data/property_by_game_size.png")

def main():
    """Main function to run all visualizations."""
    # Create the data directory if it doesn't exist
    os.makedirs(os.path.join("data"), exist_ok=True)
    
    # Load the data
    df = load_property_data()
    if df is None:
        return
    
    # Run visualizations
    visualize_landing_frequency(df)
    visualize_property_heatmap(df)
    visualize_by_game_size(df)
    
    print("All property visualizations complete!")

if __name__ == "__main__":
    main()
