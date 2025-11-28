# Strahler Tree Experiments
Repository to hold some files to play around with Strahler trees.

## Labels in Code
Labels refer to conditions in page 19 of [this paper](https://arxiv.org/pdf/2003.08627):  
* _Cases where the siblings does not exist_
    * **A**: the number of non-empty strings among bitstrings h-1 and r+1 is k-1
    * **B**: the number of non-leadings bits in bitstrings h-1 to r+1 is t
    * **C**: bitstring r is 01^j for some j>=0, the number of non-leading bits used in bitstrings h-1 to r is t and all bitstrings r to 1 are non-empty
    * **D**: bitstring r is 1^j for some j>=1, and the number of non-leading bits used in bitstrings h-1 to r is t

* _Finding the sibling_
    * **E**: Less than t non-leading bits are used in bitstrings h-1 to r -> append 10^j with j>=0 to original string r, so that exactly t non-leading bits are used
    * **F**: Exactly t non-leading bits are used in bitstrings h-1 to r and r is in format b01^j for some j>=0 -> use b

* _Setting the remaining bits_
    * **G**: Set 00^j for some i>=0 so the total number of bits used is (k-1)+t
    * **H**: Add strings 0 so the number of non-empty bitstrings is k-1

## Command Line Arguments
The compiled binary can be used without or with one paramter:
* No parameter: Check every leaf in the tree against its successor
* One (integer) parameter: Check that specific leaf and output the result and expected result