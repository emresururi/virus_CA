from pathlib import Path

from HexGrid import *

""" A supplementary code to generate a map (in SVG format) 
of the different indexes that can be used to refer to the cells.

The grid contained in str_header is prepared using xfig.
"""

fname = Path("supplementary/hex.svg")
print(fname.absolute())
str_header = '''<?xml version="1.0" standalone="no"?>
<!-- Creator: fig2dev Version 3.2.7a -->
<!-- CreationDate: 2020-08-21 11:16:20 -->
<!-- Magnification: 1.05 -->
<svg xmlns="http://www.w3.org/2000/svg"
 xmlns:xlink="http://www.w3.org/1999/xlink"
 width="812pt" height="589pt"
 viewBox="210 27 12880 9341">
<g fill="white">
<!-- Line -->
<polygon points=" 1433,2636 2028,2636 2326,2121 2028,1605 1433,1605 1134,2121"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 1433,3667 2028,3667 2326,3151 2028,2636 1433,2636 1134,3151"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 1433,4697 2028,4697 2326,4182 2028,3667 1433,3667 1134,4182"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 1433,5728 2028,5728 2326,5213 2028,4697 1433,4697 1134,5213"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 1433,6759 2028,6759 2326,6243 2028,5728 1433,5728 1134,6243"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 1433,7789 2028,7789 2326,7274 2028,6759 1433,6759 1134,7274"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 1433,8820 2028,8820 2326,8305 2028,7789 1433,7789 1134,8305"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 1433,1605 2028,1605 2326,1090 2028,575 1433,575 1134,1090"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 3222,2636 3816,2636 4114,2121 3816,1605 3222,1605 2923,2121"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 3222,3667 3816,3667 4114,3151 3816,2636 3222,2636 2923,3151"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 3222,4697 3816,4697 4114,4182 3816,3667 3222,3667 2923,4182"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 3222,5728 3816,5728 4114,5213 3816,4697 3222,4697 2923,5213"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 3222,6759 3816,6759 4114,6243 3816,5728 3222,5728 2923,6243"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 3222,7789 3816,7789 4114,7274 3816,6759 3222,6759 2923,7274"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 3222,8820 3816,8820 4114,8305 3816,7789 3222,7789 2923,8305"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 3222,1605 3816,1605 4114,1090 3816,575 3222,575 2923,1090"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5009,2636 5605,2636 5903,2121 5605,1605 5009,1605 4712,2121"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5009,3667 5605,3667 5903,3151 5605,2636 5009,2636 4712,3151"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5009,4697 5605,4697 5903,4182 5605,3667 5009,3667 4712,4182"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5009,5728 5605,5728 5903,5213 5605,4697 5009,4697 4712,5213"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5009,6759 5605,6759 5903,6243 5605,5728 5009,5728 4712,6243"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5009,7789 5605,7789 5903,7274 5605,6759 5009,6759 4712,7274"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5009,8820 5605,8820 5903,8305 5605,7789 5009,7789 4712,8305"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5009,1605 5605,1605 5903,1090 5605,575 5009,575 4712,1090"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 6798,2636 7394,2636 7691,2121 7394,1605 6798,1605 6501,2121"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 6798,3667 7394,3667 7691,3151 7394,2636 6798,2636 6501,3151"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 6798,4697 7394,4697 7691,4182 7394,3667 6798,3667 6501,4182"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 6798,5728 7394,5728 7691,5213 7394,4697 6798,4697 6501,5213"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 6798,6759 7394,6759 7691,6243 7394,5728 6798,5728 6501,6243"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 6798,7789 7394,7789 7691,7274 7394,6759 6798,6759 6501,7274"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 6798,8820 7394,8820 7691,8305 7394,7789 6798,7789 6501,8305"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 6798,1605 7394,1605 7691,1090 7394,575 6798,575 6501,1090"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 8587,2636 9182,2636 9480,2121 9182,1605 8587,1605 8290,2121"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 8587,3667 9182,3667 9480,3151 9182,2636 8587,2636 8290,3151"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 8587,4697 9182,4697 9480,4182 9182,3667 8587,3667 8290,4182"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 8587,5728 9182,5728 9480,5213 9182,4697 8587,4697 8290,5213"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 8587,6759 9182,6759 9480,6243 9182,5728 8587,5728 8290,6243"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 8587,7789 9182,7789 9480,7274 9182,6759 8587,6759 8290,7274"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 8587,8820 9182,8820 9480,8305 9182,7789 8587,7789 8290,8305"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 8587,1605 9182,1605 9480,1090 9182,575 8587,575 8290,1090"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 10376,2636 10971,2636 11269,2121 10971,1605 10376,1605 10078,2121"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 10376,3667 10971,3667 11269,3151 10971,2636 10376,2636 10078,3151"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 10376,4697 10971,4697 11269,4182 10971,3667 10376,3667 10078,4182"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 10376,5728 10971,5728 11269,5213 10971,4697 10376,4697 10078,5213"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 10376,6759 10971,6759 11269,6243 10971,5728 10376,5728 10078,6243"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 10376,7789 10971,7789 11269,7274 10971,6759 10376,6759 10078,7274"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 10376,8820 10971,8820 11269,8305 10971,7789 10376,7789 10078,8305"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 10376,1605 10971,1605 11269,1090 10971,575 10376,575 10078,1090"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 12164,2636 12760,2636 13057,2121 12760,1605 12164,1605 11867,2121"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 12164,3667 12760,3667 13057,3151 12760,2636 12164,2636 11867,3151"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 12164,4697 12760,4697 13057,4182 12760,3667 12164,3667 11867,4182"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 12164,5728 12760,5728 13057,5213 12760,4697 12164,4697 11867,5213"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 12164,6759 12760,6759 13057,6243 12760,5728 12164,5728 11867,6243"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 12164,7789 12760,7789 13057,7274 12760,6759 12164,6759 11867,7274"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 12164,8820 12760,8820 13057,8305 12760,7789 12164,7789 11867,8305"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 12164,1605 12760,1605 13057,1090 12760,575 12164,575 11867,1090"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 540,2121 1135,2121 1433,1605 1135,1090 540,1090 243,1605"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 540,3151 1135,3151 1433,2636 1135,2121 540,2121 243,2636"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 540,4182 1135,4182 1433,3667 1135,3151 540,3151 243,3667"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 540,5213 1135,5213 1433,4697 1135,4182 540,4182 243,4697"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 540,6243 1135,6243 1433,5728 1135,5213 540,5213 243,5728"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 540,7274 1135,7274 1433,6759 1135,6243 540,6243 243,6759"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 540,8305 1135,8305 1433,7789 1135,7274 540,7274 243,7789"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 540,9335 1135,9335 1433,8820 1135,8305 540,8305 243,8820"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 540,1090 1135,1090 1433,575 1135,60 540,60 243,575"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 2329,2121 2924,2121 3222,1605 2924,1090 2329,1090 2031,1605"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 2329,3151 2924,3151 3222,2636 2924,2121 2329,2121 2031,2636"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 2329,4182 2924,4182 3222,3667 2924,3151 2329,3151 2031,3667"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 2329,5213 2924,5213 3222,4697 2924,4182 2329,4182 2031,4697"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 2329,6243 2924,6243 3222,5728 2924,5213 2329,5213 2031,5728"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 2329,7274 2924,7274 3222,6759 2924,6243 2329,6243 2031,6759"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 2329,8305 2924,8305 3222,7789 2924,7274 2329,7274 2031,7789"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 2329,9335 2924,9335 3222,8820 2924,8305 2329,8305 2031,8820"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 2329,1090 2924,1090 3222,575 2924,60 2329,60 2031,575"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 4117,2121 4713,2121 5010,1605 4713,1090 4117,1090 3820,1605"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 4117,3151 4713,3151 5010,2636 4713,2121 4117,2121 3820,2636"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 4117,4182 4713,4182 5010,3667 4713,3151 4117,3151 3820,3667"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 4117,5213 4713,5213 5010,4697 4713,4182 4117,4182 3820,4697"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 4117,6243 4713,6243 5010,5728 4713,5213 4117,5213 3820,5728"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 4117,7274 4713,7274 5010,6759 4713,6243 4117,6243 3820,6759"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 4117,8305 4713,8305 5010,7789 4713,7274 4117,7274 3820,7789"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 4117,9335 4713,9335 5010,8820 4713,8305 4117,8305 3820,8820"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 4117,1090 4713,1090 5010,575 4713,60 4117,60 3820,575"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5906,2121 6502,2121 6799,1605 6502,1090 5906,1090 5609,1605"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5906,3151 6502,3151 6799,2636 6502,2121 5906,2121 5609,2636"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5906,4182 6502,4182 6799,3667 6502,3151 5906,3151 5609,3667"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5906,5213 6502,5213 6799,4697 6502,4182 5906,4182 5609,4697"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5906,6243 6502,6243 6799,5728 6502,5213 5906,5213 5609,5728"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5906,7274 6502,7274 6799,6759 6502,6243 5906,6243 5609,6759"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5906,8305 6502,8305 6799,7789 6502,7274 5906,7274 5609,7789"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5906,9335 6502,9335 6799,8820 6502,8305 5906,8305 5609,8820"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 5906,1090 6502,1090 6799,575 6502,60 5906,60 5609,575"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 7695,2121 8291,2121 8588,1605 8291,1090 7695,1090 7397,1605"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 7695,3151 8291,3151 8588,2636 8291,2121 7695,2121 7397,2636"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 7695,4182 8291,4182 8588,3667 8291,3151 7695,3151 7397,3667"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 7695,5213 8291,5213 8588,4697 8291,4182 7695,4182 7397,4697"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 7695,6243 8291,6243 8588,5728 8291,5213 7695,5213 7397,5728"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 7695,7274 8291,7274 8588,6759 8291,6243 7695,6243 7397,6759"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 7695,8305 8291,8305 8588,7789 8291,7274 7695,7274 7397,7789"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 7695,9335 8291,9335 8588,8820 8291,8305 7695,8305 7397,8820"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 7695,1090 8291,1090 8588,575 8291,60 7695,60 7397,575"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 9484,2121 10078,2121 10377,1605 10078,1090 9484,1090 9185,1605"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 9484,3151 10078,3151 10377,2636 10078,2121 9484,2121 9185,2636"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 9484,4182 10078,4182 10377,3667 10078,3151 9484,3151 9185,3667"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 9484,5213 10078,5213 10377,4697 10078,4182 9484,4182 9185,4697"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 9484,6243 10078,6243 10377,5728 10078,5213 9484,5213 9185,5728"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 9484,7274 10078,7274 10377,6759 10078,6243 9484,6243 9185,6759"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 9484,8305 10078,8305 10377,7789 10078,7274 9484,7274 9185,7789"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 9484,9335 10078,9335 10377,8820 10078,8305 9484,8305 9185,8820"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 9484,1090 10078,1090 10377,575 10078,60 9484,60 9185,575"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 11272,2121 11867,2121 12165,1605 11867,1090 11272,1090 10974,1605"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 11272,3151 11867,3151 12165,2636 11867,2121 11272,2121 10974,2636"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 11272,4182 11867,4182 12165,3667 11867,3151 11272,3151 10974,3667"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 11272,5213 11867,5213 12165,4697 11867,4182 11272,4182 10974,4697"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 11272,6243 11867,6243 12165,5728 11867,5213 11272,5213 10974,5728"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 11272,7274 11867,7274 12165,6759 11867,6243 11272,6243 10974,6759"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 11272,8305 11867,8305 12165,7789 11867,7274 11272,7274 10974,7789"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 11272,9335 11867,9335 12165,8820 11867,8305 11272,8305 10974,8820"
 stroke="#000000" stroke-width="30px"/>
<!-- Line -->
<polygon points=" 11272,1090 11867,1090 12165,575 11867,60 11272,60 10974,575"
 stroke="#000000" stroke-width="30px"/>
'''
str_footer = '''</g>
</svg>
'''

