# Cache

#### Contraints:
- Class name must be "Main"
- Libraries included:
- json simple, guava, apache commons lang3, junit, jmock


## LRU Cache


Cache replacement algorithms are efficiently designed to replace the cache when the space is full. 
The Least Recently Used (LRU) is one of those algorithms. As the name suggests when the cache memory is full, 
LRU picks the data that is least recently used and removes it in order to make space for the new data. 
The priority of the data in the cache changes according to the need of that data i.e. if some data is fetched 
or updated recently then the priority of that data would be changed and assigned to the highest priority, 
and the priority of the data decreases if it remains unused operations after operations.


Operations in LRU Cache

* LRUCache (Capacity c): Initialize LRU cache with positive size capacity c.
* get (key): Returns the value of Key 'k' if it is present in the cache otherwise it returns -1. Also updates the priority of data in the LRU cache.
* put (key, value): Update the value of the key if that key exists, Otherwise, add key-value pair to the cache. 
  If the number of keys exceeded the capacity of LRU cache then dismiss the least recently used key.


The functions get and put must each run in O(1) average time complexity.

### Sample Template

class Main {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
