#include <vector>
#include <unordered_set>
#include <iostream>
#include <cassert>

int k = 4, t = 2, h = 3;
std::vector<std::vector<int>> leaves_b {
    {0, 0, 0, 0},
    {0, 0, 0, 0},
    {0, 0, 0},
    {0, 0, 0, 1},
    {0, 0, 1, 0},
    {0, 0, 0, 0},
    {0, 0, 0},
    {0, 0, 0, 1},
    {0, 0},
    {0, 0, 1, 0},
    {0, 0, 1},
    {0, 0, 1, 1},
    {0, 1, 0, 0},
    {0, 1, 0, 0},
    {0, 1, 0},
    {0, 1, 0, 1},
    {0, 1, 1, 0}
};
std::vector<std::vector<int>> leaves_d {
    {0, 0, 0, 1},
    {0, 0, 1, 1},
    {0, 0, 1},
    {0, 0, 1, 1},
    {0, 0, 0, 1},
    {0, 1, 1, 1},
    {0, 1, 1},
    {0, 1, 1, 1},
    {0, 1},
    {0, 1, 1, 1},
    {0, 1, 1},
    {0, 1, 1, 1},
    {0, 0, 0, 1},
    {0, 0, 1, 1},
    {0, 0, 1},
    {0, 0, 1, 1},
    {0, 0, 0, 1}
};

std::vector<std::vector<int>> leaves2_b {
    {0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 0, 1, 0, 0},
    {0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 0, 0, 0, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0, 1},
    {0, 0, 0},
    {0, 0, 0, 1, 0},
    {0, 0, 0, 1},
    {0, 0, 0, 1, 1},
    {0, 0, 1, 0, 0},
    {0, 0, 1, 0, 0},
    {0, 0, 1, 0},
    {0, 0, 1, 0, 1},
    {0, 0, 1, 1, 0},
    {0, 1, 0, 0, 0},
    {0, 1, 0, 0, 0},
    {0, 1, 0, 0, 0},
    {0, 1, 0, 0},
    {0, 1, 0, 0, 1},
    {0, 1, 0, 1, 0},
    {0, 1, 1, 0, 0}
};

std::vector<std::vector<int>> leaves2_d {
    {0, 0, 0, 1, 2},
    {0, 0, 1, 1, 2},
    {0, 0, 1, 2, 2},
    {0, 0, 1, 2},
    {0, 0, 1, 2, 2},
    {0, 0, 1, 1, 2},
    {0, 0, 0, 1, 2},
    {0, 1, 1, 1, 2},
    {0, 1, 1, 2, 2},
    {0, 1, 1, 2},
    {0, 1, 1, 2, 2},
    {0, 1, 1, 1, 2},
    {0, 1, 2, 2, 2},
    {0, 1, 2, 2},
    {0, 1, 2, 2, 2},
    {0, 1, 2},
    {0, 1, 2, 2, 2},
    {0, 1, 2, 2},
    {0, 1, 2, 2, 2},
    {0, 1, 1, 1, 2},
    {0, 1, 1, 2, 2},
    {0, 1, 1, 2},
    {0, 1, 1, 2, 2},
    {0, 1, 1, 1, 2},
    {0, 0, 0, 1, 2},
    {0, 0, 1, 1, 2},
    {0, 0, 1, 2, 2},
    {0, 0, 1, 2},
    {0, 0, 1, 2, 2},
    {0, 0, 1, 1, 2},
    {0, 0, 0, 1, 2}
};

std::vector<int> tmp_b;
std::vector<int> tmp_d;

int skipUntilNextLevel (std::vector<int>& curr_d, int i) 
{
    while ((i >= 0 && curr_d[i] == curr_d[i+1]) || i == curr_d.size() - 1) 
    {
        tmp_b[i] = 0;
        i --;
    }
    return i;
}

