class Node {
    head = null
    tail = null
    next = null
    prev = null 

    buildNode(dict) {
        for (const [key, value] of Object.entries(dict)) {
           this[key] = value; 
        }
    }
    insertBeginning() {
        if (Node.head == null) {
            Node.head = this
            Node.tail = this
        } else {
            this.next = Node.head
            this.prev = null
            Node.head.prev = this
            Node.head = this
        }
    }
}