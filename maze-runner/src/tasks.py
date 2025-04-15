# tasks.py
from celery import Celery
from src.enhanced_explorers import Explorer
from src.maze import create_maze

# Setup Celery App
celery_app = Celery(
    'maze_tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery_app.task
def explorer_task_celery(maze_type, width, height, visualize):
    maze = create_maze(width, height, maze_type)
    explorer = Explorer(maze, visualize=visualize)
    
    time_taken, moves = explorer.solve()
    backtracks = getattr(explorer, 'backtracks', None)

    return (time_taken, len(moves), backtracks)
