import fileinput
import math

class BitsPacket:
    OP_SUM = 0
    OP_PRD = 1
    OP_MIN = 2
    OP_MAX = 3
    OP_GRT = 5
    OP_LST = 6
    OP_EQL = 7

    def __init__(self, hex_string, msb_at=15):
        self.subpackets = []

        self._len = 0 # Length in bits
        self.hex = hex_string
        self.current_word = int(self.hex[:4], base=16)
        self.msb_at = msb_at
        
        # bits msb..msb-3   -> version
        self.version = self._get_next_n_bits(3)
        # bits msb-3..msb-6 -> type
        self.type = self._get_next_n_bits(3)

        self.value = 0

        if self.type == 4:
            self._parse_literal()
        else:
            self._parse_operator()

        self.enclosed_version_total = self.version + sum(encl.enclosed_version_total for encl in self.subpackets)

    def _get_next_n_bits(self, n):
        # The number of bits we have available to feed is msb+1
        val = 0
        while n > self.msb_at+1:
            num_getting = self.msb_at+1
            adder = self._get_next_n_bits(num_getting)
            val += adder
            n -= (num_getting)
            # Now left-shift val by the number of bits we still need:
            val = val << min(num_getting, n)

        val += (self.current_word >> (self.msb_at+1-n)) & (0xffff >> (16-n))
        # print(f"msb at {self.msb_at}, current word {self.hex[:4]} ({self.current_word}) >> {self.msb_at+1-n} mask {0xffff >> (16-n)}, val {(self.current_word >> (self.msb_at+1-n)) & (0xffff >> (16-n))} {bin(val)}")
        self._advance_window(n)
        return val

    def _advance_window(self, msb_decr):
        self.msb_at -= msb_decr

        
        # *** TODO: Handle if we're on the last byte. (though my input works fine)

        while len(self.hex) > 2 and self.msb_at < 8: # it's in the lower half of the word
            self.msb_at += 8
            self.hex = self.hex[2:] # Chop off the fully used MSByte.
        # Update the current word:
        self.current_word = int(self.hex[:2+2], base=16)

        self._len += msb_decr

    def _parse_literal(self):
        self.value = 0
        while True:
            frame = self._get_next_n_bits(5)
            more = frame & 0b10000
            val  = frame & 0b01111

            self.value = self.value << 4
            self.value += val

            if not more:
                return

    def _parse_operator(self):
        len_is_packets = self._get_next_n_bits(1)
        len_val = self._get_next_n_bits(11 if len_is_packets else 15)

        while len_val > 0: # TODO not this
            subfield = BitsPacket(self.hex, self.msb_at)
            if len_is_packets:
                len_val -= 1
            else:
                len_val -= len(subfield)
            self.subpackets.append(subfield)
            self._advance_window(len(subfield))
        
        if self.type == BitsPacket.OP_SUM:
            self.value = sum(map(lambda a: a.value, self.subpackets))
        elif self.type == BitsPacket.OP_PRD:
            self.value = math.prod(map(lambda a: a.value, self.subpackets))
        elif self.type == BitsPacket.OP_MAX:
            self.value = max(map(lambda a: a.value, self.subpackets))
        elif self.type == BitsPacket.OP_MIN:
            self.value = min(map(lambda a: a.value, self.subpackets))
        elif self.type == BitsPacket.OP_GRT:
            self.value = int(self.subpackets[0].value > self.subpackets[1].value)
        elif self.type == BitsPacket.OP_LST:
            self.value = int(self.subpackets[0].value < self.subpackets[1].value)
        elif self.type == BitsPacket.OP_EQL:
            self.value = 1 if self.subpackets[0].value == self.subpackets[1].value else 0
        else:
            raise ValueError(f"Bad opcode {self.type}.")

    def __str__(self):
        return f"BitsPacket(version={self.version}, type={self.type}, value={self.value}, total_vers={self.enclosed_version_total}, len={self._len}, subs=[{','.join(map(str, self.subpackets))}])"
    
    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self._len

def main():
    hex_string = fileinput.input().readline().strip()
    print(BitsPacket(hex_string).value)
    pass

if __name__ == '__main__':
    main()
