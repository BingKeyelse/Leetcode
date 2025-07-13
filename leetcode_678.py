class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        star_near= []  # lưu trữ star gần nhất
        sym_near=[] # lưu trữ kí hiệu '(' gần nhất có thể 

        for i, sym in enumerate(s):
            if  len(sym_near)==0 and len(star_near)==0 and sym == ')': # nếu chưa gì mà không có '(' hay '*' 
                                                                        # thì nó đóng ')' thì false luôn
                return False
            else:
                if sym== ')' and len(sym_near)>0: # ưu tiên từ '(' trước
                    sym_near.pop()
                elif sym== ')'and len(star_near)>0:  # sau cùng mới là '*' 
                    star_near.pop()
                elif sym== '(':
                    sym_near.append(i)
                else:
                    star_near.append(i)
                    
        # Triệt tiêu cả '(' nữa chứ chứ không là fail bài này
        if len(star_near)< len(sym_near):
            return False
        else:
            while len(sym_near)>0:
                if star_near[-1]>sym_near[-1]:
                    star_near.pop()
                    sym_near.pop()
                else:
                    return False
        return True
                     
s = "(*))"
print(Solution().checkValidString(s))                  


                            