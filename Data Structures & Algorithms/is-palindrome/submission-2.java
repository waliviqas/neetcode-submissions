class Solution {
    public boolean isPalindrome(String s) {
        // left = 0
        // right = s.length

        // while left < right

        // l = s.charAt(left)
        // r = s.charAt(right)

        // if !alphaNumeric(l)
        //     left++
        //     continue
        
        // if !alphaNumeric(r)
        //     right--
        //     continue
        
        // if !(left.lowercase = right.lowercase)
        //     return false

        // right--
        // left++

        // otherwise:
        //     return true

        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            char l = s.charAt(left);
            char r = s.charAt(right);

            if (!Character.isLetterOrDigit(l)) {
                left++;
                continue;
            }

            if (!Character.isLetterOrDigit(r)) {
                right--;
                continue;
            }

            if (Character.toLowerCase(l) != Character.toLowerCase(r)) {
                return false;
            }

            right--;
            left++;
        }

        return true;
    }
}
