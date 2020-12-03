class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        if count_a < count_b:# a为更多的pattern
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        if not value:#value空 pattern里都是a
            return count_b == 0
        if not pattern:
            return False

        for len_a in range(len(value) // count_a + 1):###每个a代表的长度
            rest = len(value) - count_a * len_a#rest为除a代表长度外的长度
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
                len_b = 0 if count_b == 0 else rest // count_b
                pos, correct = 0, True
                value_a, value_b = None, None#首先对a,b代表的字符串赋空
            
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos+len_a]#substring为 当前位置：当前位置+len_a
                        if not value_a:#第一次碰到a 对a赋substring
                            value_a = sub
                        elif value_a != sub:#第k次碰到a 判断a==substring  不等就返回false
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos+len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:#跑完一轮如果correct依然是True 且a,b代表不同的字符串
                    return True
        return False