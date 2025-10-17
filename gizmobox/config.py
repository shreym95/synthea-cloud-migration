# Setting up config parameters for all notebooks

# Data Lake Storage
DATA_LAKE = 'dbassstorage'
CONTAINER = 'gizmobox'
DATA_LAKE_PATH = f'abfss://{CONTAINER}@{DATA_LAKE}.dfs.core.windows.net'

# Unity Catalog
CATALOG = 'gizmobox'
LANDING = 'landing'
BRONZE = 'bronze'
SILVER = 'silver'
GOLD = 'gold'
VOLUME_PATH = f'/Volumes/{CATALOG}'