- `if`
  
```python
x = int(input('please enter an integer:'))

if x < 10:
    print('less than 10')
elif x == 10:
    print('equal 10 ')
else:
    print('more than 10')
```

- `for`

```python
nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    print(n)
```


- `range()` function

```python
for i in range(5):
    print(i)
```
> output: [0,5)


- `break` and `continue`

```python
for i in range(10):
    if i % 2 == 0: 
        continue
    elif i == 5:
        break
    else:
        print(i, ' is odd number')
```
> 1  is odd number  
> 3  is odd number  

- `pass` 
> doing nothing

```python
n = 1
if n == 1:
    pass
else:
    print('complete')
```