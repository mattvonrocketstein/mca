"""
"""

from unittest2 import TestCase
from mca import META1

class Class1(object):
    __metaclass__ = META1

    def foo(self): return 'foo'

class Class2(object):
    __metaclass__ = META1

    def bar(self): return 'bar'

class Mixin1(object):
    def baz(self): return 'baz'

class TestStuff(TestCase):

    def setUp(self):
        pass

    def test_lshift_with_bad_args(self):
        with self.assertRaises(TypeError):
            Class3 = Class1<<Class2
        with self.assertRaises(TypeError):
            Class3 = Class1<<3
    def test_rshift_with_bag_args(self):
        with self.assertRaises(TypeError):
            Class3 = Class1>>Class2
        with self.assertRaises(TypeError):
            Class3 = Class1>>3

    def test_lshift_with_legit_args(self):
        Class3 =  Class1 << Mixin1
        class3 = Class3()
        self.assertTrue(hasattr(class3, 'foo'))
        self.assertTrue(hasattr(class3, 'baz'))
        self.assertTrue(class3.foo(),'foo')
        self.assertTrue(class3.baz(),'baz')

    def test_rshift_with_legit_args(self):
        Class3 =  Class1 >> Mixin1
        class3 = Class3()
        self.assertTrue(hasattr(class3, 'foo'))
        self.assertTrue(hasattr(class3, 'baz'))
        self.assertTrue(class3.foo(),'foo')
        self.assertTrue(class3.baz(),'baz')

    def test_shift_ops_return_new_classes(self):
        # No caching allowed.
        Class31 =  Class1 >> Mixin1
        Class32 =  Class1 >> Mixin1
        Class41 =  Class1 << Mixin1
        Class42 =  Class1 << Mixin1
        self.assertNotEqual(Class31, Class32)
        self.assertNotEqual(Class41, Class42)

    def test_compositing_with_namespace_overlap(self):
        #with self.assertRaises(TypeError):
        pass

    def test_compositing_with_no_namespace_overlap(self):
        pass
