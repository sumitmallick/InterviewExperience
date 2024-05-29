# Approach 1
def max_sum_non_adjacent_array(input_list):
	if not input_list:
    return 0
  n = len(input_list) # 4
  if n == 1:
    return input_list[0]
  
  if n == 2:
    return max(input_list[0], input_list[1])

  two_prev = input_list[0] # 2
  prev = max(input_list[0], input_list[1]) # max(2, 5) = 5
  
  for i in range(2, n): # 3
    curr = max(prev, two_prev + input_list[i]) # max(5,5+6) = 11 -> [2, 5, 5, 11]
    two_prev = prev
    prev = curr
  return prev


# input_list = [2, 5, 1, 6]
# Time com: O(n-2) -> O(n)
# Space: O(1)

# Approach 2

def max_sum_non_adjacent_array(input_list):
	def max_val(i, val_dict):
    if i < 0:
    	return 0
    if i in val_dict:
      return val_dic[i]
    
    first_curr = input_list[i] + max_val(i-2, val_dict)
    sec_curr =max_val(i-1, val_dict)
    
    val_dict[i] = max(first_curr, sec_curr)
    return val_dict[i]
    	
  if not input_list:
    return 0
    	
  val_dict = {}
  return max_val(len(input_list) - 1, val_dict)
