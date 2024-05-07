# chinese-poster
A very large Chinese character 汉子 e-poster. Contains the top 99.99 percentile (6500) of most frequent characters from [Jun Da's frequency list](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO).

This website is inspired by stories of classic language learners who would print posters of [Jouyou Kanji List](https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji) for daily Japanese practice. It isn't perfect. It is an approximate way for looking at all the Chinese characters you need at once. You can click on each card to see more info on specific definitions.

![image](https://github.com/digitalconfucius/chinese-poster/assets/156959605/99395404-36a8-4ff2-9802-8182788dbefd)

[Check out the website here](https://digitalconfucius.github.io/chinese-poster/)!

# Usage

```
git clone https://github.com/digitalconfucius/chinese-poster.git

cd chinese-poster

python tools/convert.py data/mydata.csv
```

Afterward, find the output in data/output.html, then manually copy and paste it into the appropriate section in index.html.
