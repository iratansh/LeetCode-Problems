class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        valid_v4, check_v4, valid_v6, check_v6 = False, False, False, False
        
        # check whether to test for v4 or v6 ips
        if "." in queryIP:
            ip = queryIP.split(".")
            check_v4 = True if len(ip) == 4 else False
        else:
            ip = queryIP.split(":")
            check_v6 = True if len(ip) == 8 else False
         
        if check_v4:
            for el in ip:
                if el == "" or len(el) > 1 and el[0] == '0':
                    return "Neither"
                for char in el:
                    if not char.isdigit():
                        return "Neither"
                if int(el) > 255:
                    return "Neither"
            return "IPv4"
        elif check_v6:
            for el in ip:
                if el == "" or len(el) > 4:
                    return "Neither"
                for i in el:
                    if i.isalpha():
                        if i.lower() not in 'abcdef':
                            return "Neither"
                    elif i.isdigit():
                        pass
                    else:
                        return "Neither"
            return "IPv6"
        return "Neither"
