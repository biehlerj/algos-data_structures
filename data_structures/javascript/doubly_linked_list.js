// Defining what a node of a doubly linked list contains
class Node {
  constructor (element) {
    this.element = element;
    this.prev = null;
    this.next = null;
  }
}

// Defining a doubly linked list and its methods
class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  // Method to add a node to the end of doubly linked list
  addAtEnd(element) {
    var node = new Node(element);

    var current;

    if (this.head == null) {
      this.head = node;
    } else {
      current = this.head;

      while (current.next) {
        current = current.next;
      }
      current.next = node;
      node.prev = current;
    }
    this.size++;
  }

  // Method to add a node at the beginning of the list
  addAtBeginning(element) {
    var node = new Node(element);
    var current;

    if (this.head == null) {
      this.head = node;
    } else {
      current = this.head;
      node.next = current;
      current.prev = node;
    }
    this.size++;
  }

  // Method to add a node at a given index
  insertAt(element, index) {
    if (index > 0 && index > this.size) {
      return false;
    } else {
      var node = new Node(element);
      var current, prev;

      current = this.head;
      if (index === 0) {
        node.next = current;
        this.head = node;
      } else {
        var i = 0;

        while (i < index) {
          prev = current;
          current = current.next;
          i++;
        }
        node.next = current;
        node.prev = prev;
        prev.next = node;
        current.prev = node;
      }
      this.size++;
    }
  }

  /**
   * @TODO: Complete the following functions
   * removeFrom (index)
   * removeElement (element)
   */

  // Helper Functions
  /**
   * @TODO: Complete the following helper functions
   * indexOf (element)
   * isEmpty ()
   * sizeOfList()
   * printList ()
   */
}