# Data-Structure-Unit-5-Case-Study-
A Python case study for Graphs and Trees. It models a city map as a weighted graph and uses Dijkstra’s algorithm to find the shortest route. It also builds a Huffman tree to encode and decode text using character frequencies.

# City Navigation and Huffman Coding

A Python case study for Unit 5: Graphs and Trees. It demonstrates two concepts using basic Python lists, loops, and classes:

1. **Weighted graph:** Models roads between cities and uses Dijkstra’s algorithm to find the shortest route.
2. **Huffman tree:** Counts character frequencies and assigns binary codes, with more frequent characters generally receiving shorter codes.

## Requirements

- Python 3.7 or newer
- No external packages required

## How to Run

Open a terminal in this folder and run:

```bash
python CaseStudy5.py
```

If your system uses `python3`, run:

```bash
python3 CaseStudy5.py
```

## Sample Output

See [`sample_output.txt`](sample_output.txt) for an example run.

The exact Huffman codes can vary when characters have equal frequencies, because either character may be placed on either side of the tree.

## Algorithms and Complexity

### City navigation

Dijkstra’s algorithm repeatedly chooses the unvisited city with the smallest known distance and checks its connected roads. This simple list-based version runs in approximately **O(V² + E)** time, where `V` is the number of cities and `E` is the number of roads.

### Huffman coding

The program counts each character, repeatedly combines the two nodes with the lowest frequencies, and traverses the resulting tree to assign codes. Finding the smallest nodes by scanning a list makes tree construction approximately **O(k²)**, where `k` is the number of distinct characters.

## Note

The Huffman section demonstrates how frequency-based codes are created and prints the encoded bits. It is an educational example, not a ZIP/GZIP file compressor. A complete file compressor also needs to save the tree or code table and pack the bits into bytes.

## Files

- `CaseStudy5.py` — City map and Huffman coding examples.
- `README.md` — Project overview and instructions.
- `sample_output.txt` — Example program output.