void getLevelPSuccessor (int idx, int p)
{
    tmp_b = leaves2_b[idx];
    tmp_d = leaves2_d[idx];

    int i = tmp_d.size() - 1;
    std::cout << "Start i in " << i << std::endl;
    std::cout << "Skipping bits below p\n";
    // skip bits "below p"
    while (i >= 0 && tmp_d[i] < p) 
    {
        tmp_b[i] = 0;
        i --;
    }
    std::cout << "After skipping i is " << i << std::endl;

    std::cout << "Calculating NES ";
    // Calculate number of Non-Empty Strings (NES): count unique values in tmp_d up until there
    size_t nes = std::unordered_set<int>( tmp_d.begin(), tmp_d.begin() + i + 1 ).size();
    std::cout << nes << std::endl;
    // Subtract the string that we currently look at (A, B only refers to strings "above")
    if (nes - 1 == k - 1) {
        // A: No next sibling on this layer
        std::cout << "Skipping a level\n";
        i = skipUntilNextLevel(tmp_d, i);
    }

    while (i >= 0) {
        // check if there was a level change
        if (i == tmp_d.size()-1 or tmp_d[i] != tmp_d[i+1]) 
        {
            std::cout << "Handling level change\n";
            // Calculate the Non-Leading Bits (NLB): take the complete length and subtract the number of NES (every NES has one leading bit)
            int nlb = (i + 1) - nes;
            nes --;
            std::cout << "NLB " << nlb << " i " << i << " NES " << nes << std::endl;
            if (nlb < t) 
            {
                std::cout <<  "Smaller than t\n";
                int new_index = tmp_d[i];
                i ++;
                if ((i + t - nlb + 1)  > tmp_b.size())
                {
                    tmp_b.insert(tmp_b.end(), t - nlb, 0);
                    tmp_b[i] = 1;
                    tmp_d.insert(tmp_d.end(), t - nlb, new_index);
                    i += t - nlb;
                }
                else 
                {
                    tmp_b[i] = 1;
                    tmp_d[i] = new_index;
                    int j = 1;
                    while (nlb + j < t) 
                    {
                        tmp_b [i + j] = 0;
                        tmp_d [i + j] = new_index;
                        j ++;
                    }
                    // remember the last changed position
                    i += j;
                }
                break;
            }
        }
        // For all following cases we know NLB == t        
        // Have to always check 0s - even when e.g. the first case applies
        if (tmp_b[i] == 0) 
        {
            if (i == 0 || tmp_d[i - 1] != tmp_d[i])
            {
                std::cout << "Found a 0 in the beginning\n";
                // The 0 is either the first bit in total, or it is the first bit of that level
                int strings_after_current = std::unordered_set<int> (tmp_d.begin() + i, tmp_d.end()).size();
                if (strings_after_current == h - tmp_d[i])
                {
                    // All bitstrings after the current level are non-empty, we simply move on
                    // C: No sibling on this layer
                    i --;
                    continue;
                }
                // We can use this level: Break out of the loop and start changing at the current i
                break;
            }
            else {
                assert (tmp_d[i - 1] == tmp_d[i]);
                std::cout << "A zero in the middle!\n";
                break;
            }
        }
        else 
        {
            std::cout << "start setting things to 0\n";
            // We can already start setting everything there to 0 and change where it belongs later
            tmp_b[i] = 0;
            i --;
        }
    }

    // A base case, we have reached the root: we are top
    // Special case of D
    if (i == -1) 
    {
        std::cout << "We are at top\n";
        tmp_d[0] = -1;
        return;
    }

    // Change where the bits belong
    std::cout << "Adjusting bit level\n";
    std::cout << "starting at " << i << std::endl; 
    
    int no_of_needed_nes = (k-1) - (nes+1);
    if (no_of_needed_nes == 0) {
        // special case: Don't add anything, remove everything after the current position
        tmp_d.resize(i);
        tmp_b.resize(i);
    }
    else {
        int set_index = tmp_d[i-1] + 1;
        // Fill up with just the next one as long as we still have bits
        std::cout << "Needed nes: " << no_of_needed_nes << std::endl;
        while (tmp_b.size() - i >= no_of_needed_nes) 
        {
            assert (i >= 0 && i < tmp_d.size());
            tmp_d[i] = set_index;
            i ++;
        }
        std::cout << "Filling singles\n";
        // Now assign the rest of the bits one level a piece
        while (i < tmp_b.size())
        {
            set_index ++;
            tmp_d[i] = set_index;
            i ++;
        }
    }

}

