public class General4 {
	public static boolean isPalindrome(String text) {
		int first = 0;
		int last = text.length();
		while(first < last) {
			if(text.charAt(first) != text.charAt(last))
				return false;
			first++;
			last++;
		}
		return true;
	}

	public static void main(String[] args) {
	}
}
