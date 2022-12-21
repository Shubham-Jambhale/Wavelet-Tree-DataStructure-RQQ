class Node:
    def __init__(self, char,freq,zero,one, left=None, right=None):

        self.char = char
        self.freq = freq
        self.zero_counter = zero
        self.one_counter = one
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right


class Wavelet_Tree:
    def __init__(self, freq, left=None, right=None):

        # assigning the given array to self variable
        self.char_array = freq
        
        # finding out mid and calculatimng the frequency array
        self.mid =  (min(freq)+ max(freq)) / 2
        self.frequ= []
        for i in range(len(freq)):
            if freq[i] > self.mid:
                self.frequ.append(1)
            else:
                self.frequ.append(0)
        
        #calculating the prefix sum which is calculated in 2 arrays one is numbner of zeros and number of ones.
        zero_counter = 0
#this array indicated the number of zeros which are there i.e if given array is [0010] then zero array will store [1,2,2,3]
        self.zero = []
        one_counter = 0
#this array indicated the number of ones which are there i.e if given array is [0010] then zero array will store [0,0,1,1]
        self.one =[]
        
        # iterating over the frequency aray and deriving the ones and zeros array.
        for i in range(len(self.frequ)):
            if self.frequ[i] == 0:
                zero_counter += 1
            self.zero.append(zero_counter)
            if self.frequ[i] == 1:
                one_counter += 1
            self.one.append(one_counter)
        self.create_wavelet_tree(self.char_array,self.frequ,self.zero,self.one)

    #this is the print function which is BFS or level order
    
    def print(self):
        queue =[]
        # appending the root and start iterating
        queue.append(self.start)
        l = 0
        while queue:
            #this is to store the elements at each level
            temp_level =[]
            for i in range(len(queue)):
                elem = queue.pop(0)
                #to store the intermediate elements in the level.
                temp = []
                #if it is a single empty array we have to store X in place of it 
                if elem.freq == [0]:
                    temp.append('X')
                # joining the frequency in string format
                else:
                    temp.append("".join(str(k) for k in elem.freq))
                
                #if element has left then appending it to queue
                if elem.left:
                    queue.append(elem.left)
                # if element has right appending it to queue
                if elem.right:
                    queue.append(elem.right)
                # appending the intermediate elements to the array which stores element at each level
                temp_level.append("".join(str(k) for k in temp)) 
            
            #skipping the last level of leaf nodes
            if len(set(temp_level)) == 1 and temp_level[0] == 'X':
                pass
            #printing the level
            else:
                print("Level",l,":",temp_level)
                l += 1
                    
               
    def create_wavelet_tree (self,array,freq,zero,one) :
    # creating a node of the tree which includes 4 arrays. 1.elements array, 2.frequency array, 3.zero array, 4.one array
        self.start = Node(array,freq,zero,one)
        queue =[]
        queue.append(self.start)
        l = 0
        #following the same procedure as the BFS and iterating over the tree and creating the tree
        while queue:
            for i in range(len(queue)):
                element = queue.pop(0)
                if len(set(element.char)) == 1:
                       continue 
                curr = element
                temp = []
                left = []
                right = []
                left_frequ = []
                right_frequ = []
                zero_counter_left = []
                one_counter_left = []
                zero_counter_right = []
                one_counter_right = []
                one_counter = 0
                zero_counter = 0 
              
                if len(element.char) > 1:
                    #creating the left and right arrays
                    for i in range(len(element.char)):
                        if element.freq[i] == 1:
                            right.append(element.char[i])
                        else:
                            left.append(element.char[i])
                   
                #creating frequency arry for left as we have to recalculate the frequency after creating the left arrray
                    if left != []:
                        mini_left = min(left)
                        maxi_left = max(left)
                        mid_left = (mini_left + maxi_left) / 2
                        for i in range(len(left)):
                            if left[i] > mid_left:
                                left_frequ.append(1)
                            else:
                                left_frequ.append(0)
                # creating the frequency array for right array as we have to recalculate the frequency after creating the right array
                    if right != []:
                        mini_right = min(right)
                        maxi_right = max(right)
                        mid_right = (mini_right+maxi_right) / 2
                        for i in range(len(right)):
                            if right[i] > mid_right:
                                right_frequ.append(1)
                            else:
                                right_frequ.append(0)
                    
                 #creating zeros and ones array so they can be accessed in the Rqq using 0(1) time complexity.   
                    for i in range(len(left_frequ)):
                        if left_frequ[i] == 0:
                            zero_counter += 1
                        zero_counter_left.append(zero_counter)
                        if left_frequ[i] == 1:
                            one_counter += 1
                        one_counter_left.append(one_counter)
                    zero_counter = 0
                    one_counter = 0
                    
                    for i in range(len(right_frequ)):
                        if right_frequ[i] == 0:
                            zero_counter += 1
                        zero_counter_right.append(zero_counter)
                        if right_frequ[i] == 1:
                            one_counter += 1
                        one_counter_right.append(one_counter)
                    
                    
                    #adding element to left and right of the tree node
                    element.left = Node(left,left_frequ,zero_counter_left,one_counter_left)
                    element.right = Node(right,right_frequ,zero_counter_right,one_counter_right)
                    
                    #appending element ot the queue
                    if curr.left!=None:
                        queue.append(curr.left)
            
                    if curr.right!=None:
                        queue.append(curr.right)
                        
    #calculating the Rqq         
    def RQQ ( self , k , left , right ) :
        curr = self.start
        level = 0
        while curr :
            print("Level",level,":",(k,left,right))
            level += 1
            #handling the case for left goilg less than zero
            if left - 2 < 0:
                no_of_zero = curr.zero_counter[right-1]
            else:  
                no_of_zero = (curr.zero_counter[right-1] - curr.zero_counter[left - 2]) 
            
            #deciding on which side of the tree to go.
            if no_of_zero >= k:
