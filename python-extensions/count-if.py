#!/usr/bin/env python

import gdb
import sys

class CountIf(gdb.Command):
    """

    """

    def __init__(self):
        super(CountIf, self).__init__("count-if",
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

        cnt = 0

        for i in range(int(arr_size)):
            expr = expr_template.replace("#", str(i))
            value = gdb.parse_and_eval(expr)
            if str(value) == search_value:
                cnt += 1
            sys.stdout.write("Found {}; Viewed {}\r".format(cnt, i))
            sys.stdout.flush()
CountIf()