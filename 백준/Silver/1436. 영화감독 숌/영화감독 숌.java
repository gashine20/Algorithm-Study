import java.util.*;

public class Main {
	//영화감독 숌
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int endNumber =666; //종말 숫자
		int count = 1; //N번째를 찾아야한다.
		
		int N=sc.nextInt();
		
		while(count != N) {
			endNumber++;
			if(String.valueOf(endNumber).contains("666")) {
				count++;
			}
			
		}
		
		System.out.println(endNumber);
				

	}

}
