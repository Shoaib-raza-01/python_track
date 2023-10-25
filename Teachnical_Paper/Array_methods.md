# Array Methods


In python arrays are generally represented by List.  
List are mutable data type.

1. **append(item)**
   - It appends an item to the end of the list.
   
     ```python
     list1 = [1, 2, 3]
     list1.append(4)
     ```

2. **extend(iterable)**
   - It appends the elements of an iterable (e.g., another list) to the end of the list.
   
     ```python
     list1 = [1, 2, 3]
     list2 = [4, 5]
     list1.extend(list2)
     ```

3. **insert(index, item)**
   - It inserts an item at the specified index in the list.
   
     ```python
     list1 = [1, 2, 3]
     list1.insert(1, 4)
     ```

4. **remove(item)**
   - It removes the first occurrence of the specified item from the list.
   
     ```python
     list1 = [1, 2, 3, 2]
     list1.remove(2)
     ```

5. **pop(index)**
   - It removes and returns the item at the specified index. If no index is provided, it removes and returns the last item.
   
     ```python
     list1 = [1, 2, 3]
     popped = list1.pop(1)
     ```

6. **index(item)**
   - It returns the index of the first occurrence of the specified item in the list.
   
     ```python
     list1 = [1, 2, 3, 2]
     index = list1.index(2)
     ```

7. **count(item)**
   - It returns the number of times the item appears in the list.
   
     ```python
     list1 = [1, 2, 3, 2]
     count = list1.count(2)
     ```

8. **sort()**
   - It sorts the list in ascending order (in-place).
   
     ```python
     list1 = [3, 1, 2]
     list1.sort()
     ```

9. **reverse()**
   - It reverses the order of elements in the list (in-place).
   
     ```python
     list1 = [1, 2, 3]
     list1.reverse()
     ```

10. **copy()**
    - It creates a shallow copy of the list.
    
      ```python
      original = [1, 2, 3]
      copy = original.copy()
      ```

11. **clear()**
    - It removes all items from the list, making it empty.
    
      ```python
      list1 = [1, 2, 3]
      list1.clear()
      ```
