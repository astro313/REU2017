# Usage Example
import pdb


def add(aa, bb):
    s3 = aa + bb
    s3 = s3 * 2
    return s3

a = "a" * 4
pdb.set_trace()
b = "b" * 2
c = "c" * 3
final = add(a, b)
print final
