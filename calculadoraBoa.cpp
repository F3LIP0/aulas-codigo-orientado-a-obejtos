#include <iostream>
using namespace std;

    float soma(float a, float b) {
        return a + b;
    } 
    float subtracao(float a, float b) {
        return a - b;
    }
    float multiplicacao(float a, float b) {
        return a * b;
    }
    float divisao(float a, float b) {
        if (b != 0) {
             return a / b;
        } else {
            return 0;
        }
       
    }


int main (){
    float num1, num2;
    char operacao;
    int stop = true;

    cout << "Digite o primeiro numero: ";
    cin >> num1;
    cout << "Digite o segundo numero: ";
    cin >> num2;

    cout << "Escolha uma operacao (1- Soma, 2- subtração, 3- multiplicação, 4- divisão) " << endl;
    cin >> operacao;

    if (operacao = 1) {
       cout << soma (num1, num2) << endl;
    } else if (operacao = 2) {
        cout << subtracao (num1, num2) << endl;
    } else if (operacao = 3) {
        cout << multiplicacao (num1, num2) << endl;
    } else if (operacao = 4){
        cout << divisao (num1, num2) << endl;
    } else {
        cout << "Operação invalida" << endl;
    }
    int a = 1;

    cout << "Deseja continuar o programa (1- sim, 2-nao)";
    cin >> a;

    if (a = 2){
    stop = false;
    }
    return 0; 
}