#                 print("gooing left")
                #going on the left side of the tree and recalculating the left right  
                if (left-2) < 0:
                    left = 1
                else:    
                    left = curr.zero_counter[left - 2] + 1
                
                right = curr.zero_counter[right-1]

                if k == 1 and left == 1 and right == 1:
                    ans = curr.char
                    print("Level",level,":",(k,left,right))
                    level += 1
                    curr = curr.left
                    return curr.char
                if curr.left:
                    curr=curr.left
                else:
                    break
            else:
                #going to the right and recalculating the k, left, right
                k = k - no_of_zero
                if (left-2) < 0:
                    left = 1
                else:
                    left = curr.one_counter[left - 2] + 1
                right = curr.one_counter[right-1]
                
                if k == 1 and left == 1 and right == 1:
                    print("Level",level,":",(k,left,right))
                    ans = curr.char
                    level += 1
                    curr =curr.right
                    return  curr.char
                if curr.right:
                     curr = curr.right
                else:
                    break
        return curr.char
                        
if __name__=="__main__":
    
    print("---Output---")
    print()
    w = Wavelet_Tree([6, 2, 0, 7, 9, 3, 1, 8, 5, 4])
    print("Wavelet Tree for [6, 2, 0, 7, 9, 3, 1, 8, 5, 4] is:")
    print()
    w.print()
    print()
    output = w.RQQ(5,3,9)
    print()
    print("Minimum for RQQ (5,3,9) is :")
    print(output)
    print()

    w = Wavelet_Tree([1, 2, 0, 3, 9, 4])
    print("Wavelet Tree for [1, 2, 0, 3, 9, 4] is:")
    print()
    w.print()
    print()
    output = w.RQQ(3,2,6)
    print()
    print("Minimum for RQQ (3,2,6) is:")
    print(output)
    print()

    w = Wavelet_Tree([1, 2, 0, 3, 9, 4])
    print("Wavelet Tree for [1, 2, 0, 3, 9, 4] is:")
    print()
    w.print()
    print()
    output = w.RQQ(3,1,3)
    print()
    print("Minimum for RQQ (3,1,3) is:")
    print(output)
    print()

    w = Wavelet_Tree([1, 2, 0, 3, 4, 4])
    print("Wavelet Tree for [1, 2, 0, 3, 4, 4] is:")
    print()
    w.print()
    print()
    output = w.RQQ(5,1,6)
    print()
    print("Minimum for RQQ (4,1,6) : ")
    print(output)
    print()
    w = Wavelet_Tree([3,3,3,3,3,4])
    print("Wavelet Tree for [3,3,3,3,3,4] is:")
    print()
    w.print()
    print()
    output = w.RQQ(6,1,6)
    print()
    print("Minimum for RQQ (6,1,6) :")
    print(output)
        