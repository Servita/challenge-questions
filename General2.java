import java.util.ArrayList;

protected class IntersectFinder<T> {
	public boolean contains(T item, T[] array) {
		for(T arr_element : array) {
			if(item.equals(arr_element)) return true;
		}
		return false;
	}

	public T[] insersect(T[] array_1, T[] array_2) {
		ArrayList<T> intersect = new ArrayList<T>();
		for(T item : array_1) {
			if(this.contains(item, array_2)) {
				intersect.add(item);
			}
		}
		return (T[]) intersect.toArray();
	}
}

public class General2 {	
	public static void main(String args[]) {
	}
}
