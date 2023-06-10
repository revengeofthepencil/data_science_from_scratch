import sys
import os
from pathlib import Path
current_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = Path(current_path).parent
# adding ch04 to the system path
sys.path.append(os.path.join(parent_dir, "ch04"))

from linear_algebra import dot

"""
We'll first look at covariance, the paired analogue of variance.
Whereas variance measures how a single variable deviates from its mean,
covariance measures how two variables vary in tandem from their means:
"""
