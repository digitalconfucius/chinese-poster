# chinese-poster
A very large Chinese character 汉子 e-poster. Contains the top 99.99 percentile (6500) of most frequent characters from [Jun Da's frequency list](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO).

This website isn't perfect. It is an approximate way for looking at all the Chinese characters you need at once. You can click on each card to see more info on specific definitions.

# Usage

```
git clone https://github.com/digitalconfucius/chinese-poster.git

cd chinese-poster

python tools/convert.py data/mydata.csv
```

Afterward, find the output in data/output.html, then manually copy and paste it into the appropriate section in index.html.
