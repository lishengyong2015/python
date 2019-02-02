Run Length Encoding（RLE）行程长度的原理是将字符串的连续重复字符用一个计数值和字符代替。
比如，数据项为
AA AA BB C0 C0 C0 C0 FF FF FF FF FF FF （13字节）
可以视为  2*AA + BB + 4*C0 + 6*FF
压缩为  02  AA  01  BB  04 C0  06 FF  （8个字节)
本代码为python版本，可直接操作二进制数据。

