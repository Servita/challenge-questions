import java.util.ArrayList;
import java.util.List;

public class General {
    //Create a function that accepts an array of integers and returns the sum of all the even numbers in the array.
    public static Integer question1(List<Integer> numbers){
        int sum = 0;
        for (Integer i : numbers){
            sum += i;
        }
        return sum;
    }


    //Create a function that accepts two arrays and returns a new array that contains only the elements that are common between the two arrays.
    public static List<Integer> question2(List<Integer> list1, List<Integer> list2){
        ArrayList<Integer> list3 = new ArrayList<>();
        for (Integer i : list1){
            if (list2.contains(i)){
                list3.add(i);
            }
        }
        return list3;
    }

    //Create a function that accepts an array of integers and returns the second smallest number in the array.
    public static Integer question3(List<Integer> list){
        list.sort(null);
        return list.get(list.size()-2);
    }

    //Write a program that accepts a string and returns true if the string is a palindrome, false otherwise.
    public static Boolean question4(String word){
        String reversed = "";
        for (int i = 0; i<word.length(); i++){
            reversed += word.toLowerCase().charAt(word.length()-1 - i);
        }
        return word.equals(reversed);
    }

    //Write a program that accepts two strings and returns true if they are anagrams of each other, false otherwise.
    public static Boolean question5(String word1, String word2){
        ArrayList<String> word3 = new ArrayList<>();
        for (String s : (word1.split(""))){
            word3.add(s);
        }

        return false;
    }

    public static void main(String[] args) {
        System.out.println(General.question4("word"));
        System.out.println(General.question4("racecar"));
    }
}
