#-------------------------------------------------------------------------------
# Name:        table.py
# Version:     0.25
#
# Purpose:     Input an iterable of data and output it as a formatted table.
#
# Author:      Ken Tong
#
# Created:     31/07/2015
# Updated:     10/08/2015
#-------------------------------------------------------------------------------

class Table(object):
    """
    Class Table creates an object which formats input data and optional headers.
    """
    def __init__(self, data, header=None, alignment=None):
        """
        Initialize a Table object.

        Arguments:
        data: An input iterable of data.

        header: A tuple or list specifying the headers for the data. If header
                is in the data iterable, 'firstrow' must be specified.

        alignment: Alignment of the column. Specify left (default), right or centre.
                    You can also using the first letter (l, r, or c) to specify
                    alignment.

        Returns:
        results: A tuple with formatted spacing and an underline for the headers.
                The results tuple is the header at position 0 and the underline
                at position 1.
        """
        self.alignment = alignment
        self.data = data
        self.header = header
        self._index = 0
        self.results = self.table(self.data, self.header, self.alignment)

    def _get_column_widths(self, data, header):
        """
        Get the length of each column for a value of an item in the input iterable.

        Arguments:
        data: An input iterable of data.

        header: A tuple or list specifying the headers for the data. If header
                is in the data iterable, 'firstrow' must be specified.

        Returns:
        column_width_dict: Dictionary of the position of a column as they key
                             and the length of the column as the value.
        """
        padding = 2
        column_width_dict = {}
        if not header is None:
            if isinstance(data, tuple):
                data = (header,) + data
            if isinstance(data, list):
                data = [header] + data
        for row in data:
            for idx, val in enumerate(row):
                if len(column_width_dict) < len(row):
                    column_width_dict[idx] = len(val) + padding
                else:
                    if len(str(val)) > column_width_dict[idx]:
                        column_width_dict[idx] = len(val) + padding
        return column_width_dict

    def _get_alignment(self, alignment):
        """
        Function returns alightment character for the output.

        Arguments:
        alignment: the alignment for the table

        Returns:
        alignment_char: the alignment character
        """
        if alignment is None:
            return '<'

        else:
            alignment_char_dict = {
                'c': '^',
                'center': '^',
                'centre': '^',
                'l': '<',
                'left': '<',
                'r': '>',
                'right': '>'
            }
            return alignment_char_dict.get(alignment.lower(), '<')

    def table(self, data, header, alignment):
        """
        Output an iterable of data as a table.

        Arguments:
        data: An input iterable of data.

        header: A tuple or list specifying the headers for the data. If header
                is in the data iterable, 'firstrow' must be specified.

        alignment: Alignment of the column. Specify left (default), right or centre.
                    You can also using the first letter (l, r, or c) to specify
                    alignment.

        Returns:
        results: A tuple with formatted spacing and an underline for the headers.
                The results tuple is the header at position 0 and the underline
                at position 1.
        """
        try:
            if isinstance(data, (list, tuple)):
                column_width_dict = self._get_column_widths(data, header)

                # Create the format string based on the data and length of each column.
                # The first row in the data is used to determine the number of columns.
                output_list = []
                for i in range(0, len(data[0])):
                    output_list.append('{' + str(i) + ':' + self._get_alignment(self.alignment) +
                        str(column_width_dict[i]) + '}')
                output = ' '.join(output_list)

                # Create the dashed underline that goes under each column.
                underline = []
                for key, val in column_width_dict.iteritems():
                    underline.append('-' * val)

                # Output the table. Use the tuple specified with the header parameter if
                # avaiable. If 'header = firstrow' is specified, the first row of
                # the data iterable contains the header. If header is no specified
                # or 'header = None'assume the assume there is no header in the
                # data iterable.
                output_return = []
                if not header is None:
                    try:
                        if isinstance(header, (list, tuple)):
                                output_return.append(output.format(*header))
                                output_return.append(output.format(*underline))
                                for row in data:
                                    output_return.append(output.format(*row))
                                return tuple(output_return)
                        elif isinstance(header, str) and header.lower() == 'firstrow':
                            for idx, item in enumerate(data):
                                if idx == 1:
                                    output_return.append(output.format(*underline))
                                output_return.append(output.format(*item))
                            return tuple(output_return)
                        elif isinstance(header, str) and header.lower() != 'firstrow':
                            print 'Error: Header input is {0}. Needs to be a list, '\
                                'tuple, or \'firstrow\' must be specified for '\
                                'header argument.'.format(str(type(header))[1:-1])
                    except IndexError as e:
                        print 'Error: {0}. Number of data and header '\
                                  'columns do not match. There are {1} '\
                                  'columns in the header and {2} '\
                                  'columns in the input data.'\
                                  .format(str(e), str(len(header)), str(len(data)))
                    except TypeError as e:
                        print 'Error: Header input is {0}. Needs to be a list, '\
                            'tuple, or \'firstrow\' must be specified for '\
                            'header argument.'.format(str(type(header))[1:-1])
                else:
                    for idx, item in enumerate(data):
                        output_return.append(output.format(*item))
                    return tuple(output_return)
            else:
                print 'Error: Data input is {0}. Needs to be a list or tuple.'\
                      .format(str(type(data))[1:-1])
        except IndexError as e:
            print 'Error: {0}. There is an error with the data input.'\
                  .format(str(e))

    def __getitem__(self, index):
        """
        Get a formatted table item by index.
        """
        try:
            item = self.results[index]
            return item
        except IndexError as e:
            return 'Error: {0}.'.format(str(e))

    def __iter__(self):
        """
        Iterator to allow table to be looped over.
        """
        return self

    def next(self):
        # No double underscores for Python 2.x support.
        """
        Iterator to loop over formatted table.
        """
        try:
            item = self.results[self._index]
        except IndexError:
            self._index = 0
            raise StopIteration
        self._index += 1
        return item

    def __str__(self):
        """
        String function to allow printing of table.
        """
        try:
            rtn = ''.join([str(item) + '\n' for item in self.results])
            return rtn
        except TypeError as e:
            return 'Error: {0}. Cannot print results.'.format(str(e))