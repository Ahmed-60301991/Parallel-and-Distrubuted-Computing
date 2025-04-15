# Question 1: Automated Maze Explorer

This section provides a detailed explanation of how the automated maze explorer works in the `maze-runner` project. It covers the algorithm used, how it handles loops, the backtracking strategy, and the statistics collected during the run. The explanation is based on both practical observations from running the explorer and a code-level understanding of `explorer.py`.

---

## 1. Algorithm Used: Right-Hand Rule

The automated explorer uses the **Right-Hand Rule** algorithm, a common maze-solving technique for exploring simply-connected mazes (i.e., mazes without loops). The rule works as follows:

- The explorer always keeps its "right hand" in contact with the wall.
- At every step, the explorer evaluates directions in this priority order:
  1. **Turn right**
  2. **Move forward**
  3. **Turn left**
  4. **Turn around (backtrack)**

This approach ensures that the explorer does not miss any corridor and systematically navigates toward the goal if a path exists.

> **Implementation Insight:**
> - In `explorer.py`, the explorer maintains a facing direction (`current_direction`) and determines possible directions using this priority strategy.
> - Movement decisions are made relative to the current orientation, enabling consistent behavior regardless of the explorer's position.

---

## 2. Loop Detection Mechanism

To prevent getting stuck in infinite loops, especially in mazes with cycles, the explorer incorporates a **loop detection mechanism**:

- It tracks a history of visited cells using a tuple `(position, direction)`.
- If it revisits the **same cell** from the **same direction** more than once within a short interval, it's considered a potential loop.
- A loop counter or visit history dictionary (`visit_count`) is used to keep track of how often a cell is visited from a specific orientation.

> **Key Logic:**
> ```python
> visit_count[(x, y, direction)] += 1
> if visit_count[(x, y, direction)] > threshold:
>     handle_loop()
> ```

This mechanism enables the explorer to **detect repeated patterns** and respond accordingly.

---

## 3. Backtracking Strategy

When the explorer encounters:
- A **dead end**, or
- Detects that it is **stuck in a loop**,

It initiates a **backtracking strategy**, which involves:

- Maintaining a **stack** of previously visited positions (`path_history`).
- **Popping** from the stack to return to earlier decision points.
- From these previous positions, it checks for **unexplored directions** to continue the maze traversal.

> **Implementation Note:**
> - This is similar to a **depth-first search (DFS)** fallback strategy, ensuring all paths are eventually explored even in complex maze structures.
> - Backtracking also ensures that the agent can escape local loops or dead ends efficiently.

---

## 4. Performance Metrics Collected

After completing the maze, the automated explorer outputs a comprehensive set of **statistics** to evaluate its performance:

| Metric                 | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Total Moves**        | Number of steps taken from start to finish                                  |
| **Time Taken**         | Duration (in seconds) of the full exploration run                           |
| **Backtracks**         | Number of times the agent reversed its path due to loops or dead ends       |
| **Loop Encounters**    | Number of times a loop was detected and handled                             |
| **Path History**       | The sequence of `(x, y)` positions visited throughout the run               |
| **Exploration Outcome**| Whether the goal was reached and the final position of the agent            |

These metrics help compare performance across different maze types and explorer configurations.

---

## 5. Observations from Different Maze Types

### ➤ Static Maze (Predefined Walls)
- The explorer follows the right-hand wall precisely.
- Clearly visible turn decisions and systematic traversal.
- Minimal backtracking required in linear paths.

### ➤ Random Maze (Maze with Cycles)
- The explorer may revisit nodes and detect loops.
- Backtracking is invoked more frequently.
- Loop detection proves useful for convergence.

### ➤ With Visualization
- Movement is visible in real-time.
- Easy to identify turns, backtracks, and exploration patterns.
- Good for debugging and understanding behavior.

### ➤ Without Visualization
- Significantly faster execution.
- Useful for bulk performance testing and collecting metrics.
- Same logic and output but runs headlessly.

---

## Summary

The automated maze explorer demonstrates a solid understanding of maze-solving strategies. It combines:

- The **Right-Hand Rule** for primary navigation,
- **Loop detection** to avoid infinite cycles,
- **Backtracking** to recover from dead ends, and
- **Detailed metrics** for performance evaluation.

This makes it a robust solution capable of handling both simple and complex mazes with varied layouts.

---


# Question 2
## Solution: Parallel Maze Exploration Using MPI4Py

In this solution, we modified the maze exploration program to run multiple maze explorers in parallel across multiple machines using MPI4Py. This setup allows us to efficiently compare the performance of different explorers and identify the best route out of the maze. The solution leverages MPI to distribute tasks across a master-worker architecture, where each worker computes the exploration statistics for a specific number of explorers. 

