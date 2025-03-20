#!/usr/bin/env python3
"""
Main script to visualize Monopoly game statistics.
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = ['pandas', 'matplotlib', 'seaborn', 'numpy']
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Missing required package: {package}")
            install = input(f"Would you like to install {package}? (y/n): ")
            if install.lower() == 'y':
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            else:
                print(f"Cannot continue without {package}. Exiting.")
                return False
    
    return True

def main():
    """Run all visualization scripts."""
    # Check if we have the required dependencies
    if not check_dependencies():
        return
    
    # Make sure we're in the stats directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    print("=== Monopoly Statistics Visualization ===")
    
    # Run property visualizations
    print("\nGenerating property visualizations...")
    try:
        from visualize_properties import main as run_property_viz
        run_property_viz()
    except Exception as e:
        print(f"Error running property visualizations: {e}")
    
    # Run dice visualizations
    print("\nGenerating dice visualizations...")
    try:
        from visualize_dice import main as run_dice_viz
        run_dice_viz()
    except Exception as e:
        print(f"Error running dice visualizations: {e}")
    
    print("\nVisualization complete! Check the 'data' directory for the generated images.")

if __name__ == "__main__":
    main()
