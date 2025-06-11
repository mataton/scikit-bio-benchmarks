"""Basic benchmarks that don't import scikit-bio modules."""
import numpy as np

class BasicBenchmarks:
    def time_numpy_basic(self):
        """Test numpy operations (doesn't import scikit-bio)."""
        arr = np.random.random(1000)
        return np.sum(arr)
    
    def time_simple_operation(self):
        """Simple Python operation."""
        return sum(range(1000))
