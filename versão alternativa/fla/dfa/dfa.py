#!/usr/bin/python
# -*- coding: utf-8 -*-

from instance import Instance
import logging


class DeterministicFiniteAutomaton:
    def __init__(self, states, initialState, acceptanceStates, transitions):
        self.states = states
        self.initialState = initialState
        self.acceptanceStates = acceptanceStates
        self.transitions = transitions
        self.currentConfiguration = None

    def restart(self):
        self.currentConfiguration = None

    def get_decision(self):
        if len(self.currentConfiguration.current_word) == 0:
            if self.currentConfiguration.current_state in self.acceptanceStates:
                return True
            else:
                return False
        return None

    def get_initial_configuration(self, word):
        return Instance(self, self.initialState, word)

    def load_configuration(self, configuration):
        self.currentConfiguration = configuration

    def step_forward(self):
        transition = self.currentConfiguration.get_valid_transition()
        if transition == None:
            if len(self.currentConfiguration.current_word) == 0 and self.currentConfiguration.current_state in self.acceptanceStates:
                self.currentConfiguration.acceptance_status = True
            else:
                self.currentConfiguration.acceptance_status = False
        else:
            self.currentConfiguration = self.currentConfiguration.apply_transition(
                transition)

    def run(self):
        logging.debug(self.currentConfiguration)
        pertinence_decision = self.get_decision()
        if pertinence_decision == True:
            return True
        while not self.currentConfiguration.is_final():
            self.step_forward()
            logging.debug(self.currentConfiguration)
        return self.get_decision()
