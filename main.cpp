#include <iostream>
using namespace std;

int main (){
    int idade;
    cout << "Digite sua idade: ";
    cin >> idade;
    if (idade >= 18) {
        cout << "Voce pode ser preso";
    }
    else {
        cout << "Voce vai pra FASE";
    }
    
    

    return 0;

}