def compare_results(results):
    print("\n--- Explorer Performance on Static Maze ---")
    print(f"{'Explorer':<10} {'Time (s)':<10} {'Moves':<10} {'Backtracks':<12}")
    best = min(results, key=lambda x: x[0])

    for idx, (time_taken, move_count, backtracks) in enumerate(results, 1):
        backtrack_str = str(backtracks) if backtracks is not None else "N/A"
        print(f"{idx:<10} {time_taken:<10.5f} {move_count:<10} {backtrack_str:<12}")
    
    print(" Best Time:", f"{best[0]:.5f} seconds with {best[1]} moves")
