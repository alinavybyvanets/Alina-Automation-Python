from pathlib import Path
import pandas as pd
path = Path(".")
csv_files = list(path.glob("*.csv"))

df1 = pd.read_csv(csv_files[0])
df2 = pd.read_csv(csv_files[1])

combined_df = pd.concat([df1, df2])
unique_df = combined_df.drop_duplicates()

result_file = path / "result_vybyvanets.csv"
unique_df.to_csv(result_file, index=False)
print(f"Готово! Результат збережено в: {result_file}")


