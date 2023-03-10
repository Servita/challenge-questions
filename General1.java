public class General1 {
	public static int sum1(int[] array) {
		int sum = 0;
		for(int number : array) {
			if(number % 2 == 0) sum += number;
		}
		return sum;
	}

	public static void main(String[] args) {
	}
}
