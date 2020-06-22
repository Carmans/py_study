#encoding: utf-8

testl = {'key1': 2, 'key2': 3, 'key3': 4}

kv1 = testl.items()
# print(next(kv1))

kv2 = testl.iteritems()
print(next(kv2))
print(next(kv2))
print(next(kv2))