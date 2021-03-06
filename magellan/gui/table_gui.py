import logging
# from builtins import str
from PyQt4 import QtGui
import six

import magellan as mg
from magellan.utils.generic_helper import remove_non_ascii

logger = logging.getLogger(__name__)


def view_table(table, edit_flag=False, show_flag=True):
    datatable = QtGui.QTableWidget()

    # disable edit
    if edit_flag == False:
        datatable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

    datatable.setRowCount(len(table.index))
    datatable.setColumnCount(len(table.columns))

    # set data
    for i in range(len(table.index)):
        for j in range(len(table.columns)):
            datatable.setItem(i, j, QtGui.QTableWidgetItem(str(table.iat[i, j])))

    list_col = list(table.columns.values)
    datatable.setHorizontalHeaderLabels(list_col)

    # set window size
    width = min((j + 1) * 105, mg._viewapp.desktop().screenGeometry().width() - 50)
    height = min((i + 1) * 41, mg._viewapp.desktop().screenGeometry().width() - 100)
    datatable.resize(width, height)

    # set window title
    datatable.setWindowTitle("Dataframe")

    if show_flag:
        # show window
        datatable.show()
        mg._viewapp.exec_()


    if edit_flag:
        return datatable



# edit table
def edit_table(table, show_flag=True):
    datatable = view_table(table, edit_flag=True, show_flag=show_flag)
    cols = list(table.columns)
    idxv = list(table.index)
    for i in range(len(table.index)):
        for j in range(len(table.columns)):
            val = datatable.item(i, j).text()
            inp = table.iat[i, j]
            val = _cast_val(val, inp)
            table.set_value(idxv[i], cols[j], val)

# need to cast string values from edit window
def _cast_val(v, i):
    if v == "None":
        return None
    elif isinstance(i, bool):
        return bool(v)
    elif isinstance(i, float):
        return float(v)
    elif isinstance(i, int):
        return int(v)
    elif isinstance(i, six.string_types):
        v = remove_non_ascii(str(v))
        return str(v)
    elif isinstance(i, object):
        return v
    else:
        logger.warning('Input value did not match any of the known types')
        return v
