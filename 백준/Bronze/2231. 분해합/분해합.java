import java.util.*;

public class Main {

	private static int getDivideSum(int N) {
		
		int M=0;//우리가 찾아야 될 값
		
		for(int i =0; i<N;i++) {//N보다 작은 수부터 한개씩 찾기
			int number = i;
			//100의 자리수라고 한정했다.
			int sum=0;  
			while(number !=0) {
				sum+=number%10; //자릿수 더하기
				number/=10;
			}
			
			if(sum + i == N) { // 자기 자신 더하기 
				M = i;
				break;
			}
			
		}
		return M;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int M; int N; //M은 N의 생성자 
	
		N = sc.nextInt();
		
		M = getDivideSum(N);
		System.out.println(M);
		
		sc.close();
		
	}

}
