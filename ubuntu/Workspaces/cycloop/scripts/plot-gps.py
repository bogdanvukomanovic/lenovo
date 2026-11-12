#!/usr/bin/env python3
"""
Script to plot 2D points from a CSV file.
Each row should contain x,y coordinates as floats.
"""

import csv
import sys
import matplotlib.pyplot as plt

def plot_csv(filename):
    """Read CSV file and plot points."""
    x_coords = []
    y_coords = []
    
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row_num, row in enumerate(reader, start=1):
                if len(row) < 2:
                    print(f"Warning: Row {row_num} has less than 2 columns, skipping")
                    continue
                try:
                    x = float(row[0])
                    y = float(row[1])
                    x_coords.append(x)
                    y_coords.append(y)
                except ValueError as e:
                    print(f"Warning: Row {row_num} contains non-numeric data: {row}, skipping")
                    continue
        
        if not x_coords:
            print("Error: No valid points found in CSV file")
            return
        
        plt.figure(figsize=(10, 8))
        plt.plot(x_coords, y_coords, 'b-', linewidth=2, label='Path')
        plt.plot(x_coords, y_coords, 'ro', markersize=4, label='Points')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'GPS Coordinates from {filename}')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
        
        print(f"Plotted {len(x_coords)} points from {filename}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python plot_csv.py <csv_file>")
        print("Example: python plot_csv.py data/gps-data.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    plot_csv(csv_file)

