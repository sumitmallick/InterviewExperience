public class Main {
    public static void main(String[] args) {
        Cache<Integer, Integer> lruCache = CacheFactory.createCache(CacheFactory.CacheType.LRU);

        lruCache.put(1, 1);
        lruCache.printCache(); // Print cache state

        lruCache.put(2, 2);
        lruCache.printCache(); // Print cache state

        System.out.println(lruCache.get(1)); // returns 1
        lruCache.printCache(); // Print cache state

        lruCache.put(3, 3); // evicts key 2
        lruCache.printCache(); // Print cache state

        System.out.println(lruCache.get(2)); // returns -1 (not found)
        lruCache.printCache(); // Print cache state

        lruCache.put(4, 4); // evicts key 1
        lruCache.printCache(); // Print cache state

        System.out.println(lruCache.get(1)); // returns -1 (not found)
        lruCache.printCache(); // Print cache state

        System.out.println(lruCache.get(3)); // returns 3
        lruCache.printCache(); // Print cache state

        System.out.println(lruCache.get(4)); // returns 4
        lruCache.printCache(); // Print cache state
    }
}