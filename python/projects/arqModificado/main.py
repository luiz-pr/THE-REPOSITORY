from pathlib import Path

data_criacao = lambda f: f.stat().st_ctime
data_modificacao = lambda f: f.stat().st_mtime

directory = Path('./')
files = directory.glob('*.txt')
sorted_files = sorted(files, key=data_modificacao, reverse=True)

for f in sorted_files:
    print(f)