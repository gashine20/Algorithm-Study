import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    //숫자 카드
    static boolean search_binary(int[] arr,int num){ //이진탐색
        int leftIndex =0;
        int rightIndex = arr.length-1;


            while(leftIndex<=rightIndex){
                int midIndex = (leftIndex+rightIndex)/2;
                int mid = arr[midIndex];

                if(mid > num) rightIndex = midIndex-1; //mid값이 찾는 값보다 크면 오른쪽으로 이동
                else if(mid<num) leftIndex = midIndex +1;
                else return true;
            }
            return false;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] numCard = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<numCard.length;i++){
            numCard[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(numCard);

        int M = Integer.parseInt(br.readLine());
        int[] findCard = new int[M];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<findCard.length;i++){
            findCard[i] =  Integer.parseInt(st.nextToken());
        }

        for(int i=0;i<findCard.length;i++){
            if(search_binary(numCard,findCard[i])){
                System.out.print(1 + " ");
            }
            else System.out.print(0 + " ");
        }


    }
}
