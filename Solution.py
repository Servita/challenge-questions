class Solution:
    def EvenSum (list):
        answer = 0
        for i in range (len(list)):
            if list[i] % 2 == 0:
                answer += list[i]
        return answer

    def Common (list1, list2):
        answer = []
        for elem in list1:
            if elem in list2:
                answer.append(elem)
        return answer

    def Smallest2 (list : list):
        if list[0] > list[1]:
            smallest = list[1]
            smallest2 = list[0]
        else:
            smallest = list[0]
            smallest2 = list[1]
        for elem in list:
            if elem < smallest:
                smallest2 = smallest
                smallest = elem
            elif elem < smallest2:
                smallest2 = elem
        return smallest2

    def palindrome (string : str):
        for i in range(len(string)/2):
            if string[i] != string[(len(string)-1)-i]:
                return False
        return True

    def anagrams (word1 : str, word2 : str):
        if word1.length= != word2.length:
            return False
        for elem in word1:
            if elem not in word2:
                return False
        return True