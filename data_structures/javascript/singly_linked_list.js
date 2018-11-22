// User defined Node class
class Node {
  // Creating the constructor
  constructor(element) {
    this.element = element;
    this.next = null;
  }
}

// Implementing a Linked List in JavaScript
class LinkedList {
  // Constructor for singly linked list
  constructor() {
    this.head = null;
    this.size = 0;
  }
  /**
   * TODO: add the following function(s)
   * removeElement(element)
   */

  // Adds a node at the end of a linked list
  add(element) {
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
  insertAt(element, index) {
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
      if (index == 0) {
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
  removeFrom(index) {
    // Making sure index is a valid amount
    if (index > 0 && index > this.size) {
      return -1;
    } else {
      var curr, prev, i = 0;
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
  
  /** 
   * TODO: add the following helper function(s)
   * isEmpty
   * size_Of_List
   * PrintList
   */
}
