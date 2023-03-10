public class General3 {
	public static int findSecondSmallest(int[] array) {
		int[] smallest_ints = new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE};
		for(int i = 0; i < array.length; i++) {
			if(array[i] < array[smallest_ints[0]]) {
				smallest_ints[1] = smallest_ints[0];
				smallest_ints[0] = i;
			}else if(array[i] <= array[smallest_ints[1]]) {
				smallest_ints[1] = i;
			}
		}
		return array[smallest_ints[1]];
	}

	public static void main(String[] args) {
	}
}
