# Python snippet

This is a repository for storing some small but useful tool written using python.

# What's include currently

- [x] URL_CONVERT, support thunder/qq/flashget url
- [x] Weather, look up weather info conveniently
- [x] CapcitySum, sum the capcity of KBs, MBs, GBs, TBs or PBs
- [ ] Some other comming soon

# How to use in general

```bash
git clone https://github.com/opensource-yunnan-university/python_snippet.git
cd python_snippet
python whatever_in_this_repository.py
```

# How to use in details

### URL_CONVERT, see snapshot below

![url_convert_example][url_convert_example]

### Weather, see snapshot below

![weather_example][weather_example]


### CapcitySum, see the following

```bash
➜  python_snippet git:(master) ✗ cat data.txt 
55.22G
1.30K
361.91G
85.77G
27.33G
12.4M
0.3T
1.2P
➜  python_snippet git:(master) ✗ cat data.txt|./capcity_sum.py 
Processing  55.22G
Processing  1.30K
Processing  361.91G
Processing  85.77G
Processing  27.33G
Processing  12.4M
Processing  0.3T
Processing  1.2P
Total bytes is 1.35197908483e+15 bytes, or 1289347729.52 KB, or 1289347729.52 MB, or 1259128.64211 GB, or 1229.61781456 TB, or 1.20079864703 PB
➜  python_snippet git:(master) ✗ ./capcity_sum.py data.txt 
Processing  55.22G
Processing  1.30K
Processing  361.91G
Processing  85.77G
Processing  27.33G
Processing  12.4M
Processing  0.3T
Processing  1.2P
Total bytes is 1.35197908483e+15 bytes, or 1289347729.52 KB, or 1289347729.52 MB, or 1259128.64211 GB, or 1229.61781456 TB, or 1.20079864703 PB
➜  python_snippet git:(master) ✗ ./capcity_sum.py 
55.22G
1.30K
361.91G
85.77G
27.33G
12.4M
0.3T
1.2PProcessing  55.22G
Processing  1.30K
Processing  361.91G
Processing  85.77G
Processing  27.33G
Processing  12.4M
Processing  0.3T
Processing  1.2P
Total bytes is 1.35197908483e+15 bytes, or 1289347729.52 KB, or 1289347729.52 MB, or 1259128.64211 GB, or 1229.61781456 TB, or 1.20079864703 PB
➜  python_snippet git:(master) ✗ 
```

# How to contribute

1. fork repository
2. add your code
3. update readme
4. send pr

# License

[Apache License 2.0][Apache License 2.0]

[Apache License 2.0]: http://www.apache.org/licenses/
[url_convert_example]: images/url_convert_example.png
[weather_example]: images/weather_example.png