hex6 = HexGrid(7, 6, "tl")
bl = HexGrid(7, 6, "bl")
cent = HexGrid(7, 6, "center", (3, 2))

with open(fname, 'w') as writer:
    writer.write(str_header)
    for i in range(-2, 7):
        y = 2560 + i * 1040
        for j in range(-2, 12, 2):
            ii, jj = hex6.qr2ij((i, j))
            bl_x, bl_y = bl.qr2xy((i, j))
            cent_x, cent_y = cent.qr2xy((i, j))

            x = 2275 + j * 900
            # <g transform="translate(2340,3600) rotate(-60)" >
            string = '<g transform="translate({:},{:}) rotate(-60)" >\n<text xml:space="preserve" x="0" y="0" '\
                     'fill="#000000" font-family="Times" font-style="normal" font-weight="normal" font-size="192" '\
                     'text-anchor="start">{:2d},{:2d}</text>\n</g><!-- Text -->'.format(x, y, i, j)
            string_ij = '<g transform="translate({:},{:}) rotate(0)" >\n<text xml:space="preserve" x="0" y="0" '\
                        'fill="blue" font-family="Times" font-style="normal" font-weight="normal" font-size="192" '\
                        'text-anchor="start">{:2d},{:2d}</text>\n</g><!-- Text -->'.format(x + 200, y - 80, ii, jj)
            string_bl = '<g transform="translate({:},{:}) rotate(0)" >\n<text xml:space="preserve" x="0" y="0" '\
                        'fill="purple" font-family="Times" font-style="normal" font-weight="normal" font-size="192" '\
                        'text-anchor="start">{:2d},{:2d}</text>\n</g><!-- Text -->'.format(x + 200, y + 140, bl_x, bl_y)
            string_cent = '<g transform="translate({:},{:}) rotate(0)" >\n<text xml:space="preserve" x="0" y="0" '\
                          'fill="red" font-family="Times" font-style="normal" font-weight="normal" font-size="192" '\
                          'text-anchor="start">{:2d},{:2d}</text>\n</g><!-- Text -->'.format(x + 200,
                                                                                             y + 360, cent_x, cent_y)
            writer.write(string)
            writer.write(string_ij)
            writer.write(string_bl)
            writer.write(string_cent)

            ii, jj = hex6.qr2ij((i, j + 1))
            bl_x, bl_y = bl.qr2xy((i, j + 1))
            cent_x, cent_y = cent.qr2xy((i, j + 1))
            string = '<g transform="translate({:},{:}) rotate(-60)" >\n<text xml:space="preserve" x="0" y="0" '\
                     'fill="#000000" font-family="Times" font-style="normal" font-weight="normal" font-size="192" '\
                     'text-anchor="start">{:},{:}</text>\n</g><!-- Text -->'.format(x + 900, y - 540, i, j + 1)
            string_ij = '<g transform="translate({:},{:}) rotate(0)" >\n<text xml:space="preserve" x="0" y="0" '\
                        'fill="blue" font-family="Times" font-style="normal" font-weight="normal" font-size="192" '\
                        'text-anchor="start">{:},{:}</text>\n</g><!-- Text -->'.format(x + 1100, y - 620, ii, jj)
            string_bl = '<g transform="translate({:},{:}) rotate(0)" >\n<text xml:space="preserve" x="0" y="0" '\
                        'fill="purple" font-family="Times" font-style="normal" font-weight="normal" font-size="192" '\
                        'text-anchor="start">{:},{:}</text>\n</g><!-- Text -->'.format(x + 1100, y - 400, bl_x, bl_y)
            string_cent = '<g transform="translate({:2d},{:2d}) rotate(0)" >\n<text xml:space="preserve" x="0" y="0" '\
                          'fill="red" font-family="Times" font-style="normal" font-weight="normal" font-size="192" '\
                          'text-anchor="start">{:},{:}</text>\n</g><!-- Text -->'.format(x + 1100,
                                                                                         y - 180, cent_x, cent_y)
            writer.write(string)
            writer.write(string_ij)
            writer.write(string_bl)
            writer.write(string_cent)

    delta_l1 = 595
    delta_l2 = 1192
    delta_x = 298
    delta_y = 515
    x0, y0 = 2326, 2121
    line_color = 'purple'
    stroke_width = 90
    string = '<line x1="{:}" y1="{:}" x2="{:}" y2="{:}" style="stroke:{:};stroke-width:{:}" />\n'
    for y0 in (2121, 1030 * 8):
        for i in range(3):
            x1 = x0 + i * (delta_l1 + delta_l2)
            y1 = y0
            x2 = x1 + delta_l1
            y2 = y1
            writer.write(string.format(x1, y1, x2, y2, line_color, stroke_width))

            x1 = x2
            y1 = y2
            x2 = x1 + delta_x
            y2 = y1 - delta_y
            writer.write(string.format(x1, y1, x2, y2, line_color, stroke_width))

            x1 = x2
            y1 = y2
            x2 = x1 + delta_l1
            y2 = y1
            writer.write(string.format(x1, y1, x2, y2, line_color, stroke_width))

            x1 = x2
            y1 = y2
            x2 = x1 + delta_x
            y2 = y1 + delta_y
            writer.write(string.format(x1, y1, x2, y2, line_color, stroke_width))
        x1 = x2
        y1 = y2
        x2 = x1 + delta_l1
        y2 = y1
        writer.write(string.format(x1, y1, x2, y2, line_color, stroke_width))
    x0, y0 = 2326, 2121
    sign = 1
    for x0 in (2326, 1192 * 7):
        sign *= -1
        for i in range(6):
            x1 = x0
            y1 = y0 + i * 1030
            x2 = x1 + sign * delta_x
            y2 = y1 + delta_y
            writer.write(string.format(x1, y1, x2, y2, line_color, stroke_width))

            x1 = x2
            y1 = y2
            x2 = x1 - sign * delta_x
            y2 = y1 + delta_y
            writer.write(string.format(x1, y1, x2, y2, line_color, stroke_width))

    # Bring out the reference hexagons:
    string_hex6 = '<polygon points=" {:},{:} {:},{:} {:},{:} {:},{:} {:},{:} {:},{:}" stroke = "{:}" '\
                  'stroke-width = "{:}" fill="none" /> '
    line_color = "blue"
    x0, y0 = 2326, 2121  # "tl" reference cell
    writer.write(string_hex6.format(x0, y0,
                                    x0 + delta_l1, y0,
                                    x0 + delta_l1 + delta_x, y0 + delta_y,
                                    x0 + delta_l1, y0 + 2 * delta_y,
                                    x0, y0 + 2 * delta_y,
                                    x0 - delta_x, y0 + delta_y,
                                    line_color, stroke_width
                                    ))
    line_color = "red"
    x0, y0 = 2326 + delta_l1 + delta_l2, 2121 + 4 * delta_y  # "centered" reference cell
    writer.write(string_hex6.format(x0, y0,
                                    x0 + delta_l1, y0,
                                    x0 + delta_l1 + delta_x, y0 + delta_y,
                                    x0 + delta_l1, y0 + 2 * delta_y,
                                    x0, y0 + 2 * delta_y,
                                    x0 - delta_x, y0 + delta_y,
                                    line_color, stroke_width
                                    ))
    line_color = "purple"
    x0, y0 = 2326, 2121 + 10 * delta_y  # "bl" reference cell
    writer.write(string_hex6.format(x0, y0,
                                    x0 + delta_l1, y0,
                                    x0 + delta_l1 + delta_x, y0 + delta_y,
                                    x0 + delta_l1, y0 + 2 * delta_y,
                                    x0, y0 + 2 * delta_y,
                                    x0 - delta_x, y0 + delta_y,
                                    line_color, stroke_width
                                    ))
    writer.write(str_footer)
