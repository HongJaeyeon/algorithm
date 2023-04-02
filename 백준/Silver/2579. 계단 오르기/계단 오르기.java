import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] p = new int[N+1];
		int[] dp = new int[N+1];
		for (int i = 1; i <= N; i++) {
			p[i] = Integer.parseInt(br.readLine());
		}
		if (N == 1) {
			System.out.println(p[1]);
		}else if (N == 2) {
			System.out.println(p[1] + p[2]);
		}else {
			dp[1] = p[1];
			dp[2] = p[1] + p[2];
			for (int i = 3; i <= N; i++) {			
				dp[i] = Math.max(dp[i-3]+p[i-1]+p[i], dp[i-2]+p[i]);
			}
			System.out.println(dp[N]);		
		}

//		i-3 i-2 i-1 i
//		i(마지막칸)에 도착했을때 이전 칸을 갔다가 온건지(2연속) 아니면 이전 칸을 건너뛰고 온 건지 나누면된다.
	}

}