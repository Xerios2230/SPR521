import os, re, collections

# 1
with open("data.txt", "w", encoding="utf-8") as f:
    for _ in range(3): f.write(input("Введіть рядок: ") + "\n")

# 2
if os.path.exists("data.txt"):
    with open("data.txt", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if i % 2 == 0: print(line.strip())
else:
    print("Файл data.txt не існує")

# 3
with open("data.txt", encoding="utf-8") as f, open("filtered.txt", "w", encoding="utf-8") as out:
    for line in f:
        if "Python" in line: out.write(line)

# 4
fname = input("Ім'я файлу: ")
with open(fname, encoding="utf-8") as f, open("cleaned.txt", "w", encoding="utf-8") as out:
    out.write(re.sub(r"\d", "", f.read()))

# 5
with open("log.txt", encoding="utf-8") as f:
    words = re.findall(r"\w+", f.read().lower())
cnt = collections.Counter(words).most_common(10)
with open("word_stats.txt", "w", encoding="utf-8") as out:
    for w, c in cnt: out.write(f"{w}: {c}\n")

# 6
with open("data.txt", encoding="utf-8") as f, open("reversed.txt", "w", encoding="utf-8") as out:
    out.writelines(reversed(f.readlines()))
