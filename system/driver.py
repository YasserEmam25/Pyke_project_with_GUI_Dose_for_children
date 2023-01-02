# driver.py
import os

import sys

from pyke import knowledge_engine
from pyke import krb_traceback

from GUI import *

engine = knowledge_engine.engine(__file__)


def test_questions():
    gui_main_page()

    engine.reset()

    try:
        engine.activate('simple_rules')
        with engine.prove_goal('simple_rules.output($age,$weight,$con,$time,$analysis,$type,$method)') \
                as gen:
            sys.stdin = open('input.txt')

            for vars, plan in gen:
                first = vars['analysis']
                second = vars['type']
                third = vars['method']
                forth = ((vars['age'] * vars['weight']) / vars['con'])
                fifth = (vars['time'])
                tkinter_gui_out(first, second, third, forth, fifth)
                print("\nAnalysis method: " + vars['analysis'])
                print("Solution Type: " + vars['type'])
                print("Method of Administration: " + vars['method'])
                print("\nYou should give: %s" % ((vars['age'] * vars['weight']) / vars['con']) + " mg/", (vars['time']),
                      "hrs")
    except:
        krb_traceback.print_exc()
        sys.exit(1)

    with open("input.txt", 'r+') as file:
        file.truncate()
