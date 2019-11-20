import sys

class State(object):
    def __init__(self, state_name):
        self.state_name = state_name
        self.final = False


class Transition(object):
    def __init__(self, current_state, next_state, symbol):
        self.current_state = current_state
        self.next_state = next_state
        self.symbol = symbol


class Automaton(object):
    def __init__(self):
        input = open(sys.argv[1], 'r')
        input.readline()

        temp = input.readline().replace(",", " ").replace("{", "").replace("}","").split()
        self.states = []

        for name in temp:
            self.states.append(State(name))

        temp = input.readline().replace(",", " ").replace("{", "").replace("}", "").split()
        self.alphabet = []
        for symbol in temp:
            self.alphabet.append(symbol)

        input.readline()
        temp = input.readline()
        self.transitions = []
        while temp[0] == '(':
            temp = temp.replace(",", " ").replace("(", "").replace(")", "").replace("->", " ").split()
            source = State(temp[0])
            target = State(temp[2])

            for state in self.states:
                if state.state_name == source.state_name:
                    source = state
                if state.state_name == target.state_name:
                    target = state
            self.transitions.append(Transition(source, target, temp[1]))
            temp = input.readline()

        temp = input.readline().replace(",", "")
        self.initial = self.states[0]
        for state in self.states:
            if temp == state.state_name + '\n': # \n because of txt
                self.initial = state

        temp = input.readline().replace(",", " ").replace("{", "").replace("}", "").split()
        for temp_state in temp:
            for state in self.states:
                if temp_state == state.state_name:
                    state.final = True
                    
        input.close()


    def min_automaton(self):
        peers = []
        for s1 in range(len(self.states)):
            for s2 in range(len(self.states)-s1-1):
                # peers.append(Peer(self.states[s1], self.states[s1 + s2 + 1]))
                peers.append(Peer(self.states[s1], self.states[s1+s2+1]))

        for peer in peers:
            if peer.state1.final != peer.state2.final:
                peer.dij = False
                peer.reason = "final/ no final"

        for peer in peers:
            if peer.dij:
                list_t1 = self.transitions_of_state(peer.state1)
                list_t2 = self.transitions_of_state(peer.state2)
                for t1 in list_t1:
                    for t2 in list_t2:
                        if t1.symbol == t2.symbol and peer.dij:
                            next_peer = peer
                            for peer2 in peers:
                                if ((t1.next_state == peer2.state1 and t2.next_state == peer2.state2) or
                                   (t2.next_state == peer2.state1 and t1.next_state == peer2.state2)):
                                   next_peer = peer2

                            if not next_peer.dij:
                                peer.non_dij(t1.symbol + next_peer.to_string())
                            elif next_peer != peer:
                                next_peer.sij.append(peer)

        #self.write_table(peers)
        self.update_afd(peers)
        self.write_min_afd(peers)



    def transitions_of_state(self, state):
        transitions_list = []

        for transition in self.transitions:
            if transition.current_state == state:
                transitions_list.append(transition)
        return transitions_list


    def update_afd(self, table_list):
        for peer in table_list:
            if peer.dij:
                self.mix_two_states(peer.state1, peer.state2, table_list)



    def mix_two_states(self, state1, state2, table_list):
        # state1.state_name += state2.state_name

        for peer in table_list:
            if peer.state1 == state2:
                peer.state1 = state1
            if peer.state2 == state2:
                peer.state2 == state2

        for p1 in range(len(table_list)):
            p2 = p1+1
            while (p2 < len(table_list)):
                if(table_list[p1].state1 == table_list[p2].state1 and
                   table_list[p1].state2 == table_list[p2].state2):
                   del table_list[p2]
                p2 += 1

        for transition in self.transitions:
            if transition.current_state == state2:
                transition.current_state = state1
            if transition.next_state == state2:
                transition.next_state = state1

        if self.initial == state2:
            self.initial = state1

        for t1 in range(len(self.transitions)):
            t2 = t1+1
            while(t2 < len(self.transitions)):
                if(self.transitions[t1].current_state == self.transitions[t2].current_state and
                   self.transitions[t1].next_state == self.transitions[t2].next_state and
                   self.transitions[t1].symbol == self.transitions[t2].symbol):
                   del self.transitions[t2]

                t2 += 1
        
        i = 0
        while i < len(self.states):
            if self.states[i] == state2:
                del self.states[i]
            i += 1


    def write_table(self, table_list):
        out_table = open(sys.argv[2], 'w+')
        out_table.write("INDEX\t\tD[i,j]=\t\t\tS[i,j]=\t\t\tREASON")
        for line in table_list:
            out_table.write("\n[" + str(line.state1.state_name).replace("q", "") + "," + str(line.state2.state_name).replace("q", "") + "]")
            if line.dij:
                out_table.write("\t\t0")
            else:
                out_table.write("\t\t1")
            dependences = "{ "
            if len(line.sij) > 0:
                dependences += line.sij[0].to_string()
            for s in line.sij:
                if line.sij[0] != s:
                    dependences += ","
                    dependences += s.to_string()
            dependences += " }"
            out_table.write("\t\t\t" + dependences)
            out_table.write("\t\t\t\t" + line.reason)
        out_table.close()


    def write_min_afd(self, table_list):

        # min_afd = open(sys.argv[3], 'w+')
        min_afd = open(sys.argv[2], 'w+')
        min_afd.write("DFA\n")
        min_afd.write(' '.join(self.alphabet)+ "\n")
        min_afd.write("E\n")
        min_afd.write(''.join(self.states[0].state_name)+' ')
        for i in range(1, len(self.states)):
            if self.states[i].state_name != 'qTrap':
                min_afd.write(''.join(self.states[i].state_name)+' ')
        
        min_afd.write("\n" + self.initial.state_name +'\n')
        for state in self.states:
            if state.final:
                min_afd.write(state.state_name+' ')

        for transition in self.transitions:
            if transition.next_state.state_name != 'qTrap' and transition.current_state.state_name != 'qTrap':
                min_afd.write("\n" + transition.current_state.state_name + " " + transition.symbol + " " + transition.next_state.state_name)
       
        min_afd.close()


    def is_complete(self):
        for state in self.states:
            transition = self.transitions_of_state(state)
            if len(transition) != len(self.alphabet):
                return False
        return True

    def make_complete(self):
        if not self.is_complete():
            qTrap = State("qTrap")
            self.states.append(qTrap)

            for state in self.states:
                transiitons = self.transitions_of_state(state)
                symbols_of_transition = []
                for transiiton in transiitons:
                    symbols_of_transition.append(transiiton.symbol)

                for symbol in self.alphabet:
                    if not symbols_of_transition.__contains__(symbol):
                        self.transitions.append(Transition(state, qTrap, symbol))



class Peer:
    def __init__(self, state1, state2):
        self.state1 = state1
        self.state2 = state2
        self.dij = True
        self.sij = []
        self.reason = ""


    def non_dij(self, reason):
        self.dij = False
        self.reason = reason
        for s in self.sij:
            if s.dij:
                s.non_dij(("prop[" + self.state1.state_name.replace("q", "") + "," + self.state2.state_name.replace("q", "") + "]"))
    
    def to_string(self):
        str = "[" + self.state1.state_name.replace("q", "") + "," + self.state2.state_name.replace("q", "") + "]"
        return str



if __name__ == "__main__":
    a = Automaton()
    if not a.is_complete():
        a.make_complete()
    
    a.min_automaton()
