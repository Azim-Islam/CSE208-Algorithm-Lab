#include <stdio.h>
#include <limits.h>
#include <time.h>  

typedef long long ll;


int coins[] = {1, 2, 4, 6, 38, 41, 51, 52, 66, 88}; 
//int coins[] = {1, 4, 8, 10}; 
int dp [1000000] = {0};

int min(int a, int b)
{
    if (a > b){
        return b;
    }
    else{
        return a;
    }
}

ll minCoinsDynamic(int N, int M) // N = Coin change amount, M = Number of Notes
{
    //Initializing all values to INT_MAX i.e. minimum coins to make any
    //amount of sum is INT_MAX
    for(int i = 0;i<=N;i++)
        dp[i] = INT_MAX;
    
    //Base case 
    //Minimum coins to make sum = 0 cents is 0
    dp[0] = 0;
    
    //Iterating in the outer loop for possible values of sum between 1 to N
    //Since our final solution for sum = N might depend upon any of these values
    for(int i = 1;i<=N;i++)
    {
        //Inner loop denotes the index of coin array.
        //For each value of sum, to obtain the optimal solution.
        for(int j = 0;j<M;j++)
        {
        //i —> sum
        //j —> next coin index
        //If we can include this coin in our solution
        if(coins[j] <= i)
        {
            //Solution might include the newly included coin
            dp[i] = min(dp[i], 1 + dp[i - coins[j]]);
        }
        }
    }
  return dp[N];
}


int findMinGreedy(int cost,int M) // cost = Change To Make, M = Number Of Notes To Make
{
    int i, k = 0;
    int count = 0;
    for (i = M-1; i >= 0; i--) {
        while (cost >= coins[i]) {
            cost -= coins[i];
            //printf("\t%d Taka Note Required in Greedy\n ", coins[i]);
            count += 1;
        }
    }
    return count;
}
  

int main(){

    double time_spent = 0.0;
    clock_t begin = clock();
    // Checking how much time passed then the function is called
    printf("%llu Number of notes required in Dynamic\n", minCoinsDynamic(2500, 10)); 
    clock_t end = clock();
    // calculate elapsed time by finding difference (end - begin) and
    // dividing the difference by CLOCKS_PER_SEC to convert to seconds
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    printf("The runtime of Dynamic Technique is %.32f seconds\n", time_spent);



    time_spent = 0.0;
    begin = clock();
    // do some stuff here
    printf("%d Number of notes required in Greedy\n", findMinGreedy(2500, 10) );
    end = clock();
    // calculate elapsed time by finding difference (end - begin) and
    // dividing the difference by CLOCKS_PER_SEC to convert to seconds
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    printf("The runtime of Greedy Technique is %.32f seconds\n", time_spent);
    

}