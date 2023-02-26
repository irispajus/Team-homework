class Solution {
public:

    bool isPalindrome(int x) {
        string xs = to_string(x);

        string xr = xs;
        reverse(xr.begin(), xr.end());
        if (xs == xr) return true;
        else return false;

    }
};