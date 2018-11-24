// User defined Node class
class Node {
  // Creating the constructor
  constructor (element) {
    this.element = element;
    this.next = null;
  }
}

// Implementing a Linked List in JavaScript
class LinkedList {
  // Constructor for singly linked list
  constructor () {
    this.head = null;
    this.size = 0;
  }

  // Adds a node at the end of a linked list
  add (element) {
    // Create a new node
    var node = new Node(element);

    // Store the current node
    var current;

    // Check if the list is empty, if it is add the element as the head
    if (this.head == null) {
      this.head = node;
    } else {
      current = this.head;

      // Iterate to the end of the list
      while (current.next) {
        current = current.next;
      }

      // Add the node
      current.next = node;
    }
    this.size++;
  }

  // Inserting a node at a given index
  insertAt (element, index) {
    if (index > 0 && index > this.size) {
      return false;
    } else {
      // Create the new node
      var node = new Node(element);

      // Creating variables to track the current node and the previous node
      var curr, prev;

      // Setting the current node to the head node
      curr = this.head;

      // Add the element to the beginning of the list if index is 0
      if (index === 0) {
        node.next = curr;
        this.head = node;
      } else {
        var i = 0;

        // Iterate over the list until we reach the index where we want to insert
        while (i < index) {
          prev = curr;
          curr = curr.next;
          i++;
        }

        // Add the element at the given index
        node.next = curr;
        prev.next = node;
      }
      this.size++;
    }
  }

  // Removes a node from a linked list at a given index
  removeFrom (index) {
    // Making sure index is a valid amount
    if (index > 0 && index > this.size) {
      return -1;
    } else {
      var curr; var prev; var i = 0;
      curr = this.head;
      prev = curr;

      // If index is the first item delete it
      if (index === 0) {
        this.head = curr.next;
      } else {
        // Iterate over the list to the index position
        while (i < index) {
          prev = curr;
          curr = curr.next;
          i++;
        }
        // Remove the element
        prev.next = curr.next;
      }
      this.size--;

      // Return the removed element
      return curr.element;
    }
  }

  // Removing a given element
  removeElement (element) {
    var current = this.head;
    var prev = null;

    // Iterate over the list until the given element is found
    while (current != null) {
      if (current.element === element) {
        if (prev === null) {
          this.head = current.next;
        } else {
          prev.next = current.next;
        }
        this.size--;
        return current.element;
      }
      prev = current;
      current = current.next;
    }
    return -1;
  }

  // Helper functions

  // Finding the index of a given element
  indexOf (element) {
    var current = this.head;
    var count = 0;

    while (current != null) {
      if (current.element === element) {
        return count;
      }
      count++;
      current = current.next;
    }
    return -1;
  }

  // Checking if a linked list is empty
  isEmpty () {
    return this.size === 0;
  }

  sizeOfList () {
    console.log(this.size);
  }

  // Printing the list
  printList () {
    var curr = this.head;
    var str = '';

    while (curr) {
      str += curr.element + ' ';
      curr = curr.next;
    }
    console.log(str);
  }
}

// creating an object for the
// Linked list class
var ll = new LinkedList();

// testing isEmpty on an empty list
// returns true
console.log(ll.isEmpty());

// adding element to the list
ll.add(10);

// prints 10
ll.printList();

// returns 1
console.log(ll.sizeOfList());

// adding more elements to the list
ll.add(20);
ll.add(30);
ll.add(40);
ll.add(50);

// returns 10 20 30 40 50
ll.printList();

// prints 50 from the list
console.log('is element removed ?' + ll.removeElement(50));

// prints 10 20 30 40
ll.printList();

// returns 3
console.log('Index of 40 ' + ll.indexOf(40));

// insert 60 at second positon
// ll contains 10 20 60 30 40
ll.insertAt(60, 2);

ll.printList();

// returns false
console.log('is List Empty ? ' + ll.isEmpty());

// remove 3rd element from the list
console.log(ll.removeFrom(3));

// prints 10 20 60 40
ll.printList();
