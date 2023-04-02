import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[] p;
	static int[] dp;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		p = new int[N+1];
		dp = new int[N+1];
		for (int i = 1; i <= N; i++) {
			p[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= i; j++) {
				//dp[i]는 맨처음에 0으로 초기화 되어있기 때문에 가능 
				dp[i] = Math.max(dp[i], dp[i-j]+p[j]);
			}
		}
		System.out.println(dp[N]);
	}
}

//dp[2] = max(dp[0]+p2, dp[1]+p1)
//dp[3] = max(dp[0]+p3, dp[1]+p2, dp[2]+p1)
//dp[4] = max(dp[0]+p4, dp[1]+p3, dp[2]+p2, dp[3]+p1)