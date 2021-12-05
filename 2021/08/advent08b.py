import fileinput
from collections import namedtuple

def main():
     output_total = 0
     for line in fileinput.input():
          segment_digit_map = dict()
          digit_segments_map = dict()

          ten_digits, output_digits = line.split(' | ')
          ten_digits = ten_digits.split()
          ten_digits = list(map(frozenset, ten_digits))
          ten_digits = sorted(ten_digits, key=len)

          # ten_digits will be in order of number of segments, to wit:
          #  2 3 4 5 5 5 6 6 6 7
          # So, ten_digits[0] -> "1"
          segment_digit_map[ten_digits[0]] = 1
          digit_segments_map[1] = ten_digits[0]
          #     ten_digits[1] -> "7"
          segment_digit_map[ten_digits[1]] = 7
          digit_segments_map[7] = ten_digits[1]
          #     ten_digits[2] -> "4"
          segment_digit_map[ten_digits[2]] = 4
          digit_segments_map[4] = ten_digits[2]
          #     ten_digits[9] -> "8"
          segment_digit_map[ten_digits[9]] = 8
          digit_segments_map[8] = ten_digits[9]

          for segment_group in ten_digits[3:6]: # the 5-length groups               
               if len(segment_group - digit_segments_map[4]) == 3:
                    # 2: the 5-len with 3 segments not in 4
                    digit_segments_map[2] = segment_group
                    segment_digit_map[segment_group] = 2
               elif len(segment_group - digit_segments_map[7]) == 2:
                    # 3: the 5-len with 2 segments not in 7
                    digit_segments_map[3] = segment_group
                    segment_digit_map[segment_group] = 3
               elif len(segment_group - digit_segments_map[7]) == 3:
                    # 5: the 5-len with 3 segments not in 7
                    digit_segments_map[5] = segment_group
                    segment_digit_map[segment_group] = 5

          for segment_group in ten_digits[6:9]: # the 6-length groups
               if len(digit_segments_map[4] - segment_group) == 0:
                    # 9: the 6-len that contains every segment in "4"
                    digit_segments_map[9] = segment_group
                    segment_digit_map[segment_group] = 9
               elif len(digit_segments_map[7] - segment_group) == 0:
                    # 0: the 6-len that contains every segment in 7 but not in 4
                    digit_segments_map[0] = segment_group
                    segment_digit_map[segment_group] = 0
               else:
                    # 6: the other one
                    digit_segments_map[6] = segment_group
                    segment_digit_map[segment_group] = 6

          output_digits_translated = ''
          output_digit_segs = list(map(frozenset, output_digits.split()))
          for segs in output_digit_segs:
               output_digits_translated += str(segment_digit_map[segs])

          output_total += int(output_digits_translated)     
     print(output_total)

          

if __name__ == '__main__':
    main()
