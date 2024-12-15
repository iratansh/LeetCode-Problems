uint32_t reverseBits(uint32_t n) {
    uint32_t res = 0;

    for (int i = 0; i < 32; i++) {
        uint32_t b = (n >> i) & 1;
        res = res | (b << (31 - i));
    }
    return res;
}
