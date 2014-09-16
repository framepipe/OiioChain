import OpenImageIO as oiio

class OiioChain():
    '''A wrapper class for OpenImageIO to simplify chaining of methods'''

    def __init__(self, srcfile):

        self.imgbuf = oiio.ImageBuf(srcfile)

    def crop(self, x1, x2, y1, y2):

        width = x2 - x1
        height = y2 - y1

        cropped = oiio.ImageBuf(oiio.ImageSpec (width, height, 3, oiio.FLOAT))
        success = oiio.ImageBufAlgo.crop(cropped, self.imgbuf, oiio.ROI(x1, x2, y1, y2))

        if success:
            self.imgbuf = cropped

        return self

    def resize(self, width, height):

        resized = oiio.ImageBuf(oiio.ImageSpec (width, height, 3, oiio.FLOAT))
        success = oiio.ImageBufAlgo.resize(resized, self.imgbuf)

        if success:
            self.imgbuf = resized

        return self

    def cut(self, x1, x2, y1, y2):

        width = x2 - x1
        height = y2 - y1

        chopped = oiio.ImageBuf(oiio.ImageSpec (width, height, 3, oiio.FLOAT))
        success = oiio.ImageBufAlgo.cut(chopped, self.imgbuf, oiio.ROI(x1, x2, y1, y2))

        if success:
            self.imgbuf = chopped

        return self

    def paste(self, x, y, z, srcfile):

        srcbuf = oiio.ImageBuf(srcfile)

        spec = self.imgbuf.spec()

        if(spec.width >= srcbuf.spec().width or spec.height >= srcbuf.spec().height):
            oiio.ImageBufAlgo.paste(self.imgbuf, x, y, z, 0, srcbuf)

        return self

    def rotate90(self):
        rotated = oiio.ImageBuf()

        success = oiio.ImageBufAlgo.rotate90(rotated, self.imgbuf)

        if success:
            self.imgbuf = rotated

        return self

    def rotate180(self):
        rotated = oiio.ImageBuf()

        success = oiio.ImageBufAlgo.rotate180(rotated, self.imgbuf)

        if success:
            self.imgbuf = rotated

        return self

    def rotate270(self):
        rotated = oiio.ImageBuf()

        success = oiio.ImageBufAlgo.rotate270(rotated, self.imgbuf)

        if success:
            self.imgbuf = rotated

        return self

    def flip(self):
        flipped = oiio.ImageBuf()

        success = oiio.ImageBufAlgo.flip(flipped, self.imgbuf)

        if success:
            self.imgbuf = flipped

        return self

    def flop(self):
        flopped = oiio.ImageBuf()

        success = oiio.ImageBufAlgo.flop(flopped, self.imgbuf)

        if success:
            self.imgbuf = flopped

        return self

    def flipflop(self):
        flipflopped = oiio.ImageBuf()

        success = oiio.ImageBufAlgo.flipflop(flipflopped, self.imgbuf)

        if success:
            self.imgbuf = flipflopped

        return self

    def text(self, x, y, text):
        oiio.ImageBufAlgo.render_text(self.imgbuf, x, y, text, 50, "Arial")

        return self

    def extend(self, width, height):
        spec = self.imgbuf.spec()

        if width >= spec.width or height >= spec.height:
            extended = oiio.ImageBuf(oiio.ImageSpec (width, height, 3, oiio.FLOAT))
            oiio.ImageBufAlgo.zero(extended)

            pasteX = (width - spec.width) / 2
            pasteY = (height - spec.height) / 2

            success = oiio.ImageBufAlgo.paste(extended, pasteX, pasteY, 0, 0, self.imgbuf)

            if success:
                self.imgbuf = extended

        return self

    def write(self, filename):
        self.imgbuf.write(filename)