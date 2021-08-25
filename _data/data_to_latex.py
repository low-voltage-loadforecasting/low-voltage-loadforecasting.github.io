import pandas as pd
import yaml

pd.options.display.max_colwidth = 500

with open("data.yml", "r") as f:
    df = pd.io.json.json_normalize(yaml.load(f, Loader=yaml.FullLoader))
    
df.Bibtexkey = df.Bibtexkey.astype(str).str.replace("\['", "").astype(str).str.replace("']", "").astype(str).str.replace("', '", ", ")
df["Name"] = "\href{\\url{" + df["Url"] + "}}{" + df["Name"] + "}~\cite{" + df["Bibtexkey"] + "}" if (df["Bibtexkey"].str == "None") else "\href{\\url{" + df["Url"] + "}}{" + df["Name"] + "}"

COLUMNS = ['Name', 'Type', 'Customers', 'Resolution', 'Duration', 'Intervention', 'Submetering', 'Weather', 'Location','Other', 'Licence']

df = df.sort_values(["Type", "Location", "Name"])

with open("table.tex", "w") as f2:
    s = df[COLUMNS].to_latex(index=False, escape=False, col_space=1)
    s = s.replace("    ", "").replace("\n ", "\n").replace("\n ", "\n").replace("\n ", "\n").replace("\n ", "\n")
    f2.write(s)