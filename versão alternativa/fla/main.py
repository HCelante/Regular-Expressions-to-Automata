#!/usr/bin/python
# -*- coding: utf-8 -*-

from dfa.dfa import DeterministicFiniteAutomaton
from dfa.transition import Transition as DFATransition 

from ndfa.ndfa import NonDeterministicFiniteAutomaton
from ndfa.transition import Transition as NDFATransition 



import sys
import logging

def dfa(lines, cmdline_args):
    input_alphabet    = lines[0].split()
    states            = lines[2].split()
    initial_state     = lines[3]
    acceptance_states = lines[4].split()
    transitions = []
    for description in lines[5:]:
        splited_description = description.split()
        transition = DFATransition(splited_description[0], splited_description[1], splited_description[2])
        transitions.append(transition)
    dfa = DeterministicFiniteAutomaton(states, initial_state, acceptance_states, transitions)
    initial_configuration = dfa.get_initial_configuration(cmdline_args[0])
    dfa.load_configuration(initial_configuration)
    result = dfa.run()
    if dfa.get_decision() == True:
        print("Aceitou")
    else:
        print("Rejeitou")

def ndfa(lines, cmdline_args):
    input_alphabet    = lines[0].split()
    whitespace        = lines[1]
    states            = lines[2].split()
    initial_states    = lines[3].split()
    acceptance_states = lines[4].split()
    transitions = []
    for description in lines[5:]:
        splited_description = description.split()
        if splited_description[1] == whitespace:
            splited_description[1] = None
        transition = NDFATransition(splited_description[0], splited_description[1], splited_description[2])
        transitions.append(transition)
    ndfa = NonDeterministicFiniteAutomaton(states, initial_states, acceptance_states, transitions)
    initial_configurations = ndfa.get_initial_configurations(cmdline_args[0])
    ndfa.load_configurations(initial_configurations)
    result = ndfa.run()
    if ndfa.get_decision() == True:
        print("Aceitou")
    else:
        print("Rejeitou")


if __name__ == "__main__":
    #logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    fp = open(sys.argv[1], "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
    lines_cmd = fp.readlines()
    lines = []
    for line in lines_cmd:
        lines.append(line.rstrip())
    automaton_type = lines[0]
    lines = lines[1:]

    if automaton_type == "DFA":
        dfa(lines, sys.argv[2:])
    elif automaton_type == "NDFA":
        ndfa(lines, sys.argv[2:])

