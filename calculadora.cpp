#include<iostream>
using namespace std;
int main (){
    int num1, num2;
    char operacao;
    int stop = true;
    cout << "Digite o primeiro numero: ";
    cin >> num1;
    cout << "Digite o segundo numero: ";
    cin  >> num2;

    cout << "Escolha a operação (+, -, *, /): ";
    cin >> operacao;

    if (operacao == '+') {
        cout << "Sua soma ficou " << (num1 + num2) << endl;
    } else if (operacao == '-') {
        cout << "Sua subtraçaõ ficou " << (num1 - num2) << endl;
    } else if (operacao == '*') {
        cout << "Sua multiplicação ficou " << (num1 * num2) << endl;
    } else if (operacao == '/') {
        if (num2 != 0) {
        cout << "Sua divisão ficou " << (num1 / num2) << endl;
        }
    }
    else {
        cout << "Operação invalida" ;
    }
    int a = 1;
    cout << "Deseja encerrar o programa? (1 - sim / 2 - não) ";
    cin >> a;
    if (a ==1) {
        stop = false;
    }

    return 0;
}