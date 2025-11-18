import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

CSV_FILE = "website_wata.csv"         
OUTPUT_PLOT = "tsne_scatter.png"
OUTPUT_EMBED = "tsne_embeddings.csv"

RANDOM_STATE = 42
TSNE_PERPLEXITY = 30
TSNE_LEARNING_RATE = 200
TSNE_N_ITER = 1000
PCA_COMPONENTS = 10     # set to None to skip PCA pre-reduction

# -----------------------
# Load
# -----------------------
df = pd.read_csv(CSV_FILE)
print(f"Loaded {len(df)} rows, columns: {list(df.columns)}")

# -----------------------
# Basic cleaning & columns
# -----------------------
# Ensure expected columns exist (defensive)
expected = ['Page Views', 'Session Duration', 'Bounce Rate',
            'Traffic Source', 'Time on Page', 'Previous Visits', 'Conversion Rate']
present = [c for c in expected if c in df.columns]
if len(present) < 5:
    raise ValueError(f"Too few expected columns present. Found: {present}")

# Remove % signs if present and convert numeric columns
num_cols = ['Page Views', 'Session Duration', 'Bounce Rate',
            'Time on Page', 'Previous Visits', 'Conversion Rate']
for c in num_cols:
    if c in df.columns:
        df[c] = df[c].astype(str).str.replace('%', '').str.strip()
        df[c] = pd.to_numeric(df[c], errors='coerce')

# Keep only rows that have at least some numeric data
df = df.dropna(subset=[c for c in num_cols if c in df.columns], how='any').reset_index(drop=True)

# -----------------------
# Preprocessing: encode + scale
# -----------------------
numeric_features = [c for c in num_cols if c in df.columns]
categorical_features = ['Traffic Source'] if 'Traffic Source' in df.columns else []

transformers = []
if numeric_features:
    transformers.append(("num", StandardScaler(), numeric_features))
if categorical_features:
    transformers.append(("cat", OneHotEncoder(sparse_output=False, handle_unknown='ignore'), categorical_features))

ct = ColumnTransformer(transformers=transformers, remainder='drop')
X = ct.fit_transform(df)

print(f"Transformed feature matrix shape: {X.shape}")

# -----------------------
# Optional PCA pre-reduction (helps t-SNE speed/stability)
# -----------------------
if PCA_COMPONENTS and X.shape[1] > PCA_COMPONENTS:
    pca = PCA(n_components=PCA_COMPONENTS, random_state=RANDOM_STATE)
    X_used = pca.fit_transform(X)
    print(f"PCA reduced to {PCA_COMPONENTS} components (explained ~{pca.explained_variance_ratio_.sum():.2f})")
else:
    X_used = X

# -----------------------
# Run t-SNE
# -----------------------
tsne = TSNE(n_components=2,
            perplexity=TSNE_PERPLEXITY,
            learning_rate=TSNE_LEARNING_RATE,
            max_iter=TSNE_N_ITER,
            init='pca',
            random_state=RANDOM_STATE)
emb = tsne.fit_transform(X_used)
df['TSNE-1'] = emb[:, 0]
df['TSNE-2'] = emb[:, 1]

# -----------------------
# Save embeddings CSV
# -----------------------
cols_to_save = ['TSNE-1', 'TSNE-2'] + [c for c in df.columns if c in expected]
df[cols_to_save].to_csv(OUTPUT_EMBED, index=False)
print(f"Saved embeddings to: {OUTPUT_EMBED}")

# -----------------------
# Plot: color by Traffic Source if available, else plain
# -----------------------
plt.figure(figsize=(9,6))
if 'Traffic Source' in df.columns:
    cat_vals = df['Traffic Source'].astype(str)
    unique = cat_vals.unique()
    for u in unique:
        sel = df[cat_vals == u]
        plt.scatter(sel['TSNE-1'], sel['TSNE-2'], label=str(u), s=40, alpha=0.8)
    plt.legend(title='Traffic Source', bbox_to_anchor=(1.05,1), loc='upper left')
else:
    plt.scatter(df['TSNE-1'], df['TSNE-2'], s=40, alpha=0.8)

plt.xlabel('TSNE-1')
plt.ylabel('TSNE-2')
plt.title('t-SNE projection — Website Sessions')
plt.tight_layout()
plt.savefig(OUTPUT_PLOT, dpi=300)
plt.close()
print(f"Saved plot to: {OUTPUT_PLOT}")

print("t-SNE pipeline finished.")
