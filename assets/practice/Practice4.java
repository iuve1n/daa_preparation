import java.util.*;
class Practice4 {
static int solve(String a, String b) {
  // TODO: implement without looking at the reference.
  return 0;
}
public static void main(String[] args) {
check(solve("cat","cut")==1);check(solve("","abc")==3);check(solve("kitten","sitting")==3);check(solve("same","same")==0);
System.out.println("All listed checks passed");
}
static void check(boolean ok){if(!ok)throw new AssertionError("A listed check failed");}
}
