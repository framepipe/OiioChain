# OiioChain

OiioChain is a simple python wrapper for OpenImageIO, which makes chaining of ImageBufAlgo functions simple. To use it, simply initialise the class with a file you want and call the algo functions together.

```python
from oiio_chain import OiioChain

chain = OiioChain("Dino_001_01_X1_0066.cr2")

chain.crop(1208, 4901, 814, 2385)\
    .extend(3693, 2077).resize(1920, 1080)\
    .text(1300, 1030, "00066.cr2").text(1600, 1030, "00:00:02:18")\
    .write("final.jpg")
```

Currently supports a subset of all methods (crop, resize, cut, paste, rotate90, rotate180, rotate270, flip, flop, flipflop, text, extend and write).