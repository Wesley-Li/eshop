'''
Created on 2014年7月3日

@author: Arc
'''
from xml.dom.minidom import Document

doc = Document()

def addleafnode(parnode, childname, childvalue):
        
        """
            Add leaf node
        """

        node = doc.createElement(childname)
        parnode.appendChild(node)
        textnode = doc.createTextNode(childvalue)
        node.appendChild(textnode)