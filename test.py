from pychorus import create_chroma
from pychorus.similarity_matrix import TimeTimeSimilarityMatrix, TimeLagSimilarityMatrix

chroma, _, sr, _ = create_chroma("daft.wav")
time_time_similarity = TimeTimeSimilarityMatrix(chroma, sr)
time_lag_similarity = TimeLagSimilarityMatrix(chroma, sr)

## Visualize the results
#time_time_similarity.display()
#time_lag_similarity.display()