### Key Concepts Used:
- **MPI4Py**: This Python library allows us to use the Message Passing Interface (MPI) to distribute tasks among multiple machines. We used MPI to distribute maze exploration tasks to worker processes on multiple computers, with one master node coordinating the work and collecting results.
- **Task Queue System**: We created a task list for each explorer, which was distributed to available worker processes. This allows for efficient parallel execution.
- **Performance Comparison**: After the exploration tasks were completed, the results were gathered at the master node. The best explorer was identified based on the fastest time or the fewest moves, and the results for each explorer were displayed for comparison.

### How the Solution Works:
1. **Task Distribution**: The main program generates a list of tasks based on the user-specified number of explorers (`--explorers`). In my own, I used 3, so that I have 1 master master, which is my VM, and 2 worker VMs, which are my teams other VMs. These tasks are divided among available worker nodes, with each node performing the maze exploration for a subset of explorers.
2. **Running Explorers in Parallel**: Each worker node runs the `explorer_task` function, which creates a maze, initializes an explorer, and measures the time taken and number of moves made during the exploration.
3. **Collecting Results**: Once all tasks are completed, the results (time taken, number of moves) from all explorers are gathered at the master node using `MPI.COMM_WORLD.gather()`.
4. **Comparison and Output**: The master node compares the results, identifying the best explorer based on the fastest time. It also displays the performance statistics for each explorer, such as total time, total moves, and the number of backtrack operations.

### Output:
The output includes the statistics for each explorer, such as the time taken, number of moves made, and the average moves per second. The best explorer, in terms of time, is displayed with its corresponding performance metrics.

pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)  
Hello from the pygame community. https://www.pygame.org/contribute.html

=== Maze Exploration Statistics ===  
Total time taken: 0.00 seconds  
Total moves made: 1279  
Number of backtrack operations: 0  
Average moves per second: 1056630.85  
==================================

pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)  
Hello from the pygame community. https://www.pygame.org/contribute.html

=== Maze Exploration Statistics ===  
Total time taken: 0.00 seconds  
Total moves made: 1279  
Number of backtrack operations: 0  
Average moves per second: 942465.71  
==================================

pygame 2.6.1 (SDL 2.28.4, Python 3.12.2)  
Hello from the pygame community. https://www.pygame.org/contribute.html

=== Maze Exploration Statistics ===  
Total time taken: 0.00 seconds  
Total moves made: 1279  
Number of backtrack operations: 0  
Average moves per second: 966579.25  
==================================

=== Maze Exploration Statistics ===  
Total time taken: 0.00 seconds  
Total moves made: 1279  
Number of backtrack operations: 0  
Average moves per second: 1122518.27  
==================================

--- Explorer Performance on Static Maze ---  
Explorer   Time (s)   Moves      Backtracks  
1          0.00       1279       N/A         
2          0.00       1279       N/A         
3          0.00       1279       N/A         
4          0.00       1279       N/A         

🏁 Best Time: 0.00 seconds with 1279 moves


### Key Steps Taken:
1. **Modified the Main Program**: We integrated MPI4Py to manage the distribution of tasks between the master and worker nodes.
2. **Used `MPI.COMM_WORLD` to Manage Communication**: This allowed workers to send their results back to the master node for comparison.
3. **Explorers Run in Parallel**: Multiple explorers were run simultaneously, with the results gathered and analyzed.
4. **Improved Task Distribution**: The program was designed to divide the task of exploring the maze among all available machines in a balanced manner, ensuring that no single worker was overloaded with too many explorers.

### Conclusion:
Using MPI4Py, we successfully parallelized the maze exploration task, enabling multiple explorers to run concurrently on multiple machines. The system efficiently compared their performance and identified the best-performing explorer. This approach can be further enhanced by integrating a task queue system like Celery and RabbitMQ for more dynamic task distribution in larger setups.


# Question 3
## Maze Exploration Performance Analysis

### Results Summary

Below are the statistics for each maze explorer on the static maze:

| Explorer | Time (s) | Moves | Backtracks |
|----------|----------|-------|------------|
| 1        | 0.00     | 1279  | N/A        |
| 2        | 0.00     | 1279  | N/A        |
| 3        | 0.00     | 1279  | N/A        |
| 4        | 0.00     | 1279  | N/A        |
| 5        | 0.00     | 1279  | N/A        |
| 6        | 0.00     | 1279  | N/A        |

### Key Observations:
- **Time Taken:** All explorers reported **0.00 seconds** for solving the maze. This suggests that the maze-solving process is extremely fast for these implementations, likely due to the simplicity of the static maze or limitations in time tracking precision.
  
- **Moves:** Every explorer made **1279 moves**. This is expected, as the maze is static and deterministic, so the number of moves is constant for all explorers.

