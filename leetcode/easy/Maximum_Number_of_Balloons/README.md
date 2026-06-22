## Intuition

Match each letter with the letters in the ballon. If each letter matches add it to the count. Then find Max number of counts.

## Approach

Match each letter with the letters in the ballon. If each letter matches add it to the count. Then find Max number of counts, by using min since the compiler uses n-1 method and starts from 0.

## Complexity
### Time Complexity
**O(n)**
### Space Complexity
* **General case:** **O(k)** (or **O(n)** in the worst case)
* **For lowercase English letters only:** **O(1)**

## Code
```python
    from collections import Counter

    text = input("Enter the text: ")

    count = Counter(text)

    max_balloons = min(
        count['b'],
        count['a'],
        count['l'] // 2,
        count['o'] // 2,
        count['n']
    )

    print(f"Maximum number of instances of 'balloon' that can be formed: {max_balloons}")
```