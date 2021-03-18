#!/usr/bin/env python

import gdb

class FilteredSearch(gdb.Command):
    """

    """

    def __init__(self):
        super(FilteredSearch, self).__init__("filtered-search",
                gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL)

    def invoke(self, argument, from_tty):
        args = gdb.string_to_argv(argument)
        if len(args) != 3:
            print "Argument required - expression, array size, value"
            return

        expr_template = args[0]
        arr_size = args[1]
        search_value = args[2]

        print expr_template, arr_size, search_value

        for i in range(int(arr_size)):
            expr = expr_template.replace("#", str(i))
            value = gdb.parse_and_eval(expr)
            if str(value) == search_value:
                print "Find value in %d element" % (i)

FilteredSearch()