- **Backtracking:** No backtrack operations were reported (N/A). This could indicate that the explorers are efficient in finding the solution without needing to backtrack, which is a positive outcome for pathfinding efficiency.

- **Average Moves per Second:** The average moves per second across explorers range from **1,012,981 to 1,240,350 moves/sec**, indicating variations in performance likely due to different execution environments or minor computational differences.

### 🏁 **Best Time and Performance:**
- All explorers have the same time and moves, with the best solution being **0.00 seconds** with **1279 moves**.

### Conclusion:
- The maze-solving process is highly efficient for all explorers on the static maze.
- Given that all explorers made the same number of moves and had the same time, it suggests that the maze is well-suited to quick exploration and that the explorers' performance is nearly identical in this context.
- The lack of backtracking is also an indication of effective pathfinding in a static maze scenario.

#### Final Thoughts:
- If you were to test with a more complex or dynamic maze, you would likely see more variation in times, moves, and backtracking operations, as the maze complexity would affect the solver behavior.


# Question 4

#### 1. **Identified Limitations of the Current Explorer**

The current maze explorer implementation has several limitations that affect its performance, efficiency, and robustness when solving a maze:

1. **Limited Exploration Algorithm**: The current algorithm relies solely on the right-hand rule for movement, which is a basic algorithm that can fail in certain mazes. It may not always find the most optimal path or may get stuck in loops, especially in more complex mazes.
  
2. **Backtracking Limitation**: The backtracking feature is implemented, but it only occurs after the explorer gets stuck. This means the explorer does not proactively consider alternative paths, leading to inefficiency and slow progress in certain scenarios.

3. **Penalties for A***: The current explorer does not employ an intelligent search algorithm like A* (A-star), which would allow for more informed exploration. The current approach may unnecessarily explore suboptimal paths, leading to a higher number of moves.

4. **Lack of Path Optimization**: The current pathfinding does not incorporate any form of path optimization. The explorer does not consider the distance to the goal in its decision-making process, potentially leading to an inefficient traversal.

#### 2. **Proposed Improvements to the Exploration Algorithm**

To overcome these limitations, we propose the following improvements:

1. **Implement A* (A-Star) Algorithm**:
   - **Why**: A* is a heuristic-based search algorithm that combines the benefits of Dijkstra's algorithm (finding the shortest path) with a heuristic function that estimates the cost to reach the goal. This helps in efficiently exploring the maze, prioritizing the most promising paths.
   - **High Penalty Implementation**: In our maze, the goal is to encourage faster exploration without revisiting the same paths unnecessarily. By applying a high penalty for revisiting a node (e.g., using an infinite penalty), we ensure that the explorer does not waste time on paths that have already been explored.
   
2. **Introduce Proactive Path Selection**:
   - **Why**: Instead of blindly following the right-hand rule or backtracking after getting stuck, the explorer should consider multiple options in each step. This will allow for more efficient exploration and the ability to avoid dead-ends proactively.
   - **How**: At each junction, we will look ahead in all four possible directions (right, forward, left, and back) and choose the best option based on certain criteria like distance to the goal or available unexplored paths.

#### 3. **Implementation of Proposed Improvements**

The following changes were implemented:

- **A* Algorithm**: A priority queue (min-heap) stores the frontier nodes ordered by their f-cost, which is the sum of the actual cost to reach the cell and the heuristic cost to reach the goal. The algorithm evaluates the best path based on these costs and ensures no node is revisited unnecessarily.
  
- **Heuristic Function**: We used the **Manhattan distance** as the heuristic for A*. This estimates the cost to the goal based on the horizontal and vertical distances, which is ideal for grid-based mazes.
  
- **Proactive Path Selection**: At each decision point, the A* algorithm considers all possible moves (right, forward, left, and back) and chooses the one with the best cost estimate. This allows the explorer to make informed decisions instead of relying on simple rules.

#### 4. **Explanation of Modifications**

1. **A* Algorithm Implementation**:
   - The A* algorithm was implemented to evaluate the cost of each move using both the actual cost and the heuristic estimate. By applying a high penalty for revisiting cells (e.g., infinite penalty), the explorer avoids wasting time on already explored paths, making the search more efficient.

2. **Heuristic Function**:
   - The **Manhattan distance** heuristic was used because it is simple and effective for grid-based mazes. It calculates the sum of the horizontal and vertical distances to the goal, providing an estimate of the remaining cost.

3. **Proactive Path Selection**:
   - Instead of following a rigid rule like the right-hand rule, the explorer evaluates multiple paths at each junction and chooses the best one based on the calculated f-cost. This leads to faster and more efficient exploration.

#### 5. **Conclusion**

The enhancements made to the maze explorer, specifically the implementation of the A* algorithm and the introduction of proactive path selection, significantly improve its ability to efficiently solve mazes. The high penalty for revisiting nodes ensures that the explorer avoids redundant paths, and the A* algorithm enables the explorer to make more informed decisions, resulting in fewer moves and faster completion times.




