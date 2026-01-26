import java.util.*;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int a = gcd(arrayA);
        int b = gcd(arrayB);
        
        // System.out.println("a: " + a + " b: " + b);
        
        if(!validateSplit(b, arrayA)){
            b = 0;
        }
        if(!validateSplit(a, arrayB)){
            a =0;
        }
        int answer = Math.max(a, b);
        
        return answer;
    }
    
    public boolean validateSplit(int b, int[] array) {
        if(b == 0){
            return true;
        }
        for(int a : array){
            if(a < b) continue;
            if(a % b == 0){
                return false;
            }
        }
        return true;
    }
    
    public int gcd(int[] array) {
        int result = 0;
        // 정렬
        Arrays.sort(array);
        
        // 작은 수의 약수 구하고
        int a = array[0];
        // System.out.println("작은수 : " + a);
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 1; i < Math.sqrt(a); i++) {
            if(a%i == 0){
                list.add(i);
                list.add(a/i);
            }
        }
        if((int)Math.sqrt(a) * (int)Math.sqrt(a) == a){ // 25 = 5* 5인경우 5도 추가
            list.add((int)Math.sqrt(a));
        }
        
        Collections.sort(list, Collections.reverseOrder());

        // 큰 약수부터 모두 나눠지는지 확인
        for(int B : list){
            if(B == 1){
                break;
            }
            boolean flag = true;
            
            for(int A : array){
                if(A%B !=0 ){
                    // System.out.println("A:" + A + " B:" + B + "로 나눠지지 않음");
                    flag = false;
                    break;
                }
            }
            if(flag){
                result = B;
                break;
            }
        }
        
        // 나눠지는거 없으면 그냥 return 0
        return result;
    }
    
    
}