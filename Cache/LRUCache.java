import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.locks.ReentrantLock;

public class LRUCache<K, V> implements Cache<K, V> {
    private class Node {
        K key;
        V value;
        Node prev;
        Node next;

        Node(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    private final int capacity;
    private final Map<K, Node> cache;
    private final ReentrantLock lock = new ReentrantLock();
    private Node head;
    private Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>(capacity);
        head = new Node(null, null);
        tail = new Node(null, null);
        head.next = tail;
        tail.prev = head;
    }

    @Override
    public V get(K key) {
        lock.lock();
        try {
            Node node = cache.get(key);
            if (node == null) {
                return null;
            }
            // Move the accessed node to the front of the list
            moveToHead(node);
            return node.value;
        } finally {
            lock.unlock();
        }
    }

    @Override
    public void put(K key, V value) {
        lock.lock();
        try {
            Node node = cache.get(key);
            if (node != null) {
                // Update the value of an existing node
                node.value = value;
                // Move the node to the front of the list
                moveToHead(node);
            } else {
                if (cache.size() >= capacity) {
                    // Remove the least recently used node (tail)
                    cache.remove(tail.prev.key);
                    removeNode(tail.prev);
                }
                // Add a new node to the front of the list
                Node newNode = new Node(key, value);
                cache.put(key, newNode);
                addNode(newNode);
            }
        } finally {
            lock.unlock();
        }
    }

    private void addNode(Node node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }

    private void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void moveToHead(Node node) {
        removeNode(node);
        addNode(node);
    }

    @Override
    public void printCache() {
        System.out.print("Cache state: ");
        Node current = head.next;
        while (current != tail) {
            System.out.print("[" + current.key + "=" + current.value + "] ");
            current = current.next;
        }
        System.out.println();
    }
}