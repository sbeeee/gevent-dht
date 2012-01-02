import uidlib, math

class FingerTable():
    def __init__(self, self_node, min_count=1):
        self.known = set([])
        self.self = self_node
        self.table = []
        self.min_count = min_count
        self.max_level = self._uid_2_level(long(32*'f', 16))+1
        for i in range(self.max_level):
            self.table.append(set([]))
        
    def _uid_2_level(self, uid):
        """
        Convert a uid to a log level in the finger table
        """
        level = int(math.log(uidlib.distance(uid, self.self.uid)))
        return level
        
    def _level_check(self, level):
        """
        Make sure the level is inside the table range.
        """
        if level > len(self.table) - 1:
            for i in range(len(self.table)-1, level):
                self.table.append(set([]))
                
    def add(self, Node):
        """
        Add a node to our finger table
        """
        self.known.add(Node)
        level = self._uid_2_level(Node.uid)
        self._level_check(level)
        self.table[level].add(Node)
        
    def remove(self, Node):
        """
        remove a node from our finger table
        """
        if Node not in self.known:
            return
        self.known.remove(Node)
        level = self._uid_2_level(Node.uid)
        self.table[level].remove(Node)
        
    def get_levels(self):
        """
        return what distances we would like to get uids for
        """
        for i in range(len(self.table)):
            if len(self.table[i]) < self.min_count:
                yield i
        
import unittest, node
Node = node.Node
class fingertest(unittest.TestCase):
    def testadds(self):
    
        finger = FingerTable(Node(uidlib.new_uid(), '', '', ''))
        Nodes = set([])
        
        for i in range(100):
            a = uidlib.new_uid()
            b = Node(a, '', '', '')
            Nodes.add(b)
            finger.add(b)
            
        for y in finger.get_levels():
            pass
            
        for x in Nodes:
            finger.remove(x)
            
        self.assertTrue(len(finger.known) == 0)
            
            
            
if __name__ == "__main__":
    unittest.main()


