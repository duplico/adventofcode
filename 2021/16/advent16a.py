import fileinput
import math

class BitsPacket:
    def __init__(self, hex_string, msb_at=15):
        self.subpackets = []

        self._len = 0 # Length in bits
        self.hex = hex_string
        self.current_word = int(self.hex[:4], base=16)
        self.msb_at = msb_at
        
        self.version = self._get_next_n_bits(3)
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
        while self.msb_at < 8: # it's in the lower half of the word
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

        while len_val:
            subfield = BitsPacket(self.hex, self.msb_at)
            if len_is_packets:
                len_val -= 1
            else:
                len_val -= len(subfield)
            self.subpackets.append(subfield)
            self._advance_window(len(subfield))

    def __str__(self):
        return f"BitsPacket(version={self.version}, type={self.type}, value={self.value}, total_vers={self.enclosed_version_total}, len={self._len}, subs=[{','.join(map(str, self.subpackets))}])"
    
    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self._len

def main():
    # We add 0x00-pads to the end to prevent overruns; because the
    #  hexstring-to-binary conversion works on 16 bits at a time,
    #  and because ending zero-pads are ignored, this is safe to do.
    hex_string = fileinput.input().readline().strip() + '0000'
    print(BitsPacket(hex_string).enclosed_version_total)
    pass

if __name__ == '__main__':
    main()
