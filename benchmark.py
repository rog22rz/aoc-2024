import subprocess
import sys
import time
from tqdm import tqdm

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python benchmark.py script.py input.txt")

    # Define the script and arguments
    script_name = sys.argv[1]
    input_file = sys.argv[2]

    # Number of iterations
    num_iterations = 500

    # Store total execution time
    total_time = 0

    with tqdm(total=num_iterations, desc="Progress", unit="run") as pbar:
        for i in range(num_iterations):
            start_time = time.time()
            
            # Run the script using subprocess
            result = subprocess.run(
                ["python3", script_name, input_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Measure end time
            end_time = time.time()
            run_time = end_time - start_time
            total_time += run_time

            # Update the progress bar
            pbar.update(1)

    # Calculate average runtime
    average_time = total_time / num_iterations
    print(f"\nAverage runtime over {num_iterations} runs: {average_time:.4f} seconds")
