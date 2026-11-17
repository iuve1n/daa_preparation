import java.util.*;
class Practice7 {
static int[] solve(String s, int[] sa) {
  // TODO: implement without looking at the reference.
  return new int[0];
}
public static void main(String[] args) {
check(Arrays.equals(solve("banana",new int[]{5,3,1,0,4,2}),new int[]{0,1,3,0,0,2}));check(Arrays.equals(solve("aaa",new int[]{2,1,0}),new int[]{0,1,2}));check(Arrays.equals(solve("a",new int[]{0}),new int[]{0}));check(solve("",new int[]{}).length==0);
System.out.println("All listed checks passed");
}
static void check(boolean ok){if(!ok)throw new AssertionError("A listed check failed");}
}
