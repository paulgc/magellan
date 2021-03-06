"""
This module contains labeling related routines for a single table.
"""
import logging

import pandas as pd
import six

import magellan.catalog.catalog_manager as cm
import magellan.utils.catalog_helper as ch

logger = logging.getLogger(__name__)


def label_table(table, label_column_name, verbose=False):
    """
    Label a pandas DataFrame (for supervised learning purposes).

    This functions labels a DataFrame, typically used for supervised learning
    purposes. This function expects the input DataFrame containing the metadata
    of a candidate set (such as key, fk_ltable, fk_rtable, ltable, rtable).
    This function creates a copy of the input DataFrame, adds label column
    at the end of the DataFrame, fills the column values with 0, invokes a
    GUI for the user to enter labels (0/1, 0:non-match, 1:match) and finally
    returns the labeled DataFrame. Further, this function also copies the
    properties from the input DataFrame to the output DataFrame.

    Args:
        table (DataFrame): Input DataFrame to be labeled. Specifically,
            a DataFrame containing the metadata of a candidate set (such as
            key, fk_ltable, fk_rtable, ltable, rtable) in the catalog.
        label_column_name (string): Column name to be given for the labels
            entered by the user.
        verbose (boolean): Flag to indicate whether more detailed information
            about the execution steps should be printed out (default value is
            False).

    Returns:
        A new ataFrame with the labels entered by the user. Further,
        this function sets the output DataFrame's properties same as input
        DataFrame.

    Raises:
        AssertionError: If the input table is not of type pandas DataFrame.
        AssertionError: If the input column name is not of type string.
        AssertionError: If the label column name is already present in the
            input table.

    """
    # Validate the input parameters: check input types, check the metadata
    # for the input DataFrame as it will get copied to the labeled DataFrame
    _validate_inputs(table, label_column_name, verbose)

    # Initialize the table to be labeled: create a copy and set the column
    # values to be 0s
    labeled_table = _init_label_table(table, label_column_name)

    # Invoke the GUI
    from magellan.gui.table_gui import edit_table
    edit_table(labeled_table)

    # Post process the labeled table: validate whether the labels contain
    # only 0/1s, copy the properties (in the catalog) of the input table to the
    # labeled table
    labeled_table = _post_process_labelled_table(table, labeled_table,
                                                 label_column_name)
    # Return the labeled table
    return labeled_table


def _validate_inputs(table, label_column_name, verbose):
    """
    This function validates the inputs for the label_table function
    """
    # Validate the input parameters

    # # The input table table is expected to be of type pandas DataFrame
    if not isinstance(table, pd.DataFrame):
        logger.error('Input object is not of type data frame')
        raise AssertionError('Input object is not of type data frame')

    # # The label column name is expected to be of type string
    if not isinstance(label_column_name, six.string_types):
        logger.error('Input attr. is not of type string')
        raise AssertionError('Input attr. is not of type string')

    # # Check if the label column name is already present in the input table
    if ch.check_attrs_present(table, label_column_name):
        logger.error('The label column name (%s) is already present in the '
                     'input table', label_column_name)
        raise AssertionError('The label column name (%s) is already present '
                             'in the input table', label_column_name)

    # Now, validate the metadata for the input DataFrame as we have to copy
    # these properties to the output DataFrame

    # # First, display what metadata is required for this function
    ch.log_info(logger, 'Required metadata: cand.set key, fk ltable, '
                        'fk rtable, ltable, rtable, ltable key, rtable key',
                verbose)

    # # Second, get the metadata
    key, fk_ltable, fk_rtable, ltable, rtable, l_key, r_key = \
        cm.get_metadata_for_candset(table, logger, verbose)

    # # Third, validate the metadata
    cm.validate_metadata_for_candset(table, key, fk_ltable, fk_rtable,
                                     ltable, rtable, l_key, r_key,
                                     logger, verbose)

    # Return True if everything was successful
    return True


def _init_label_table(table, label_column_name):
    """
    This function initializes inputs required for label_table function.
    Specifically, this function makes a copy of the input table and
    initializes the column values to 0s.
    """
    # Create a copy of the input table
    labeled_table = table.copy()

    # Add the label column at the end and initialize to 0s (non-match)
    labeled_table[label_column_name] = 0

    # Return the label table
    return labeled_table


def _post_process_labelled_table(input_table, labeled_table, col_name):
    """
    This function post processes the labeled table and updates the catalog.
    Specifically, this function validates that the label column contain only
    0 and 1's, and finally copies the properties from the input table to the
    output table.
    """
    # Cast the label values to int as initially they will be strings when it
    # comes from the GUI
    labeled_table[col_name] = labeled_table[col_name].astype(int)

    # Check if the table contains only 0s and 1s
    label_value_with_1 = labeled_table[col_name] == 1
    label_value_with_0 = labeled_table[col_name] == 0
    sum_of_labels = sum(label_value_with_1 | label_value_with_0)

    # If they contain column values other than 0 and 1, raise an error
    if not sum_of_labels == len(labeled_table):
        logger.error('The label column contains values other than 0 and 1')
        raise AssertionError(
            'The label column contains values other than 0 and 1')

    # Copy the properties from the input table to label table.
    # Note: Here we dont have to check for the integrity of 'key' because the
    # key column is not tampered from the input table.
    cm.init_properties(labeled_table)
    cm.copy_properties(input_table, labeled_table)

    # Return the label table
    return labeled_table
