#include <iostream>
#include <vector>
#include <string>

#include <cmath>
// max() abs() ceil() floor() log10() round() sqrt() sin() cos() pow()




using namespace std;

int main() {
	// your code goes here
	
	// Basics
	int n;
	vector<int> v;
	//push_back() pop_back() pop_front() push_front() front() end() insert() size() erase() clear() empty() begin() rbegin() rend()

	
	string s;
	// push_back() pop_back() length() begin() end() rbegin() rend() erase() insert() erase() find()
	
	
    cin>>n;
    int input;
    while(cin>>input)
        v.push_back(input);
        
    getline(cin, s);
    
    cout<<n<<endl;
    cout<<s;
    
    
    // Functions
    
    int getSum(int a, int b);            // Function Prototype
    
    int getSum(int a, int b)
    {
        return a+b;
    }
    
    
    
    // Semantics
    // value semantics - modifying the parameter will not affect the variable passed in.
    // refrence semantics (int& a) - modifying parameter will affect the variable passed in.
    
    
    // Strings (mutable)
    // size() / length() append() find() rfind() erase(index, length) insert() replace(ind, len, str)
    // substr(startIndex)  - grab upto end
    // substr(start, length)
    // Note - if find() can't find it returns == string::npos
    
    // "hi" + "there"    - illegal  (cause it's old c strings)
    // s+'a'  - legal (char conactenation is legal)
    // s1+s2   - legal (when we store it as string variable it becomes new c++ type strings)
    
    // stoi()   to integer
    // stod()   to double
    // to_string()  to convert something into string.
    
    
    string s;
    s+="char";
    
    
    
    // C++ STL
    
    #include <algorithm>
    
    vector<int> v = {1,2,3,4};
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    find(v.begin(), v.end());                 // [begin, end)   if not v.end()
    
    //for sorted arrays
    bool present = binary_search(v.begin(), v.end(), 5);   //false
    vector<int>::iterator it = lower_bound(v.begin(), v.end(), 100);   >=
    vector<int>::iterator it = upper_bound(v.begin(), v.end(), 100);   >
    
    cout<<*it<<endl;    //value at it pointing to.
    
    for (it = v.begin(); it!=v.end(); it++)
    {
        cout<<*it<<endl;
    }
    
    auto it = lower_bound(v.begin(), v.end(), 100)  // valid
    
    for(int x: v)
    {
        cout<<x;
    }
    
    for(int& x: v)   // iterate by refrence
    {
        x++;          //effects vector content
    }
    
    
    // sets  (inserting in O(logn), searching in O(logn), deletion in O(logn) because it maintains the order.
    
    #include <set>
    set<int> s;
    insert() 
    erase(val)
    it =  find(val)   // iterator to val else s.end()
    
    
    
    // Maps
    #include <map>
    map<int, int> A;
    //inserting(key) find(key)  erase(key)    // O(logn)
    
    A[1] = 100;
    
    
    
    // Unordered Map is a hash table .
    #include <unordered_map> 
    unordered_map<string, int> umap; 
    //find(key)  erase(key)                  // O(1)
    
    
    
    
    
        
	
	return 0;
}