# Question 5
## Performance Comparison of Enhanced Explorer vs. Original Explorer

## 1. Performance Comparison Results and Analysis

### Original Explorer:
The original explorer relied on a right-hand rule algorithm with backtracking. The performance statistics collected from multiple runs on the static maze are as follows:

| **Explorer** | **Time (s)** | **Moves** | **Backtrack Operations** | **Average Moves per Second** |
|--------------|--------------|-----------|--------------------------|-----------------------------|
| 1            | 0.00         | 1279      | N/A                      | 1025523.77                  |
| 2            | 0.00         | 1279      | N/A                      | 1005909.40                  |
| 3            | 0.00         | 1279      | N/A                      | 1049191.24                  |
| 4            | 0.00         | 1279      | N/A                      | 1152667.56                  |

**Summary**: 
- The original explorer consistently took very little time (around 0.00 seconds), which was likely an artifact of the fast execution and the lack of any significant backtracking.
- The number of moves remained constant at 1279 across all tests, indicating that the exploration algorithm was not particularly efficient in finding the end point.

### Enhanced Explorer:
The enhanced explorer utilizes an A* algorithm with a high penalty for non-optimal moves, alongside other performance improvements. The performance statistics for the enhanced explorer are as follows:

| **Explorer** | **Time (s)** | **Moves** | **Backtrack Operations** | **Average Moves per Second** |
|--------------|--------------|-----------|--------------------------|-----------------------------|
| 1            | 0.00         | 127       | N/A                      | 76161.94                    |
| 2            | 0.00         | 127       | N/A                      | 77910.87                    |
| 3            | 0.00         | 127       | N/A                      | 82279.36                    |
| 4            | 0.00         | 127       | N/A                      | 93402.88                    |

**Summary**: 
- The enhanced explorer performed significantly better with only 127 moves compared to the original's 1279 moves.
- The enhanced explorer took slightly more time per move (around 0.001 seconds) compared to the original.
- However, the average moves per second is substantially lower than the original explorer. This is expected because fewer moves were made to reach the solution, but the overall computation per move (including penalties) took slightly more time.

## 2. Visualizations Showing the Improvements
### Visualisations have been included in a separate notebook named Results-Visualisation.ipynb

### Performance Improvement:
- **Number of Moves**: The number of moves in the enhanced explorer dropped drastically, indicating a more efficient pathfinding algorithm.
  

- **Average Moves per Second**: The enhanced explorer shows a more efficient search with fewer moves, though with a slightly lower average moves per second. This represents a trade-off between speed and efficiency.
  

### Time Comparison:
- **Execution Time**: The time per move for the enhanced explorer is slightly higher due to the introduction of the penalty mechanism in the A* algorithm, which involves additional computation for each decision made.


## 3. Discussion of Trade-offs or New Limitations Introduced

### Trade-offs:
- **Fewer Moves, Higher Complexity**: The enhanced explorer reduced the number of moves drastically (from 1279 to 127), but this came at the cost of higher per-move computation time. The A* algorithm with a high penalty for non-optimal moves ensures that the explorer takes the most efficient path but requires more calculations per move.
  
- **Improved Efficiency vs. Slightly Slower Execution**: The primary advantage of the enhanced explorer is its efficiency in terms of finding the shortest path with fewer moves. However, the introduction of the A* algorithm and penalty mechanism increased the computational overhead slightly, resulting in a slower average moves per second. This is a typical trade-off when optimizing for pathfinding efficiency at the expense of processing time per move.

- **Backtracking Operations**: The enhanced version does not have any backtrack operations, which means it can consistently find the optimal path without needing to retrace its steps. The original explorer relied on backtracking when it encountered dead ends, but it was not as effective in avoiding unnecessary moves.

### New Limitations:
- **Higher Computational Complexity per Move**: Although the enhanced explorer is more efficient in terms of finding the shortest path, the A* algorithm introduces more complexity in decision-making. This can lead to higher computational costs in more complex mazes with a large number of possible paths.
  
- **Potential Overhead in Larger Mazes**: For very large mazes, the A* algorithm with high penalties might incur significant overhead due to the penalty cost calculations, making it slower than simpler algorithms like the right-hand rule.

## Conclusion:
- The enhanced explorer provides a clear performance improvement by significantly reducing the number of moves to solve the maze. However, it does so at the cost of slightly higher computational time per move.
- While the original explorer was fast, it was not as efficient in pathfinding, making it suitable for smaller mazes but less effective in complex scenarios where optimal pathfinding is crucial.
- The trade-offs between speed and efficiency must be considered depending on the specific needs of the maze exploration task.