int compare(size_t idxA, size_t idxB, int pindex)
{
    auto& bitsA = leaves2_b[idxA];
    auto& indicesA = leaves2_d[idxA];
    auto& bitsB = leaves2_b[idxB];
    auto& indicesB = leaves2_d[idxB];

    // cases involving Top
    if (indicesA[0] == -1 and indicesB[0] == -1) return 0;
    if (indicesA[0] == -1) return 1;
    if (indicesB[0] == -1) return -1;
    
    for (int i=0; i < std::max(bitsA.size(), bitsB.size()); i++) {
        if (i >= bitsB.size())
        {
            return bitsA[i] == 0 ? -1: 1;
        }
        else if (i >= bitsA.size())
        {
            return bitsB[i] == 0 ? 1 : -1;
        }
        else if (indicesA[i] > pindex and indicesB[i] > pindex) {
            // equal until pindex, return 0
            return 0;
        } else if (indicesA[i] < indicesB[i]) {
            // equal until best has [eps]
            return bitsA[i] == 0 ? -1: 1;
        } else if (indicesA[i] > indicesB[i]) {
            // equal until tmp has [eps]
            return bitsB[i] == 0 ? 1 : -1;
        } else if (bitsA[i] < bitsB[i]) {
            // equal until tmp<best
            return -1;
        } else if (bitsA[i] > bitsB[i]) {
            // equal until tmp>best
            return 1;
        }
    }
    return 0;
}

int main(int argc, char *argv[])
{
    // Don't pass parameter = Go through all
    if (argc == 1) 
    {
        for (size_t idx = 0; idx < leaves2_b.size(); idx++)
        {
            getLevelPSuccessor(idx, h-1);
            if (tmp_b == leaves2_b[idx+1] && tmp_d == leaves2_d[idx+1] or (idx == leaves2_b.size() - 1 and tmp_d[0] == -1))
            {
                std::cout << idx << ": \033[32mCorrect successor!\n\033[0m";
            }
            else 
            {
                std::cout << idx << ": \033[31mWrong successor!\n\033[0m";
            }

            if (idx < leaves2_b.size() -1)
            {
                int fwd_res = compare (idx, idx+1, h-1);
                std::cout << idx << ": " << fwd_res << ( fwd_res == -1 ? " \033[32mCorrect forward comparison!\n\033[0m" : " \033[31mWrong forward comparison!\n\033[0m");
                
                int bwd_res = compare (idx+1, idx, h-1);
                std::cout << idx << ": " << bwd_res << (bwd_res == 1 ? " \033[32mCorrect backward comparison!\n\033[0m" : " \033[31mWrong backward comparison!\n\033[0m");
            }
        }
    }
    // Pass one parameter = only check that one and print result
    else if (argc == 2) 
    {
        int idx = atoi(argv[1]);

        getLevelPSuccessor(idx, h-1);
        std::cout << "Result: ";
        for (auto &&i : tmp_b)
        {
                std::cout << i;
        }
        std::cout << " ";
        for (auto &&i : tmp_d)
        {
                std::cout << i;
        }
        std::cout << std::endl;

        std::cout << "Expected: ";
        for (auto &&i : leaves2_b[idx + 1])
        {
                std::cout << i;
        }
        std::cout << " ";
        for (auto &&i : leaves2_d[idx + 1])
        {
                std::cout << i;
        }
        std::cout << std::endl;
    }
    // Pass more params = invalid
    else 
    {
        std::cout << "Too many params" << std::endl;
        return 1;
    }
   
}
