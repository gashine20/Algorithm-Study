import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Stack {
    int top;
    int size;
    int[] stack;

    Stack(int n) { //생성자
        stack = new int[n];
        top = -1;
        size = 0;
    }

    public int top() {
        if (empty() == 1) return -1;
        else return stack[top];
    }

    public int size() { //스택에 들어있는 정수 개수
        return size;
    }

    public int pop() {
        if (empty() == 1) return -1;
        else {
            size--;
            return stack[top--];
        }
    }

    public void push(int x) {
        stack[++top] = x;
        size++;
    }

    public int empty() {
        if (size == 0) return 1;
        else return 0;
    }
}

public class B10828 {
    //스택

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] stack = new String[N];

        for (int i = 0; i < N; i++) {
            stack[i] = br.readLine();
        }

        Stack stack2 = new Stack(N);

        for (int i = 0; i < N; i++) {
            if (stack[i].equals("top")) {
                System.out.println(stack2.top());
            } else if (stack[i].equals("size")) {
                System.out.println(stack2.size());
            } else if (stack[i].equals("empty")) {
                System.out.println(stack2.empty());
            } else if (stack[i].equals("pop")) {
                System.out.println(stack2.pop());
            } else { //push
                int n = Integer.parseInt(stack[i].substring(5, stack[i].length()-1));
                stack2.push(n);
            }
        }

    }
}





