import java.util.Iterator;

public class CustomQueueWithIterator<T> implements Iterable<T> {
    private Object[] arr;
    private int front;
    private int rear;
    private int size;
    private int capacity;
    
    public CustomQueueWithIterator(int cap) {
        capacity = cap;
        arr = new Object[capacity];
        front = 0;
        size = 0;
        rear = -1;
    }

    private void grow() {
        int newCap = capacity * 2;
        Object[] newArr = new Object[newCap];

        int i = front;
        int idx = 0;
        int count = 0;

        while(count < size) {
            newArr[idx] = arr[i];
            idx++;
            i++;
            if (i == capacity) i = 0;
            count++;
        }

        arr = newArr;
        capacity = newCap;
        front = 0;
        rear = size - 1;
    }
    
    public void enqueue(T data) {
        if (size == capacity) {
            grow();
        }
        
        rear = (rear + 1) % capacity;
        arr[rear] = data;
        size++;
    }
    
    @SuppressWarnings("unchecked")
    public T dequeue() {
        if (size == 0) {
            return null;
        }
        T removed = (T) arr[front];
        arr[front] = null;
        front = front + 1;
        
        if (front == capacity) front = 0;
        size --;
        return removed;
    }

    @SuppressWarnings("unchecked")
    public T peek() {
        if (size == 0) {
            return null;
        }
        return (T) arr[front];
    }
    
    public int size() {
        return size;
    }

    public Iterator<T> iterator() {
        return new QueueIterator();
    }

    private class QueueIterator implements Iterator<T> {
        private int index = front;
        private int count = 0;

        public boolean hasNext() {
            return count < size;
        }

        public T next() {
            T val = (T) arr[index];
            index++;
            if (index == capacity) index = 0;
            count++;
            return val;
        }
    }
    
    public void printQueue() {
        Iterator<T> it = iterator();
        while (it.hasNext()) {
            System.out.println(it.next() + " ");
        }
        System.out.println();
    }
}

class Main {
    public static void main(String[] args) {
        CustomQueueWithIterator<String> cq = new CustomQueueWithIterator<String>(5);
        cq.enqueue("A");
        cq.enqueue("B");
        cq.enqueue("C");
        cq.enqueue("D");
        cq.enqueue("E");
        cq.printQueue();
        cq.dequeue();
        cq.enqueue("F");
        cq.printQueue();
        for (String s : cq) {
            System.out.println(s + " ");
        }
        
    }
}
