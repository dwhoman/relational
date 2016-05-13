from relational import relation
from relational import rtypes
import tabulate

class RelationOrg(relation.Relation):
    '''Glue class between Relation and Emacs Org. Can be initialized using
    a Relation object or a list of lists with the first list being the
    column names. Emacs Org passes in tables as lists of lists when
    evaluating code with the :var header argument, where :var is the
    table name. The first Org table row must be column names and not
    be separated by a horizontal line.

    #+NAME:person
    | name |  dob | 
    |  Bob | 1950 |

    The __str__ method will return an Org table.
    '''
    def __init__(self, org_table):
        if isinstance(org_table, relation.Relation):
            self.header = org_table.header
            self.content = org_table.content
            self._readonly = org_table._readonly
        else:
            self._readonly = False
            self.header = relation.Header(org_table[0])
            self.content = {tuple(map(rtypes.Rstring,x)) for x in org_table[1::]}

    def __str__(self):
        return tabulate.tabulate(self.content, self.header, tablefmt = "orgtbl")
