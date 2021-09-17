from collections.abc import Sequence


# utils to work with nested collections
def recursive_iter(seq):
    ''' Iterate over elements in seq recursively (returns only non-sequences)
    '''
    if isinstance(seq, Sequence):
        for e in seq:
            for v in recursive_iter(e):
                yield v
    else:
        yield seq


def flatten(seq):
    ''' Flatten all nested sequences, returned type is type of ``seq``
    '''
    return list(recursive_iter(seq))


def copy_structure(data, shape):
    ''' Put data from ``data`` into nested containers like in ``shape``.
        This can be seen as "unflatten" operation, i.e.:
            seq == copy_structure(flatten(seq), seq)
    '''
    d_it = recursive_iter(data)

    def copy_level(s):
        if isinstance(s, Sequence):
            return type(s)(copy_level(ss) for ss in s)
        else:
            return next(d_it)
    return copy_level(shape)


def convert_naslib_to_op_indices():
    pass

def convert_op_indices_to_naslib(op_indices, naslib):
    pass
