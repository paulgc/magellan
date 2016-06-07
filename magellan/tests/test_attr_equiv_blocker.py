import os
from nose.tools import *
import pandas as pd
from pandas.util.testing import assert_frame_equal
import unittest

import magellan as mg

p = mg.get_install_path()
path_for_A = os.sep.join([p, 'datasets', 'table_A.csv'])
path_for_B = os.sep.join([p, 'datasets', 'table_B.csv'])
l_key = 'ID'
r_key = 'ID'
l_block_attr_1 = 'zipcode'
l_block_attr_2 = 'birth_year'
l_block_attr_3 = 'name'
r_block_attr_1 = 'zipcode'
r_block_attr_2 = 'birth_year'
r_block_attr_3 = 'name'
l_output_attrs = ['zipcode', 'birth_year']
r_output_attrs = ['zipcode', 'birth_year']
l_output_prefix = 'l_'
r_output_prefix = 'r_'

bogus_attr = 'bogus'
block_attr_multi = ['zipcode', 'birth_year']


class AttrEquivBlockerTestCases(unittest.TestCase):

    def setUp(self):
        self.A = mg.read_csv_metadata(path_for_A)
        mg.set_key(self.A, l_key)
        self.B = mg.read_csv_metadata(path_for_B)
        mg.set_key(self.B, r_key)
        self.ab = mg.AttrEquivalenceBlocker()
        
    def tearDown(self):
        del self.A
        del self.B
        del self.ab

    @raises(AssertionError)
    def test_ab_block_tables_invalid_ltable_1(self):
        self.ab.block_tables(None, self.B, l_block_attr_1, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_ltable_2(self):
        self.ab.block_tables([10, 10], self.B, l_block_attr_1, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_ltable_3(self):
        self.ab.block_tables(pd.DataFrame(), self.B, l_block_attr_1, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_rtable_1(self):
        self.ab.block_tables(self.A, None, l_block_attr_1, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_rtable_2(self):
        self.ab.block_tables(self.A, [10, 10], l_block_attr_1, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_rtable_3(self):
        self.ab.block_tables(self.A, pd.DataFrame(), l_block_attr_1, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_l_block_attr_1(self):
        self.ab.block_tables(self.A, self.B, None, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_l_block_attr_2(self):
        self.ab.block_tables(self.A, self.B, 10, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_l_block_attr_3(self):
        self.ab.block_tables(self.A, self.B, True, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_bogus_l_block_attr(self):
        self.ab.block_tables(self.A, self.B, bogus_attr, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_multi_l_block_attr(self):
        self.ab.block_tables(self.A, self.B, block_attr_multi, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_r_block_attr_1(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, None)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_r_block_attr_2(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, 10)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_r_block_attr_3(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, True)

    @raises(AssertionError)
    def test_ab_block_tables_bogus_r_block_attr(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, bogus_attr)

    @raises(AssertionError)
    def test_ab_block_tables_multi_r_block_attr(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, block_attr_multi)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_l_output_attrs_1(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, 1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_l_output_attrs_2(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, 'name')

    @raises(AssertionError)
    def test_ab_block_tables_invalid_l_output_attrs_3(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, [1, 2])

    @raises(AssertionError)
    def test_ab_block_tables_bogus_l_output_attrs(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, [bogus_attr])

    @raises(AssertionError)
    def test_ab_block_tables_invalid_r_output_attrs_1(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, r_output_attrs=1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_r_output_attrs_2(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, r_output_attrs='name')

    @raises(AssertionError)
    def test_ab_block_tables_invalid_r_output_attrs_3(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, r_output_attrs=[1, 2])

    @raises(AssertionError)
    def test_ab_block_tables_bogus_r_output_attrs(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, r_output_attrs=[bogus_attr])

    @raises(AssertionError)
    def test_ab_block_tables_invalid_l_output_prefix_1(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_prefix=None)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_l_output_prefix_2(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_prefix=1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_l_output_prefix_3(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_prefix=True)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_r_output_prefix_1(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, r_output_prefix=None)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_r_output_prefix_2(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, r_output_prefix=1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_r_output_prefix_3(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, r_output_prefix=True)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_verbose_1(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, verbose=None)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_verbose_2(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, verbose=1)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_verbose_3(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, verbose='yes')

    @raises(AssertionError)
    def test_ab_block_tables_invalid_njobs_1(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, n_jobs=None)

    @raises(AssertionError)
    def test_ab_block_tables_invalid_njobs_2(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, n_jobs='1')

    @raises(AssertionError)
    def test_ab_block_tables_invalid_njobs_3(self):
        self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, n_jobs=1.5)

    def test_ab_block_tables(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix)
        s1 = ['_id', l_output_prefix + l_key, r_output_prefix + r_key]
        s1 += [l_output_prefix + x for x in l_output_attrs if x != l_key]
        s1 += [r_output_prefix + x for x in r_output_attrs if x != r_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), l_output_prefix + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), r_output_prefix + r_key)
        k1 = pd.np.array(C[l_output_prefix + l_block_attr_1])
        k2 = pd.np.array(C[r_output_prefix + r_block_attr_1])
        assert_equal(all(k1 == k2), True)

    def test_ab_block_tables_wi_no_output_tuples(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_3, r_block_attr_3)
        assert_equal(len(C),  0)
        assert_equal(sorted(C.columns), sorted(['_id', 'ltable_' + l_key,
                                                'rtable_' + r_key]))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_null_l_output_attrs(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, None, r_output_attrs)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['rtable_' + x for x in r_output_attrs if x != r_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_null_r_output_attrs(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs, None)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['ltable_' + x for x in l_output_attrs if x != l_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_empty_l_output_attrs(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, [], r_output_attrs)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['rtable_' + x for x in r_output_attrs if x != r_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_empty_r_output_attrs(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs, [])
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['ltable_' + x for x in l_output_attrs if x != l_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix, n_jobs=2)
        s1 = ['_id', l_output_prefix + l_key, r_output_prefix + r_key]
        s1 += [l_output_prefix + x for x in l_output_attrs if x != l_key]
        s1 += [r_output_prefix + x for x in r_output_attrs if x != r_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), l_output_prefix + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), r_output_prefix + r_key)
        k1 = pd.np.array(C[l_output_prefix + l_block_attr_1])
        k2 = pd.np.array(C[r_output_prefix + r_block_attr_1])
        assert_equal(all(k1 == k2), True)

    def test_ab_block_tables_njobs_2_eq_1(self):
        C1 = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix, n_jobs=1)
        C2 = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix, n_jobs=2)
        C1 = C1.sort_values(by=[l_output_prefix + l_key, r_output_prefix + r_key])	
        C2 = C2.sort_values(by=[l_output_prefix + l_key, r_output_prefix + r_key])
        s1 = pd.np.array(C1[l_output_prefix + l_key])
        s2 = pd.np.array(C1[r_output_prefix + r_key])
        t1 = pd.np.array(C2[l_output_prefix + l_key])
        t2 = pd.np.array(C2[r_output_prefix + r_key])
        assert_equal(all(s1 == t1), True)
        assert_equal(all(s2 == t2), True)

    def test_ab_block_tables_wi_no_output_tuples_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_3, r_block_attr_3, n_jobs=2)
        assert_equal(len(C),  0)
        assert_equal(sorted(C.columns), sorted(['_id', 'ltable_' + l_key,
                                                'rtable_' + r_key]))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_null_l_output_attrs_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, None, r_output_attrs, n_jobs=2)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['rtable_' + x for x in r_output_attrs if x != r_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_null_r_output_attrs_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs, None, n_jobs=2)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['ltable_' + x for x in l_output_attrs if x != l_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_empty_l_output_attrs_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, [], r_output_attrs, n_jobs=2)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['rtable_' + x for x in r_output_attrs if x != r_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_empty_r_output_attrs_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs, [], n_jobs=2)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['ltable_' + x for x in l_output_attrs if x != l_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_njobs_all(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix, n_jobs=-1)
        s1 = ['_id', l_output_prefix + l_key, r_output_prefix + r_key]
        s1 += [l_output_prefix + x for x in l_output_attrs if x != l_key]
        s1 += [r_output_prefix + x for x in r_output_attrs if x != r_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), l_output_prefix + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), r_output_prefix + r_key)
        k1 = pd.np.array(C[l_output_prefix + l_block_attr_1])
        k2 = pd.np.array(C[r_output_prefix + r_block_attr_1])
        assert_equal(all(k1 == k2), True)

    def test_ab_block_tables_njobs_all_eq_1(self):
        C1 = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix, n_jobs=1)
        C2 = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix, n_jobs=-1)
        C1 = C1.sort_values(by=[l_output_prefix + l_key, r_output_prefix + r_key])	
        C2 = C2.sort_values(by=[l_output_prefix + l_key, r_output_prefix + r_key])
        s1 = pd.np.array(C1[l_output_prefix + l_key])
        s2 = pd.np.array(C1[r_output_prefix + r_key])
        t1 = pd.np.array(C2[l_output_prefix + l_key])
        t2 = pd.np.array(C2[r_output_prefix + r_key])
        assert_equal(all(s1 == t1), True)
        assert_equal(all(s2 == t2), True)

    def test_ab_block_tables_wi_no_output_tuples_njobs_all(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_3, r_block_attr_3, n_jobs=-1)
        assert_equal(len(C),  0)
        assert_equal(sorted(C.columns), sorted(['_id', 'ltable_' + l_key,
                                                'rtable_' + r_key]))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_null_l_output_attrs_njobs_all(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, None, r_output_attrs, n_jobs=-1)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['rtable_' + x for x in r_output_attrs if x != r_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_null_r_output_attrs_njobs_all(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs, None, n_jobs=-1)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['ltable_' + x for x in l_output_attrs if x != l_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_empty_l_output_attrs_njobs_all(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, [], r_output_attrs, n_jobs=-1)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['rtable_' + x for x in r_output_attrs if x != r_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    def test_ab_block_tables_wi_empty_r_output_attrs_njobs_all(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs, [], n_jobs=-1)
        s1 = ['_id', 'ltable_' + l_key, 'rtable_' + r_key]
        s1 += ['ltable_' + x for x in l_output_attrs if x != l_key]
        s1 = sorted(s1)
        assert_equal(s1, sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(C, 'fk_ltable'), 'ltable_' + l_key)
        assert_equal(mg.get_property(C, 'fk_rtable'), 'rtable_' + r_key)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_candset_1(self):
        self.ab.block_candset(None, l_block_attr_1, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_candset_2(self):
        self.ab.block_candset([10, 10], l_block_attr_1, r_block_attr_1)

    @raises(KeyError)
    def test_ab_block_candset_invalid_candset_3(self):
        self.ab.block_candset(pd.DataFrame(), l_block_attr_1, r_block_attr_1)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_l_block_attr_1(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, None, r_block_attr_2)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_l_block_attr_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, 10, r_block_attr_2)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_l_block_attr_3(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, True, r_block_attr_2)

    @raises(AssertionError)
    def test_ab_block_candset_bogus_l_block_attr(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, bogus_attr, r_block_attr_2)

    @raises(AssertionError)
    def test_ab_block_candset_multi_l_block_attr(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, block_attr_multi, r_block_attr_2)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_r_block_attr_1(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, None)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_r_block_attr_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, 10)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_r_block_attr_3(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, True)

    @raises(AssertionError)
    def test_ab_block_candset_bogus_r_block_attr(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, bogus_attr)

    @raises(AssertionError)
    def test_ab_block_candset_multi_r_block_attr(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, block_attr_multi)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_verbose_1(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, None)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_verbose_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, 1)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_verbose_3(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, 'yes')

    @raises(AssertionError)
    def test_ab_block_candset_invalid_show_progress_1(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, show_progress=None)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_show_progress_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, show_progress=1)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_show_progress_3(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, show_progress='yes')

    @raises(AssertionError)
    def test_ab_block_candset_invalid_njobs_1(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=None)

    @raises(AssertionError)
    def test_ab_block_candset_invalid_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs='1')

    @raises(AssertionError)
    def test_ab_block_candset_invalid_njobs_3(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=1.5)

    def test_ab_block_candset(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix)
        D = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2)
        assert_equal(sorted(C.columns), sorted(D.columns))
        assert_equal(mg.get_key(D), '_id')
        assert_equal(mg.get_property(D, 'fk_ltable'), mg.get_property(C, 'fk_ltable'))
        assert_equal(mg.get_property(D, 'fk_rtable'), mg.get_property(C, 'fk_rtable'))
        k1 = pd.np.array(D[l_output_prefix + l_block_attr_2])
        k2 = pd.np.array(D[r_output_prefix + r_block_attr_2])
        assert_equal(all(k1 == k2), True)

    def test_ab_block_candset_empty_input(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_3, r_block_attr_3)
        assert_equal(len(C),  0)
        D = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2)
        assert_equal(len(D),  0)
        assert_equal(sorted(D.columns), sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(D, 'fk_ltable'), mg.get_property(C, 'fk_ltable'))
        assert_equal(mg.get_property(D, 'fk_rtable'), mg.get_property(C, 'fk_rtable'))

    def test_ab_block_candset_empty_output(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        D = self.ab.block_candset(C, l_block_attr_3, r_block_attr_3)
        assert_equal(len(D),  0)
        assert_equal(sorted(D.columns), sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(D, 'fk_ltable'), mg.get_property(C, 'fk_ltable'))
        assert_equal(mg.get_property(D, 'fk_rtable'), mg.get_property(C, 'fk_rtable'))

    def test_ab_block_candset_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix)
        D = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=2)
        assert_equal(sorted(C.columns), sorted(D.columns))
        assert_equal(mg.get_key(D), '_id')
        assert_equal(mg.get_property(D, 'fk_ltable'), mg.get_property(C, 'fk_ltable'))
        assert_equal(mg.get_property(D, 'fk_rtable'), mg.get_property(C, 'fk_rtable'))
        k1 = pd.np.array(D[l_output_prefix + l_block_attr_2])
        k2 = pd.np.array(D[r_output_prefix + r_block_attr_2])
        assert_equal(all(k1 == k2), True)

    def test_ab_block_candset_njobs_2_eq_1(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix)
        D1 = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=1)
        D2 = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=2)
        D1 = D1.sort_values(by=[l_output_prefix + l_key, r_output_prefix + r_key])	
        D2 = D2.sort_values(by=[l_output_prefix + l_key, r_output_prefix + r_key])
        s1 = pd.np.array(D1[l_output_prefix + l_key])
        s2 = pd.np.array(D1[r_output_prefix + r_key])
        t1 = pd.np.array(D2[l_output_prefix + l_key])
        t2 = pd.np.array(D2[r_output_prefix + r_key])
        assert_equal(all(s1 == t1), True)
        assert_equal(all(s2 == t2), True)

    def test_ab_block_candset_empty_input_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_3, r_block_attr_3)
        assert_equal(len(C),  0)
        D = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=2)
        assert_equal(len(D),  0)
        assert_equal(sorted(D.columns), sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(D, 'fk_ltable'), mg.get_property(C, 'fk_ltable'))
        assert_equal(mg.get_property(D, 'fk_rtable'), mg.get_property(C, 'fk_rtable'))

    def test_ab_block_candset_empty_output_njobs_2(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        D = self.ab.block_candset(C, l_block_attr_3, r_block_attr_3, n_jobs=2)
        assert_equal(len(D),  0)
        assert_equal(sorted(D.columns), sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(D, 'fk_ltable'), mg.get_property(C, 'fk_ltable'))
        assert_equal(mg.get_property(D, 'fk_rtable'), mg.get_property(C, 'fk_rtable'))

    def test_ab_block_candset_njobs_all(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix)
        D = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=-1)
        assert_equal(sorted(C.columns), sorted(D.columns))
        assert_equal(mg.get_key(D), '_id')
        assert_equal(mg.get_property(D, 'fk_ltable'), mg.get_property(C, 'fk_ltable'))
        assert_equal(mg.get_property(D, 'fk_rtable'), mg.get_property(C, 'fk_rtable'))
        k1 = pd.np.array(D[l_output_prefix + l_block_attr_2])
        k2 = pd.np.array(D[r_output_prefix + r_block_attr_2])
        assert_equal(all(k1 == k2), True)

    def test_ab_block_candset_njobs_all_eq_1(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1, l_output_attrs,
                            r_output_attrs, l_output_prefix, r_output_prefix)
        D1 = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=1)
        D2 = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=-1)
        D1 = D1.sort_values(by=[l_output_prefix + l_key, r_output_prefix + r_key])	
        D2 = D2.sort_values(by=[l_output_prefix + l_key, r_output_prefix + r_key])
        s1 = pd.np.array(D1[l_output_prefix + l_key])
        s2 = pd.np.array(D1[r_output_prefix + r_key])
        t1 = pd.np.array(D2[l_output_prefix + l_key])
        t2 = pd.np.array(D2[r_output_prefix + r_key])
        assert_equal(all(s1 == t1), True)
        assert_equal(all(s2 == t2), True)

    def test_ab_block_candset_empty_input_njobs_all(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_3, r_block_attr_3)
        assert_equal(len(C),  0)
        D = self.ab.block_candset(C, l_block_attr_2, r_block_attr_2, n_jobs=-1)
        assert_equal(len(D),  0)
        assert_equal(sorted(D.columns), sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(D, 'fk_ltable'), mg.get_property(C, 'fk_ltable'))
        assert_equal(mg.get_property(D, 'fk_rtable'), mg.get_property(C, 'fk_rtable'))

    def test_ab_block_candset_empty_output_njobs_all(self):
        C = self.ab.block_tables(self.A, self.B, l_block_attr_1, r_block_attr_1)
        D = self.ab.block_candset(C, l_block_attr_3, r_block_attr_3, n_jobs=-1)
        assert_equal(len(D),  0)
        assert_equal(sorted(D.columns), sorted(C.columns))
        assert_equal(mg.get_key(C), '_id')
        assert_equal(mg.get_property(D, 'fk_ltable'), mg.get_property(C, 'fk_ltable'))
        assert_equal(mg.get_property(D, 'fk_rtable'), mg.get_property(C, 'fk_rtable'))

    def test_ab_block_tuples(self):
        assert_equal(self.ab.block_tuples(self.A.ix[1], self.B.ix[2], l_block_attr_1,
                                     r_block_attr_1), False)
        assert_equal(self.ab.block_tuples(self.A.ix[2], self.B.ix[2], l_block_attr_1,
                                     r_block_attr_1), True)


