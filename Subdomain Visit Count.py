class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # so basically return the array of the count-paired domains in the format descibed in the question
        # in the output array ensure that ALL implicit domain rep's are summed
        # use a dictionary to store the domain along with its current res, incremement the res in the dictionary if we find another split apart subdomain with same domain while continuing to iterate cpdomains and simplify each domain
        # the hard part is simplifying each domain - just do a .split command to split each domain in cpdomains by "."
        # we can ensure that the rep is aligned still though by putting the split up domain in the same list as the rep
        freq = defaultdict(int)
    
        for domain in cpdomains:
            count, dom = domain.split(" ")
            count = int(count)
            parts = dom.split(".")
            for i in range(len(parts)):
                freq[".".join(parts[i:])] += count
        # [(9001, 'dicuss.leetcode.com', ...)]
        return [str(value) + " " + key for key, value in freq.items()]
            


            
