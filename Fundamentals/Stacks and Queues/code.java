public static class Queue {
	private static class Node {
	private int data:
	private Node next;
	private Node (int data) {
		this.data = data;
	}
}

private Node head;
private Node tail;

public Boolean isEmpty(){
	return head == null;
}

public int peek(){
	return head.data;
}

public void add(int data) {
	Node node = new node(data);
	if (tail != null) {
		tail.next = node;
	}
}

public int remove() {
	int data = head.data;
	head = head.next;
	if (head == null) {
		tail = null;
	}
	return data;
}