"""
    def test_ab_block_tables_multi_skd2(self):
        A = mg.read_csv_metadata('/p/sanjibkd/data1/anhaidgroup/anhaidgroup/magellan/magellan/datasets/example_datasets/books_big/msd_reduced_10K.csv')
        mg.set_key(A, 'id')
        B = mg.read_csv_metadata('/p/sanjibkd/data1/anhaidgroup/anhaidgroup/magellan/magellan/datasets/example_datasets/books_big/msd_reduced_50K.csv')
        mg.set_key(B, 'id')
        #t0 = time.time()
        C = self.ab.block_tables(A, B, 'year', 'year', ['title', 'year'],
			['title', 'year'], l_output_prefix, r_output_prefix, n_jobs=-1)
        #t1 = time.time()
        #print "Blocking time: ", (t1 - t0)

    def test_ab_block_candset_multi_skd(self):
        A = mg.read_csv_metadata('/p/sanjibkd/data1/anhaidgroup/magellan/magellan/datasets/example_datasets/bikes/A.csv')
        mg.set_key(A, 'id')
        B = mg.read_csv_metadata('/p/sanjibkd/data1/anhaidgroup/magellan/magellan/datasets/example_datasets/bikes/B.csv')
        mg.set_key(B, 'id')
        l_output_attrs = ['bike_name', 'city_posted', 'km_driven', 'price',
                          'color', 'model_year']
        r_output_attrs = ['bike_name', 'city_posted', 'km_driven', 'price',
                          'color', 'model_year']
        C = self.ab.block_tables(A, B, 'city_posted', 'city_posted',
                                 l_output_attrs, r_output_attrs, verbose=False)
        l_block_attr = 'model_year'
        r_block_attr = 'model_year'
        self.ab.block_candset(C, l_block_attr, r_block_attr,
                              verbose=False, show_progress=False, n_jobs=2)
"""
