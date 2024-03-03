#include <iostream>
#include <string>
#include <unordered_set>

bool isUnique(const std::string& inputString) {
    std::unordered_set<char> hashtable;
    for (int i=0;i<inputString.size();i++) {
        hashtable.insert(inputString[i]);
    }

    if (hashtable.size() < inputString.size()) {
        return false;
    }
    return true;
}

int main() {
    std::cout << isUnique("asde") << '\n';

    return 0;
}