import pandas as pd
import numpy as np

def load_dashboard_data():
    return pd.DataFrame({
        "Sales": np.random.randint(100, 500, 10),
        "Customers": np.random.randint(20, 100, 10)
    })
