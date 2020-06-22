#encoding: utf-8

#arg
def test_args(first, *args):
   print first
   for v in args:
      print "args %s" % v

#args = (2, 3, 4, 5)
test_args(1, 2, 3, 4, 5, 6)

#kwargs
def test_kwargs(first, *args, **kwargs):
   print first
   for v in args:
      print "args %s" % v
   for k, v in kwargs.items():
      print "kwargs", (k, v)
#args = (2, 3, 4, 5)
#kwargs: k1=5, k2=6, k0=4
test_kwargs(1, 2, 3, 4, 5, k0=4, k1=5, k2=6)