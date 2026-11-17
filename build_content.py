import json
from pathlib import Path
lessons=[]
def lesson(title,subtitle,topics,sections,lab,code,resource):
 lessons.append(dict(id=len(lessons)+1,title=title,subtitle=subtitle,topics=topics.split('|'),sections=[dict(title=a,body=b,example=c) for a,b,c in sections],lab=lab,code=code,resource=resource))
lesson('Think like an algorithm designer','From a problem statement to a defensible solution.','Contracts|Correctness|Cost models',[
('Start with a contract','An algorithm is a finite, unambiguous procedure. Before choosing a data structure, specify valid inputs, the required output, and edge cases. Correctness is relative to this contract: returning any pair is different from returning the first pair.','Two-sum contract: given an integer array and a target, return two distinct indices whose values sum to the target, or report that none exist. Can indices repeat? No. Can values repeat? Yes.'),
('Build a baseline, then improve it','A simple correct solution is a reference implementation. Enumerate every pair in O(n²) time and O(1) auxiliary space. A hash-set scan trades O(n) space for expected O(n) time. Sorting plus two pointers costs O(n log n), and requires care to preserve original indices.','For [4, 1, 4] and target 8, indices 0 and 2 are valid. A solution that stores only distinct values must still account for two occurrences.'),
('Separate evidence from proof','Tests can expose a bug, but passing a finite test set does not prove correctness for all inputs. Prove the core idea and use boundary, random, and adversarial tests to challenge the implementation. Measure operations separately from wall-clock time.','Compare an optimized solution against the brute-force baseline on many small generated arrays. Include empty input, duplicates, negatives, and no-solution cases.')],
'Implement brute-force two-sum in Java. State its contract and test five edge cases. Then describe how you would compare it with a faster implementation.',
'''static int[] twoSum(int[] a, int target) {
  for (int i = 0; i < a.length; i++)
    for (int j = i + 1; j < a.length; j++)
      if ((long) a[i] + a[j] == target)
        return new int[]{i, j};
  return new int[]{-1, -1};
}''','https://algs4.cs.princeton.edu/14analysis/')
lesson('Divide, solve, combine','Recursion, Merge Sort, and recurrence relations.','Recursion|Merge Sort|Recurrences',[
('Make progress toward a base case','Every recursive call must reduce a well-founded measure. A balanced split has logarithmic depth; removing one item at a time has linear depth. Depth alone is not the total work: all calls at each level matter.','T(n)=T(n−1)+Θ(1) expands to n−1 constant-work steps, so T(n)=Θ(n). Binary search instead halves the input and does constant work per level: Θ(log n).'),
('Merge Sort: the merge is the work','Sort each half, then repeatedly take the smaller front item from the two sorted halves. The invariant is that the output prefix is sorted and contains exactly the smallest consumed items. Taking from the left on equality preserves stability.','[7,2,5,1] → [2,7] and [1,5] → take 1, then 2, then 5, then 7. Each merge is linear. Across log₂n levels, total time is Θ(n log n), with Θ(n) auxiliary array space.'),
('Read a recurrence before using a theorem','For T(n)=aT(n/b)+f(n), compare f(n) with n^(log_b a). The Master theorem needs its stated conditions; it does not apply directly to T(n−1). If the nonrecursive work dominates polynomially, verify the regularity condition.','T(n)=2T(n/2)+(n log n)² has f(n)=n²log²n, polynomially larger than n. Also 2f(n/2)/f(n) approaches 1/2. Therefore T(n)=Θ(n²log²n), not Θ(n²log³n).')],
'Assignment 1: implement stable Merge Sort with a shared auxiliary array. Compare against Arrays.sort on random, sorted, reversed, and duplicate-heavy arrays. Derive time and space bounds.',
'''static void mergeSort(int[] a, int lo, int hi, int[] tmp) {
  if (hi - lo <= 1) return;
  int mid = lo + (hi - lo) / 2;
  mergeSort(a, lo, mid, tmp);
  mergeSort(a, mid, hi, tmp);
  int i = lo, j = mid;
  for (int k = lo; k < hi; k++)
    tmp[k] = j == hi || (i < mid && a[i] <= a[j])
        ? a[i++] : a[j++];
  System.arraycopy(tmp, lo, a, lo, hi - lo);
}''','https://algs4.cs.princeton.edu/22mergesort/')
lesson('Prove it. Then measure it.','Asymptotic bounds, invariants, and honest benchmarks.','Big O, Ω, Θ|Invariants|Benchmarking',[
('Bounds are statements, not stopwatch readings','O(g) is an eventual upper bound, Ω(g) a lower bound, and Θ(g) both. These notations do not inherently mean worst, best, or average case. First name the function you are bounding, then give the bound.','3n²+7n+2 is Θ(n²) and O(n³). The latter is valid but loose. An algorithm may have best-case Θ(n) and worst-case Θ(n²).'),
('A loop invariant has three obligations','State a property that holds before each iteration. Prove initialization, maintenance, and termination. Couple the invariant with a decreasing variant to establish termination; partial correctness alone is not enough.','Insertion Sort: before iteration i, a[0..i) is sorted and is a permutation of the original prefix. Inserting a[i] preserves this property. At i=n the whole array is sorted.'),
('Benchmark the question you actually have','Java measurements are affected by JIT compilation, garbage collection, input distribution, and hardware caches. Warm up, repeat, separate setup from timed work, and report input sizes and distributions. A finite benchmark cannot prove an asymptotic bound.','For quadratic work, doubling n tends toward four times the work. A small run that doubles in time does not invalidate the proof: fixed overhead or cache behavior can dominate.')],
'Prove linear search correct using a loop invariant. Measure two implementations across doubling input sizes; record warm-up, repetitions, medians, and the limits of your conclusion.',
'''static int find(int[] a, int x) {
  // Invariant: x is absent from a[0..i).
  for (int i = 0; i < a.length; i++)
    if (a[i] == x) return i;
  return -1;
}''','https://algs4.cs.princeton.edu/14analysis/')
lesson('Choose the right collection','Arrays, linked lists, stacks, queues, and heaps.','Amortization|Cache locality|Binary heaps',[
('Contiguous storage changes real performance','Arrays provide O(1) indexed access and good sequential locality. Linked lists need O(n) indexed search and pointer chasing. Inserting at a known node can be O(1), but finding that node is not free. Use a stack for LIFO and a queue for FIFO.','An ArrayList scan often outperforms a LinkedList scan even though both are Θ(n). Nearby array elements share cache lines; linked nodes may be scattered in memory.'),
('Pay for occasional expensive operations','A dynamic array insertion can cost Θ(n) when capacity grows. With geometric growth, the total copied elements over n appends is O(n), so append has amortized O(1) cost. Amortized analysis bounds a sequence; it is not a probabilistic average.','Doubling capacities 1,2,4,8,… copies fewer than 2n elements in total. Growing capacity by one instead copies 1+2+…+(n−1)=Θ(n²).'),
('Heap order is a local promise','In a min-heap, every parent is at most its children. The root is the minimum, but the array is not globally sorted. Root removal swaps in the last item and sifts down in O(log n). Bottom-up heap construction is O(n).','Removing all n items by standard root removal takes Θ(n log n) in the worst case. Do not multiply build-heap cost by the number of removals.')],
'Assignment 2: implement a dynamic array and a binary min-heap. Document empty-structure behavior. Compare array/list traversal and distinguish observed performance from asymptotic cost.',
'''static void siftDown(int[] h, int size, int i) {
  while (2 * i + 1 < size) {
    int c = 2 * i + 1;
    if (c + 1 < size && h[c + 1] < h[c]) c++;
    if (h[i] <= h[c]) break;
    int t = h[i]; h[i] = h[c]; h[c] = t;
    i = c;
  }
}''','https://algs4.cs.princeton.edu/24pq/')
lesson('Hashing and search trees','Collisions, balance, and prefix-aware search.','Hash tables|Balanced BSTs|Tries',[
('Hashing distributes; it does not make keys unique','Separate chaining stores colliding keys together. With n keys and m buckets, load factor α=n/m; expected lookup is O(1+α) under well-distributed hashing. The worst case remains O(n). Equality checks distinguish colliding keys.','At n=120 and m=40, α=3. If a resize creates 80 buckets, α becomes 1.5. Stored entries must be placed according to the new capacity: copying bucket positions is not enough.'),
('Different collision policies need different deletion rules','Open addressing probes within the table. Deleting a key by making its slot empty can break searches for later keys in the probe chain; a tombstone preserves the chain. Balanced BSTs instead guarantee logarithmic search and support ordered queries.','A plain BST built from ascending keys may become a chain of height n−1. AVL or red-black balancing keeps height O(log n). Hash tables do not directly provide sorted range queries.'),
('A trie follows symbols, not key comparisons','A trie stores one transition per symbol along a key path. Search for length L costs O(L) if transitions are O(1). A terminal marker distinguishes a complete key from a prefix. Memory usage depends strongly on alphabet representation.','Store “car” and “cart”. Both share c→a→r, but “car” needs its own terminal marker. Searching “ca” reaches a node yet must return false for exact-key lookup.')],
'Build a chained hash table and a trie. Force collisions deliberately. Test duplicate updates, deletion, empty keys, and a key that is a prefix of another.',
'''static final class Trie {
  java.util.Map<Character, Trie> next = new java.util.HashMap<>();
  boolean terminal;
  void add(String s) {
    Trie p = this;
    for (char c : s.toCharArray())
      p = p.next.computeIfAbsent(c, k -> new Trie());
    p.terminal = true;
  }
  boolean contains(String s) {
    Trie p = this;
    for (char c : s.toCharArray()) {
      p = p.next.get(c);
      if (p == null) return false;
    }
    return p.terminal;
  }
}''','https://algs4.cs.princeton.edu/34hash/')
lesson('Connect components cheaply','Disjoint sets and minimum spanning trees.','DSU|Kruskal|Prim',[
('DSU maintains a partition','find returns a component representative. union joins distinct components. Path compression flattens find paths; union by size attaches the smaller tree to the larger. Together they give amortized O(α(n)) per operation over a sequence. DSU does not maintain graph paths.','If 0–1 and 2–3 are connected, union(1,3) merges the two sets. A later union(0,2) changes nothing and signals that an added undirected edge would close a cycle.'),
('Kruskal and Prim use the same safe-edge principle','The cut property says a lightest edge crossing a cut is safe for some MST. Kruskal scans edges in weight order and accepts those joining different DSU components: O(E log E). Prim grows one tree with the cheapest crossing edge.','For 1–2(2), 1–3(3), 2–3(1), 2–4(4), 3–4(5), Prim from 1 chooses 1–2, then 2–3, then 2–4. Total weight is 7. The globally smallest edge need not be chosen first by Prim.'),
('State your representation and implementation','Prim with adjacency lists and a binary heap takes O(E log V) on a connected simple graph. A matrix implementation takes O(V²). A lazy heap must skip stale entries. A disconnected input produces a forest if you restart per component.','An MST minimizes total tree weight, not distance from the start. Negative weights are allowed for MSTs. Equal weights can create multiple valid MSTs.')],
'Assignment 3A: implement DSU, Kruskal, and Prim. Cross-check total weights on small random connected graphs. Include ties, negative edges, isolated vertices, and explain the cut property.',
'''static final class DSU {
  int[] p, size;
  DSU(int n) {
    p = new int[n]; size = new int[n];
    for (int i=0;i<n;i++) { p[i]=i; size[i]=1; }
  }
  int find(int x) {
    while (x != p[x]) { p[x]=p[p[x]]; x=p[x]; }
    return x;
  }
  boolean union(int a, int b) {
    a=find(a); b=find(b); if(a==b) return false;
    if(size[a]<size[b]) { int t=a;a=b;b=t; }
    p[b]=a;size[a]+=size[b];return true;
  }
}''','https://cp-algorithms.com/graph/mst_prim.html')
lesson('Put directed graphs in order','DFS, SCCs, topological order, and DAG shortest paths.','Kosaraju|Kahn|DAG paths',[
('Finish time means the whole subtree is done','DFS marks discovery before exploring neighbors and records finish after all descendants are processed. With adjacency lists it costs O(V+E). A recursion stack can overflow on a long chain; an explicit stack needs an exit event to preserve finish order.','In 0→1→2, DFS discovers 0,1,2 and finishes 2,1,0. Reversing finishing order is a topological order only when the graph is a DAG.'),
('Kosaraju separates mutual reachability','First run DFS on the original graph and collect vertices on exit. Then process vertices in decreasing finish order on the transpose, starting a new component at each unvisited vertex. Both passes together take O(V+E). Contracting SCCs always yields a DAG.','If A→B→C→A and C→D, then {A,B,C} is one SCC and {D} another. Their condensation has one edge. A cycle between components would mean they were mutually reachable and should be one component.'),
('Topological order is a dependency schedule','Kahn repeatedly removes zero-indegree vertices and decrements successors. If fewer than V vertices are removed, a directed cycle exists. For DAG shortest paths, initialize the source to 0, others to infinity, and relax outgoing edges in topological order. Negative edges are safe because there is no cycle.','In s→a(4), s→b(2), a→b(−5), process s,a,b to obtain distance(b)=−1. Dijkstra’s nonnegative-edge assumption would not hold here.')],
'Assignment 3B: implement Kosaraju, Kahn, and DAG shortest paths. Verify every reported component is mutually reachable on small inputs. Reject cyclic inputs for the DAG routine.',
'''static void finish(int v, java.util.List<Integer>[] g,
                   boolean[] seen, java.util.List<Integer> order) {
  seen[v]=true;
  for(int u:g[v]) if(!seen[u]) finish(u,g,seen,order);
  order.add(v);
}
// First: finish(v, g, seen, order) from every unseen v.
// Reset seen. Traverse reverse(order) on transposed g.
// Each new DFS on the transpose labels one SCC.
// Use iterative DFS for graphs too deep for Java's stack.''','https://cp-algorithms.com/graph/strongly-connected-components.html')
lesson('Remember the right subproblem','Dynamic programming from state to reconstruction.','LCS & LIS|Edit distance|Knapsack & tree DP',[
('Define a state before writing a loop','A DP state must contain enough information to make future decisions independent of the forgotten past. Identify base cases, transitions, and a dependency order. Memoization evaluates reachable states on demand; tabulation evaluates in an explicit order.','For 0/1 knapsack, dp[w] is the best value with capacity w using processed items. Iterate w downward for each item. Iterating upward permits the same item repeatedly, solving a different problem.'),
('Align prefixes to compare sequences','Edit distance D[i][j] is the minimum edits converting a[0..i) into b[0..j). Initialize D[i][0]=i and D[0][j]=j. Take the minimum of deletion, insertion, and match/substitution. LCS uses a related prefix grid, but its objective is longest shared subsequence.','For “cat”→“cut”, substitution gives distance 1. A subsequence need not be contiguous. Edit distance takes O(nm) time, O(nm) space with reconstruction, or O(min(n,m)) for the distance alone.'),
('An optimized representation need not be the answer','For strictly increasing LIS, tails[k] stores the smallest possible ending value of a subsequence of length k+1. Replace the first tails value ≥ x using binary search. This is O(n log n); tails itself need not be a subsequence. Track predecessors to reconstruct.','Process [3,5,7,1,2,8]: tails evolves to [1,2,7,8]. That array is not a subsequence of the input, but its length 4 is correct. For nondecreasing LIS use the first value > x.'),
('Partition and tree states','For partition DP, let dp[i] be the best answer for the first i items and try every valid final segment j..i. On a rooted tree, combine child states after processing children. For maximum independent set, keep take[v] and skip[v].','take[v]=weight[v]+Σ skip[child]; skip[v]=Σ max(take[child],skip[child]). Store both choices because selecting the parent restricts which child states are legal.')],
'Assignment 4A: implement Edit Distance with reconstruction, LCS, and 0/1 knapsack. Write down states and loop order. Add LIS predecessor reconstruction as an extension.',
'''static int editDistance(String a, String b) {
  int[][] d=new int[a.length()+1][b.length()+1];
  for(int i=0;i<=a.length();i++) d[i][0]=i;
  for(int j=0;j<=b.length();j++) d[0][j]=j;
  for(int i=1;i<=a.length();i++)
    for(int j=1;j<=b.length();j++) {
      int cost=a.charAt(i-1)==b.charAt(j-1)?0:1;
      d[i][j]=Math.min(d[i-1][j]+1,
        Math.min(d[i][j-1]+1,d[i-1][j-1]+cost));
    }
  return d[a.length()][b.length()];
}''','https://cp-algorithms.com/dynamic_programming/longest_increasing_subsequence.html')
lesson('Match without starting over','KMP, prefix functions, and rolling hashes.','KMP preprocessing|Rolling hash|Rabin–Karp',[
('The prefix function remembers a useful border','π[i] is the length of the longest proper prefix of s[0..i] that is also its suffix. On mismatch, jump j to π[j−1] rather than decrementing once or restarting blindly. Each increase and fallback can be amortized, giving O(n) preprocessing.','For “ababaca”, π=[0,0,1,2,3,0,1]. At the c, fallback from border length 3 to 1, then 0. A proper prefix must be shorter than the full string.'),
('KMP reuses previous comparisons','Maintain how many pattern characters currently match the text suffix. A mismatch follows prefix links; a full match reports an occurrence and falls back to π[m−1], allowing overlaps. Total matching time is O(n+m). Define empty-pattern behavior separately.','Pattern “aba” in “ababa” matches at indices 0 and 2. Resetting matched length to zero after the first match would miss the overlapping occurrence.'),
('Hash windows in constant time','For H=c₀p^(m−1)+…+cₘ₋₁ mod M, remove c₀p^(m−1), multiply by p, then append the new symbol. Precompute the power once. Equal hashes are candidates, not proof of equal strings. Verify characters when exact correctness is required.','Hnext=((H−out·p^(m−1))·p+in) mod M. Normalize negative Java remainders. At p=1, “ab” and “ba” have the same sum, so collisions become easy. Modular products must fit in long.')],
'Assignment 4B: implement KMP preprocessing and search, plus polynomial rolling hash. Cross-check against naive matching, including overlaps. Deliberately demonstrate a collision with base 1.',
'''static int[] prefix(String s) {
  int[] pi=new int[s.length()];
  for(int i=1;i<s.length();i++) {
    int j=pi[i-1];
    while(j>0 && s.charAt(i)!=s.charAt(j)) j=pi[j-1];
    if(s.charAt(i)==s.charAt(j)) j++;
    pi[i]=j;
  }
  return pi;
}
static long roll(long h,long out,long in,long power,long p,long mod) {
  // Assumes nonnegative inputs and products fitting in long.
  long removed=(h-out*power%mod+mod)%mod;
  return (removed*p+in)%mod;
}''','https://cp-algorithms.com/string/prefix-function.html')
lesson('Index a whole text','Suffix arrays, Kasai LCP, and Aho–Corasick.','Prefix doubling|Kasai|Multi-pattern matching',[
('Sort suffixes by ranks of growing blocks','A suffix array lists starting positions in lexicographic suffix order. Prefix doubling sorts pairs (rank[i],rank[i+k]) with an out-of-range sentinel rank −1, then assigns new ranks and doubles k. Comparison sorting per round gives O(n log²n); radix/counting sorts give O(n log n).','For “banana”, SA=[5,3,1,0,4,2], corresponding to a, ana, anana, banana, na, nana. Sorting just first characters cannot distinguish the three suffixes starting with a.'),
('Kasai reuses almost all of the previous match','Define LCP[r] as the common-prefix length of SA[r] and SA[r−1], with LCP[0]=0. Build inverse ranks. Process suffixes in text order, compare with the previous suffix in SA, and decrement the carried match length by at most one after each step. Total comparisons are O(n).','For banana, LCP=[0,1,3,0,0,2]. The longest repeated substring has length max(LCP)=3: “ana”. This LCP convention matters when comparing code or examples.'),
('Aho–Corasick matches a dictionary in one scan','Build a trie of all patterns, then BFS failure links to the longest proper suffix that is a trie prefix. On a missing transition, follow failures. Report terminal outputs including suffix matches via output links. With constant-time transitions, scanning costs O(text length + matches), after construction.','With patterns “he”, “she”, “hers”, “his”, scanning “ushers” reports “she” and “he” ending at index 3, then “hers” ending at index 5. Reporting only the current terminal misses suffix patterns.')],
'Implement prefix-doubling suffix array and Kasai. Validate against sorting explicit suffixes on small inputs. Build Aho–Corasick and test overlapping and suffix-related patterns.',
'''static int[] kasai(String s, int[] sa) {
  int n=s.length(), h=0;
  int[] rank=new int[n], lcp=new int[n];
  for(int r=0;r<n;r++) rank[sa[r]]=r;
  for(int i=0;i<n;i++) {
    int r=rank[i];
    if(r==0) { h=0; continue; }
    int j=sa[r-1];
    while(i+h<n && j+h<n && s.charAt(i+h)==s.charAt(j+h)) h++;
    lcp[r]=h;
    if(h>0) h--;
  }
  return lcp;
}''','https://cp-algorithms.com/string/suffix-array.html')
Path('content.json').write_text(json.dumps(lessons,ensure_ascii=False,indent=2))
