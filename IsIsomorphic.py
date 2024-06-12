    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        z_set = set(zip(s, t))
        return len(z_set) == len(set(s)) == len(set(t))
