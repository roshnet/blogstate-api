# Definitions for functions dedicated for frequent database operations

from database import cur


def exists(tbl_name, **kwargs):
    """
    Checks if the given key-value pairs exist in the specified table.
    
    Returns 1 if all pairs exist in the specified table, 0 otherwise.
    """

    if not 'tablename' in kwargs.keys():
        col_names = '`,`'.join([x for x in list(kwargs.keys())])
    else:
        raise KeyError('tbl_name to be specified directly as the \
                        first argument, not as a keyword argument.')

    col_string = "`"
    col_string += col_names
    col_string += "`"

    q = """SELECT {} FROM `{}` ORDER BY `user_id`;""".format(col_string, tbl_name)
    cur.execute(q)
    res = cur.fetchall()
    if len(res) > 0:
        return 1
    return 0
