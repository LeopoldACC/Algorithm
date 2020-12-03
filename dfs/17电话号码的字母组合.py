class Solution {
public:
    unordered_map<char,vector<char>> kb{{'2',{'a','b','c'}},{'3',{'d','e','f'}},{'4',{'g','h','i'}},{'5',{'j','k','l'}},{'6',{'m','n','o'}},{'7',{'p','q','r','s'}},{'8',{'t','u','v'}},{'9',{'w','x','y','z'}}};
    vector<string> res;
    string path;
    vector<string> letterCombinations(string digits) {
        if(digits.size()==0) return res;
        dfs(0,digits);
        return res;
    }
    void dfs(int cur,string digits)
    {
        if(path.size()==digits.size()) res.push_back(path);
        for(char ch:kb[digits[cur]])//kb[digits[cur]] = {a,b,c}
        {
            path+=ch;
            dfs(cur+1,digits);
            path.pop_back();
        }
    }
};