class Solution {
    public boolean isPalindrome(String s) {

        // word: raar

        int left = 0; // 0 --> 1
        int right = s.length() - 1; // 3 --> 2

        while (left < right) {
            char l = s.charAt(left);
            char r = s.charAt(right);

            if (!Character.isLetterOrDigit(l)) { // r passes --> a passes
                left++;
                continue;
            }

            if (!Character.isLetterOrDigit(r)) { // r passes --> passes
                right--;
                continue;
            }

            if (Character.toLowerCase(l) != Character.toLowerCase(r)) { // r = r, this passes 
                return false;
            }

            left++; // move to left a 
            right--; // move to right a 
        }

        return true;

        // left = 0 
        // right = s.size - 1
        // while (left < right)
        //     l = s.charAt(left)
        //     r = s.charAt(right)
        //     if (!s.isLetterOrDigit(l)) 
        //         left++
        //         continue
        //     if (!s.isLetterOrDigit(r)) 
        //         right--
        //         continue
        //     if (l != r)
        //         return false 

        //     left++
        //     right--

        // return true
    }
}
