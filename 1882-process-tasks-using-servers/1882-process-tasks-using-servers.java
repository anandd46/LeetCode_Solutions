class Solution {
    public int[] assignTasks(int[] servers, int[] tasks) {
        PriorityQueue<int[]> free = new PriorityQueue<>((a, b) -> 
            a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]
        );
        
        PriorityQueue<int[]> busy = new PriorityQueue<>((a, b) -> 
            a[0] != b[0] ? a[0] - b[0] : (a[1] != b[1] ? a[1] - b[1] : a[2] - b[2])
        );
        
        for (int i = 0; i < servers.length; i++) {
            free.add(new int[]{servers[i], i});
        }
        
        int[] ans = new int[tasks.length];
        int time = 0;
        
        for (int j = 0; j < tasks.length; j++) {
            time = Math.max(time, j);
            
            if (free.isEmpty()) {
                time = busy.peek()[0];
            }
            
            while (!busy.isEmpty() && busy.peek()[0] <= time) {
                int[] curr = busy.poll();
                free.add(new int[]{curr[1], curr[2]});
            }
            
            int[] curr = free.poll();
            ans[j] = curr[1];
            busy.add(new int[]{time + tasks[j], curr[0], curr[1]});
        }
        
        return ans;
    }
}