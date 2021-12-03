import fileinput
import operator

def filter_prefix(candidates: set[str], prefix: str = '', ones_operator=operator.ge) -> int:
    """Filter a set of binary number strings by prefix, returning a single int.

    This function considers a set of candidate strings, which must encode
    valid binary numbers. They are iteratively filtered by prefix, selecting
    each bit by whether it is the more common or less common place value for
    each successive bit (MSB first), until only a single value remains with
    that prefix, which is returned as an int.

    Specific behavior is determined by the ones_operator parameter:
    
    `ge`: Select the more common value for prefix, ties resolved to '1'
    `gt`: Select the more common value for prefix, ties resolved to '0'
    `le`: Select the less common value for prefix, ties resolved to '1'
    `lt`: Select the less common value for prefix, ties resolved to '0'

    """
    # Base case; when we're down to just one option, pop it and
    #  return it as an int:
    if len(candidates) == 1:
        return int(candidates.pop(), base=2)

    # The sets of candidates with a '1' vs '0' in the next bit to consider:
    ones = set()
    zeroes = set()
    candidate_count = len(candidates)

    # Consider each candidate binary number and sort it into the ones or zeroes
    #  sets based on the value in the next bit place under consideration
    #  (which corresponds to len(prefix)):
    while len(candidates):
        candidate = candidates.pop()
        if candidate[len(prefix)] == '1':
            ones.add(candidate)
        else:
            zeroes.add(candidate)
    
    # Use the supplied operator (less-than or greater-equal) to compare
    #  the ones and zeroes sets, selecting the ones set if the operation
    #  supplied returns True, and the zeroes set if the operation returns
    #  False.
    if ones_operator(len(ones), candidate_count/2.0):
        return filter_prefix(ones, prefix + '1', ones_operator)
    else:
        return filter_prefix(zeroes, prefix + '0', ones_operator)


def main():
    common_candidates = set(fileinput.input())
    
    print(filter_prefix(common_candidates.copy(), ones_operator=operator.lt) * \
          filter_prefix(common_candidates, ones_operator=operator.ge))


if __name__ == '__main__':
    main()
