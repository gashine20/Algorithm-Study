import java.io.*;

public class Main {
	//카운팅 정렬 
	static void counting_sort(int arr[]) throws IOException {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int[] counting = new int[10001];
		
		for(int i=0;i<arr.length;i++) { //array-> counting
			counting[arr[i]]++;
		}
		
		
		for(int i =0;i<counting.length;i++) {
			for(int j=0;j<counting[i];j++){
				bw.write(Integer.toString(i)+ "\n");			
			}
			
		}
		
		bw.flush();
		bw.close();
	}
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(bf.readLine());
		int[] arr = new int[N];
		
		for(int i =0;i<arr.length;i++) {
			arr[i]= Integer.parseInt(bf.readLine());
		}
		
		counting_sort(arr);
		
	}

}
