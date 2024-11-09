class Solution {
public:
    bool isPalindrome(string s) {
        int l=0,h=s.length()-1;

        while(l<h)
          if(!isalnum(s[l])) l++;
          else if(!isalnum(s[h])) h--;
          else if(tolower(s[l])!=tolower(s[h])) return 0;
          else l++,h--;
        
        return 1;
    }
};