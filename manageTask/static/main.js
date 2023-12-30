var next_node = null
var prev_node = null
// building Linked lists
for (let i = 0; i < listEmployees.length; i++) {
    const node = new Node()
    node.buildNode(listEmployees[i])
    node.insertBeginning()
}
// function to create element with the node passed
function createElement(value) {
    const p = document.createElement('p')
    p.innerHTML = value
    const employee = document.querySelector('#employee');
    employee.appendChild(p)
}
// adding node on page load
window.addEventListener('load', function() {
    document.querySelector('#prev').style.display = 'none'
    createElement(Node.head['user_name'])
    createElement(Node.head['salary'])
    next_node = Node.head.next
    prev_node = Node.head.prev
})
// selecting next node
const next = document.querySelector('#next')
next.onclick = () => {
    document.querySelector('#prev').style.display = 'inline-block'
    document.querySelector('#employee').innerHTML="";
    createElement(next_node['user_name'])
    createElement(next_node['salary'])
    prev_node = next_node.prev;
    next_node = next_node.next;
    if (next_node == null) {
        document.querySelector('#next').style.display = 'none'
    }
}
// selecting previous node
const prev = document.querySelector('#prev')
prev.onclick = () => {
    document.querySelector('#employee').innerHTML="";
    createElement(prev_node['user_name'])
    createElement(prev_node['salary'])
    next_node = prev_node.next
    prev_node = prev_node.prev;
    if (prev_node == null) {
        document.querySelector('#prev').style.display = 'none'
    }
    if (next_node != null) {
        document.querySelector('#next').style.display = 'inline-block'
    }
}