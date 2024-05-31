import java.util.HashMap;
import java.util.Map;

public class CacheFactory {
    public enum CacheType {
        LRU
        // Add more cache types here if needed
    }

    private static final Map<CacheType, Integer> DEFAULT_CAPACITY_MAP;

    static {
        DEFAULT_CAPACITY_MAP = new HashMap<>();
        DEFAULT_CAPACITY_MAP.put(CacheType.LRU, 100); // Default capacity for LRU cache
        // Add default capacities for other cache types if needed
    }

    public static <K, V> Cache<K, V> createCache(CacheType type) {
        return createCache(type, DEFAULT_CAPACITY_MAP.get(type));
    }

    public static <K, V> Cache<K, V> createCache(CacheType type, int capacity) {
        switch (type) {
            case LRU:
                return new LRUCache<>(capacity);
            // Add more cases for other cache types
            default:
                throw new IllegalArgumentException("Invalid cache type: " + type);
        }
    }
}