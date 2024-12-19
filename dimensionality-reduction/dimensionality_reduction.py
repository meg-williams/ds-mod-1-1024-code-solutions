# %%
import pandas as pd
from sklearn.decomposition import PCA

# %% [markdown]
# #### dataframe 

# %%
df = pd.read_csv('/Users/meganwilliams/Documents/GitHub/ds-mod-1-1024-code-solutions/dimensionality-reduction/mnist.csv')
df

# %% [markdown]
# #### pca

# %%
pca = PCA(90)
pca.fit(df)
df_pca = pca.transform(df)

# %%
pca.explained_variance_ratio_.sum()

# %%
pca.n_components_ 


