import numpy as np
from typing import Tuple

def neighborhood_disk(pos2d: np.ndarray) -> np.ndarray:

    r = np.abs(np.random.normal(0, 1))
    theta = np.random.uniform(0, 2*np.pi)
    new_pos2d = pos2d + r * np.array([np.cos(theta), np.sin(theta)])

    return new_pos2d

def evaluate_pos2d(pos2d: np.ndarray, f_2d) -> float:

    return f_2d(pos2d[0], pos2d[1])

def linear_temp_decay(alpha: float, min_temperature: float, temperature: float) -> float:
    
    return max(alpha * temperature, min_temperature)

def simulated_annealing(num_iterations: int, neighborhood_fn, energy_fn, clips: np.ndarray,
                        temperature: float, temperature_decay = None) -> Tuple[float, float]:
    """Minimizes energy
    Args:
        neighborhood_fn: Takes a position and returns a new position
        energy_fn: Takes a position and returns its energy
        clips: A Array where [..., 0] is min and [..., 1] is max

    Returns:
        best_pos, best_energy
    """

    pos = (clips[..., 1] - clips[..., 0]) / 2
    energy = energy_fn(pos)

    best_pos = pos
    best_energy = energy

    for i in range(num_iterations):
        new_pos = neighborhood_fn(pos)
        new_pos = np.clip(new_pos, clips[..., 0], clips[..., 1])
        new_energy = energy_fn(new_pos)

        prob = np.exp(- (new_energy - best_energy) / temperature)
        if prob > 1.:
            best_pos = new_pos
            best_energy = new_energy
        if prob > np.random.uniform(0, 1):
            pos = new_pos
            energy = new_energy
        
        if temperature_decay is not None:
            temperature = temperature_decay(temperature=temperature)

    return best_pos, best_energy
