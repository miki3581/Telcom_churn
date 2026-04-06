import kagglehub
import pandas as pd

# Load dataset
def load_data() -> pd.DataFrame:
    
    kagglehub.login()

    path_file =kagglehub.dataset_download("blastchar/telco-customer-churn")
    df = pd.read_csv(path_file)

    return df
